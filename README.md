	
# ChatCare

## Descripción

__ChatCare__ es un proyecto educativo de chatbot orientado a salud mental. El proyecto está estructurado en varias etapas sucesivas:

* Elección de un notebook y dataset de partida.
* Ajuste del notebook para mejorar las respuestas de acuerdo con el dataset de partida.
* Evaluación de resultados del notebook.
* Estrategias de mejora del notebook:
 * Incremento del dataset original
 * Adaptación a otros datasets con estructura diferente
* Generación de conversaciones automática y manualmente, y guardado en formato JSONL de entrenamiento de GPT3-5turbo.
* Entrenamiento fine-tuning de GPT3-5turbo con ficheros de conversación JSONL para generar modelo orientado a salud mental.
* Prueba en chat playground del modelo generado mediante fine-tuning.

## Contenido del repositorio

Este repositorio incluye diversos notebooks ejecutables en entornos Jupyter locales (o en Google Colab), así como un script Python que utiliza PyTorch y Transformers, además de los ficheros de entrada necesarios (datasets) y de salida (JSONL y txt). También se incluye una carpeta con las presentaciones y la memoria del proyecto.

### Carpeta 00-notebook-original

En esta carpeta pueden encontrarse los siguientes archivos:

* __chatbot-for-mental-health-conversations.ipynb__: notebook del chat original, ajustado para ofrecer respuestas tomadas del dataset.
* __intents-original.json__: dataset original disponible en Kaggle. Este dataset contiene unas 30 etiquetas denominadas de forma genérica (fact-1, fact-2, etc.). Para su uso con el notebook debe renombrarse a intents.json.

### Carpeta 01-via1-notag
Esta carpeta contiene todos los archivos relacionados a la vía 1 en la que se han generado 100 conversaciones usando el sistema sin tags.

* __chatBot_NoEtiqueta.ipynb__: NoteBook utilizado para trabajar en la vía 1.
* __data_NoEtiqueta.json__: dataset creado para el modelo 1 y 4.
* __data_NoEtiqueta_2.json__: dataset creado para el modelo 2 y 4.
* __data_NoEtiqueta_3.json__: dataset creado para el modelo 3 y 4.
* __modelosl.zip__: Zip que contiene los 4 modelos utilizados para generar las conversaciones.

### Carpeta 02-via2-tag

*  __01-chatbot-for-mental-health-aggregate.ipynb__: notebook Python, variación del notebook original, que permite agregar entradas al dataset original desde otro dataset distinto.
*  __02-automatic_tagging.py__: script Python que, usando transformers, realiza etiquetado y agregado automático de prompts y respuestas de un dataset adicional en el dataset del formato original.
*  __03-chatbot-for-mental-health-generate-jsonl.ipynb__: notebook Python, variación del de agregado, que inyecta preguntas de usuario desde un dataset adicional en el chatbot original y guarda cada par prompt - respuesta en el formato JSONL que requiere GPT-3.5turbo para fine-tuning.
*  __cl_output_file_formatted.json__: dataset completo de PrinceAyush, formateado para mayor legibilidad. Este fichero se puede indicar como dataset adicional en el notebook 03-chatbot-for-mental-health-generate-jsonl.ipynb que genera el JSONL de fine-tuning.
*  __cl_output_file_formatted_short.json__: versión recortada de cl_output_file_formatted.json con las entradas 101 a 649, para ser usado con el script 02-automatic_tagging.py y generar un dataset ampliado en el formato del notebook original, llamado intents-auto.json que luego se puede utilizar con el notebook de generación del JSONL.
*  __intents.json__: versión definitiva del dataset original tras distintas iteraciones de agregado manual y generación automática.
*  __intents-auto.json__: versión de intents.json generada por el script de etiquetado automático. Contiene las entradas de intents-last-manual-addition y las procedentes de inyectar el contenido de cl_output_file_formatted_short.json en el script de etiquetado automático.
*  __intents-last-manual-addition.json__: versión de intents.json generada por el script de agregado manual tras iterar por las primeras 100 entradas de cl_output_file_formatted.json. Contiene las entradas del dataset original (con ciertas etiquetas renombradas para darle contenido semántico) más el resultado de las citadas 100 entradas.

### Carpeta 03-conversaciones-JSONL

* __conv-ft1.txt__: las 100 conversaciones generadas por la vía sin tag y que han sido creadas para ser usadas en el Fine-Tuning.
* __conv-ft2.jsonl__: pares de pregunta y respuesta generados automáticamente mediante el chatbot original con dataset con tag aumentado para ser usados en el Fine-Tuning.

### Reparto de trabajo

* __Presentación__: los tres integrantes participamos igual en esta parte.
* __Memoria__: los tres integrantes participamos igual en esta parte.
* __01-via1-notag__: Jesús Espadas.
* __02-via2-tag__: Ricardo Palomares Martínez.
* __Fine-Tuning__: Gabriele Petroni.
