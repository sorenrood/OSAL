# https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/client-libraries-rest-api?tabs=version-3-1&pivots=programming-language-python
# https://pypi.org/project/azure-ai-textanalytics/
import os
from azure.ai.textanalytics import TextAnalyticsClient
# from azure.ai.textanalytics import TextAnalyticsClient
# from azure.core.credentials import AzureKeyCredential
key = os.getenv('AZURE_API_KEY')