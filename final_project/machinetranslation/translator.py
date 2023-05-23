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

def english_to_french(e_t):
    #write the code here
    if not e_t:
        return None

    # Translate the text from English to French
    f_t = language_translator.translate(
        text=e_t,
        model_id='en-fr'
    ).get_result()

    return f_t['translations'][0]['translation']

def french_to_english(f_t):
    #write the code here
    if not f_t:
        return None

    # Translate the text from English to French
    e_t = language_translator.translate(
        text=f_t,
        model_id='fr-en'
    ).get_result()

    return e_t['translations'][0]['translation']
