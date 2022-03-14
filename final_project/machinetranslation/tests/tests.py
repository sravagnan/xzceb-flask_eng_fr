""" This module contains unit tests for the translating functions
"""
import unittest

from translator import english_to_french, french_to_english, translator_instance


class TestTranslator(unittest.TestCase):
    """This class tests the Translator instance"""

    service_url = "https://api.us-south.language-translator.watson.cloud.ibm.com"
    service_name = "language_translator"
    sdk_name = "ibm-python-sdk-core"

    def test1(self):
        """This method tests defaul service url, service name and sdk name"""
        self.assertEqual(
            translator_instance().DEFAULT_SERVICE_URL, self.service_url
        )  # test default defaul service url.
        self.assertEqual(
            translator_instance().DEFAULT_SERVICE_NAME, self.service_name
        )  # test service name.
        self.assertEqual(
            translator_instance().SDK_NAME, self.sdk_name
        )  # test default sdk name.


class TestE2F(unittest.TestCase):
    """This class tests the english_to_french function"""

    def test1(self):
        """This method tests translation from english to french"""
        self.assertEqual(english_to_french(" "), " ")
        self.assertEqual(
            english_to_french("Hello"), "Bonjour"
        )  # test when Hello is given as input the output is Bonjour.
        self.assertEqual(
            english_to_french("Hello, how are you today?"),
            "Bonjour, comment vous êtes aujourd'hui?",
        )  # test when "Hello, how are you today?" is given as input the output is "Bonjour, comment vous etes aujourd'hui?".


class TestF2E(unittest.TestCase):
    """This class tests the french_to_english function"""

    def test1(self):
        """This method tests translation from french to english"""
        self.assertEqual(french_to_english(" "), " ")
        self.assertEqual(
            french_to_english("Bonjour"), "Hello"
        )  # test when Bonjour is given as input the output is Hello.
        self.assertEqual(
            french_to_english("Bonjour, comment vous êtes aujourd'hui?"),
            "Hello, how are you today?",
        )  # test when "Bonjour, comment vous etes aujourd'hui?" is given as input the output is "Hello, how are you today?".


unittest.main()
