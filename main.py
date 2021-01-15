# https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk

from PIL import Image
import pytesseract
import enchant
import nltk
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Get text from image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open('pic.jpg'))

# Make dictionary checker and list to add true words to
d = enchant.Dict("en_US")
words = []

# Clean Data
bad_chars = [';', ':', '!', "*", "|", "{", "}", "\n", "\t"]
cleaned = ''.join((filter(lambda i: i not in bad_chars, text)))

# Tokenizing (convert into sentences)
sentence_list = nltk.tokenize.sent_tokenize(cleaned)

# Create document to send to azure
documents = []
i = 1
for sentence in sentence_list:
    documents.append({"id": i, "language": "en", "text": sentence})
    i += 1

# Create a client
key = os.getenv('AZURE_API_KEY')
endpoint = 'https://soren-sentiment.cognitiveservices.azure.com/'
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Get sentiment
resp = client.analyze_sentiment(documents=documents)
print(resp)
    