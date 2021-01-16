from PIL import Image
import pytesseract
import enchant
import nltk
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


class Client:
    def __init__(self, azure_endpoint: str, azure_key: str, tesseract_path: str, image_path: str):
        self.azure_client = TextAnalyticsClient(
            endpoint=azure_endpoint, credential=AzureKeyCredential(azure_key))
        self.dictionary = enchant.Dict('en_US')
        self.documents = []
        self.tesseract_path = tesseract_path
        self.image_path = image_path
        
    def image_to_string(self):
        pass

    def analyze_sentiment(self):
        pass

    def clean_tesseract_resp(self):
        pass