from PIL import Image
import pytesseract
import enchant
import nltk
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

class Client:
    def __init__(self):
        self.sentiment_endpoint = 'https://soren-sentiment.cognitiveservices.azure.com/'
        self.sentiment_key = os.getenv('AZURE_API_KEY')
        self.dictionary = enchant.Dict('en_US')
        

