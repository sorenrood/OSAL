# https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/client-libraries-rest-api?tabs=version-3-1&pivots=programming-language-python
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def azure_sentiment(text, key):
    import requests
    documents = { 'documents': [
            { 'id': '1', 'text': text }
            ]}
    
    azure_key = key
    azure_endpoint = 'https://soren-sentiment.cognitiveservices.azure.com/'
    assert azure_key
    sentiment_azure = azure_endpoint + '/sentiment'
    
    headers   = {"Ocp-Apim-Subscription-Key": azure_key}
    response  = requests.post(sentiment_azure, headers=headers, json=documents)
    sentiments = response.json()
    return sentiments

key = os.getenv('AZURE_API_KEY')
endpoint = "https://soren-sentiment.cognitiveservices.azure.com/"
