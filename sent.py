import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Create a client
key = os.getenv('AZURE_API_KEY')
endpoint = 'https://soren-sentiment.cognitiveservices.azure.com/'
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Define documents
documents = [
    {"id": "1", "language": "en", "text": "I hated the movie. It was so slow!"},
    {"id": "2", "language": "en", "text": "The movie made it into my top ten favorites."},
    {"id": "3", "language": "en", "text": "What a great movie!"}
]

# Get sentiment
resp = client.analyze_sentiment(documents=documents)
print(resp)
