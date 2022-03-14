""" This module contains utils function for translating text
"""
# import json
import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]
VERSION_LT = "2018-05-01"


def translator_instance() -> LanguageTranslatorV3:
    """This function create an instance of the IBM Watson Language translator.

    Returns
    -------
    LanguageTranslatorV3
        instance of the IBM Watson Language translator
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version=VERSION_LT, authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator


def english_to_french(english_text: str) -> str:
    """This function translates from english to french

    Parameters
    ----------
    english_text : str
        english text to translate

    Returns
    -------
    str
        translated text
    """
    language_translator = translator_instance()
    response = language_translator.translate(
        text=english_text, model_id="en-fr"
    ).get_result()
    french_text = response["translations"][0]["translation"]
    return french_text


def french_to_english(french_text: str) -> str:
    """This function translates from french to english

    Parameters
    ----------
    french_text : str
        french text to translate

    Returns
    -------
    str
        translated text
    """
    language_translator = translator_instance()
    response = language_translator.translate(
        text=french_text, model_id="fr-en"
    ).get_result()
    english_text = response["translations"][0]["translation"]
    return english_text
