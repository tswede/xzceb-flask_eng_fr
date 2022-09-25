import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator))

language_translator.set_service_url(url)

#this function converts english text to french
def english_to_french(english_text): "english to french"
    translation_fr = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    frenchText = translation_fr['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation_eng = language_translator.translate(text=frenchText ,model_id='fr-en').get_result()
    englishText = translation_eng['translations'][0]['translation']
    return english_text
