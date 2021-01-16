import os
from client import Client

azure_endpoint = 'https://soren-sentiment.cognitiveservices.azure.com/'
azure_key = os.getenv('AZURE_API_KEY')
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = 'simple.jpg'

client = Client(azure_endpoint=azure_endpoint, azure_key=azure_key,
                tesseract_path=tesseract_path, image_path=image_path)

client.image_to_string()
client.clean_tesseract_resp()

