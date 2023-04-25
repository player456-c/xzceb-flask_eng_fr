""" print(json.dumps(translation, indent=2, ensure_ascii=False)) """

#import json
#import requests
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """ function docstring """
    if english_text == None:
        raise TypeError("It is a type error, I confirm.")
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    french_text=translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """ function docstring """
    if french_text == None:
        raise TypeError("It is a type error, I confirm.")
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    english_text=translation['translations'][0]['translation']
    return english_text

MYTEXT='Tuer le patron'

result=frenchToEnglish(MYTEXT)
print(result)
