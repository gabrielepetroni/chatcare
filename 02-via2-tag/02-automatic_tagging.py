#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 20:11:18 2024

@author: rpalomares
"""

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# import plotly.graph_objects as go
import datetime
import time
import os
import json
from transformers import pipeline

def feed_data(extra_df):
    for i in range(len(extra_df)):
        yield extra_df.iloc[i]


# Adds or modifies a row in the original intents.json dataframe with the tag, prompt and response parameters
def add_prompt_response(init_df, tag, prompt, response):
    tagged_row_count = sum(init_df['tag'] == tag)
    print(f"Row count: {tagged_row_count}")
    
    if tagged_row_count == 0:
        print('New row to be added')
        new_row = {'tag': tag, 'patterns': [[prompt]], 'responses': [[response]]}
        df_new_row = pd.DataFrame(new_row)
        init_df = pd.concat([init_df, df_new_row], ignore_index=True)
    else:
        print(f'Modifying row with tag {tag}')
        # Identifies the row index containing the tag
        row_index = init_df.index[init_df['tag'] == tag][0]
        
        # Update 'patterns' column
        patterns_list = init_df.at[row_index, 'patterns']
        patterns_list.append(prompt)
        init_df.at[row_index, 'patterns'] = patterns_list
        
        # Updates 'responses' column
        responses_list = init_df.at[row_index, 'responses']
        responses_list.append(response)
        init_df.at[row_index, 'responses'] = responses_list
    
    return init_df


# Guarda el dataset
def save_dataset(init_df):
    result_array = []
    for i, fila in init_df.iterrows():
        fila_dict = {'tag': fila['tag'], 'patterns': fila['patterns'],
                     'responses': fila['responses']}
        result_array.append(fila_dict)
    result_dict = { "intents": result_array }
    # os.replace('./intents.json', './intents-old.json')
    
    with open('./intents-auto.json', 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, indent=4)


with open('intents.json', 'r') as f:
    data = json.load(f)
init_df = pd.DataFrame(data['intents'])
tags = init_df['tag']

with open('cl_output_file_formatted_short.json', 'r') as f:
    dataset_extra = json.load(f)
extra_df = pd.DataFrame(dataset_extra)
extra_df = extra_df.dropna(subset = ['questionTitle'])
extra_df = extra_df.drop_duplicates(subset = ['questionTitle'])
patterns = extra_df['questionTitle']

st = datetime.datetime.now()
classifier2 = pipeline(task="zero-shot-classification")
lines = 0
for val in feed_data(extra_df):
    lines = lines + 1
    result = classifier2(val['questionTitle'], candidate_labels=tags)
    add_prompt_response(init_df, result['labels'][0], val['questionTitle'], val['answerText'])
    print(result['labels'][0] + " - " + val['questionTitle'] + " - " + val['answerText'])

et = datetime.datetime.now()
elapsed_time = et - st

save_dataset(init_df)

print(f"Number of inputs processed: {lines}")
print(f"Elapsed time: {elapsed_time} seconds")
print(f"Average process time for each input: {(elapsed_time / lines)}")
