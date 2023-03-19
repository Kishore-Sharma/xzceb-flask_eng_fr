'''
    Translator File
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=IAMAuthenticator(apikey)
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    '''
        Method To convert English To French
    '''
    #write the code here
    translation = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''
        Method To convert French To English
    '''
    #write the code here
    translation = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
