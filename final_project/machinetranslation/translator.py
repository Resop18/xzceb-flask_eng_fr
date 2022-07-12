# a program to translate english to french and french to english
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

language_translator.set_service_url(url)

# creates a french translation of the english provided
def english_to_french(english_text):
    if english_text=='':
        return ''
    model_id = 'en-fr'
    translation = language_translator.translate(text=english_text,model_id=model_id).get_result()
    return translation["translations"][0]["translation"]

# creates an english translation of the french provided
def french_to_english(french_text):
    if french_text=='':
        return ''
    model_id = 'fr-en'
    translation = language_translator.translate(french_text,model_id=model_id).get_result()
    return translation["translations"][0]["translation"]
