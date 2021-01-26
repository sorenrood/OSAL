import os
from client import Client
import pandas as pd
import plotly.express as px

# Define variables essential for the client to run
azure_endpoint = 'https://soren-sentiment.cognitiveservices.azure.com/'
azure_key = os.getenv('AZURE_API_KEY')
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = 'data/pic.jpg'

client = Client(azure_endpoint=azure_endpoint, azure_key=azure_key,
                tesseract_path=tesseract_path, image_path=image_path)

raw = client.image_to_string()
clean = client.clean_tesseract_resp(raw)
documents = client.text_to_document(clean)
resp = client.analyze_sentiment(documents)

sentimap = {}
sentimap['positive'] = 0
sentimap['negative'] = 0
sentimap['neutral'] = 0

for x in resp:
    sentimap['positive'] += x['confidence_scores']['positive']
    sentimap['negative'] += x['confidence_scores']['negative']
    sentimap['neutral'] += x['confidence_scores']['neutral']

data = {
    'positive': [sentimap['positive']],
    'negative': [sentimap['negative']],
    'neutral': [sentimap['neutral']],
}

print(data.items())