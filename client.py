from PIL import Image
import pytesseract
import enchant
import nltk
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


class Client:
    """Handles all data processing. The intention is to call analyze_sentiment each article."""
    def __init__(self, azure_endpoint: str, azure_key: str, tesseract_path: str, image_path: str):
        self.azure_client = TextAnalyticsClient(
            endpoint=azure_endpoint, credential=AzureKeyCredential(azure_key))
        self.dictionary = enchant.Dict('en_US')
        self.documents = []
        self.image_path = image_path
        self.cum_sentiment = 0.0
        self.raw_text = ''
        self.clean_text = ''
        self.sentence_list = []
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        
    def image_to_string(self):
        """Uses Tesseract to convert an image to a string."""
        self.raw_text = pytesseract.image_to_string(Image.open(self.image_path))

    def clean_tesseract_resp(self):
        """Clean the response from Tesseract."""
        bad_chars = [';', ':', '!', "*", "|", "{", "}", "\n", "\t"]
        self.clean_text = ''.join((filter(lambda i: i not in bad_chars, self.raw_text)))

    def text_to_document(self):
        """Convert cleaned text to a 'document' before feeding to Azure."""
        i = 1
        for sentence in nltk.tokenize.sent_tokenize(self.clean_text):
            self.documents.append({"id": i, "language": "en", "text": sentence})
            i += 1
    
    def analyze_sentiment(self):
        resp = self.azure_client.analyze_sentiment(documents=self.documents)
        print(resp)
        # Loop over sentiment scores and add to cumulative sentiment variable.