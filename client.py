from PIL import Image
import pytesseract
import enchant
import nltk
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


class Client:
    def __init__(self, azure_endpoint: str, azure_key: str):
        self.azure_client = TextAnalyticsClient(
            endpoint=azure_endpoint, credential=AzureKeyCredential(azure_key))
        self.dictionary = enchant.Dict('en_US')
        self.documents = []