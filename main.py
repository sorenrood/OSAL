import os
from client import Client
import pandas as pd
import plotly.express as px

def divide_chunks(l, n):
    '''Divides the input list into groups of n, then returns.'''
    new_list = []
    for i in range(0, len(l), n):  
        new_list.append(l[i:i + n])
    return new_list

# Define variables essential for the client to run
azure_endpoint = 'https://soren-sentiment.cognitiveservices.azure.com/'
azure_key = os.getenv('AZURE_API_KEY')
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = 'data/The_Los_Angeles_Times_Fri__Dec_12__1941_.jpg'

client = Client(azure_endpoint=azure_endpoint, azure_key=azure_key,
                tesseract_path=tesseract_path, image_path=image_path)

raw = client.image_to_string()
clean = client.clean_tesseract_resp(raw)
documents = client.text_to_document(clean)
chunked_list = divide_chunks(documents, 10)
print(chunked_list[0])
input()
resp = client.analyze_sentiment(chunked_list[0])

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