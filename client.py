from PIL import Image
import pytesseract
import enchant
import nltk
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from typing import List

class Client:
    """Handles all data processing. The intention is to call analyze_sentiment each article."""
    def __init__(self, azure_endpoint: str, azure_key: str, tesseract_path: str, image_path: str):
        self.azure_client = TextAnalyticsClient(
            endpoint=azure_endpoint, credential=AzureKeyCredential(azure_key))
        self.dictionary = enchant.Dict('en_US')
        self.image_path: str = image_path
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        
    def image_to_string(self) -> str:
        """Uses Tesseract to convert an image to a string."""
        return pytesseract.image_to_string(Image.open(self.image_path))

    def clean_tesseract_resp(self, raw_text: str) -> str:
        """Clean the response from Tesseract. Will return a str."""
        bad_chars = [';', ':', '!', "*", "|", "{", "}", "\n", "\t"]
        return ''.join((filter(lambda i: i not in bad_chars, raw_text)))

    def text_to_document(self, clean_text: str) -> List[str]:
        """Convert cleaned text to a 'document' before feeding to Azure. Will return a List[str]."""
        documents = []
        i = 1 
        for sentence in nltk.tokenize.sent_tokenize(clean_text):
            documents.append({"id": i, "language": "en", "text": sentence})
            i += 1
        return documents
    
    def analyze_sentiment(self, documents: List[str]) -> str:
        return self.azure_client.analyze_sentiment(documents=documents)
