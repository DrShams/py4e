import os
#from google.cloud import translate
from google.cloud import translate_v2
#import pandas as pd
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"GoogleCloudKey_MyServiceAcct.json"

translate_client = translate_v2.Client()

#results = translate_client.get_languages()
#lang_list = pd.DataFrame(results)
#print(lang_list)
#for language in results:
#    print(u"{name} ({language})".format(**language))
text = 'Hello world'
target = 'ru'
result = translate_client.translate(
    text,
    target_language=target
)
#print(u"Text: {}".format(result["input"]))
#print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
print("Translation:",result["translatedText"])
