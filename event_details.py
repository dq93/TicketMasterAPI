import requests
import pandas as pd
import json
import gzip
from io import BytesIO

"""
# you must have a local env file with your key
load_dotenv('/Users/sa22/Desktop/code/ticketMasterProject/TicketMasterAPI/ticketmasterAPIKey.env')

# load from a local env file with your key
API_KEY = os.getenv('TICKETMASTER_API_KEY')
if not API_KEY:
    raise ValueError("API Key not found. Ensure it is set in an env file.")
"""
URL = 'https://s3.amazonaws.com/prd141.dcfd.prod1.us-east-1.tmaws-feeds/20250129/EVENTS_RAW-US-17b2bd9a-895c-4bfd-8b44-6da9eb50a453-2025-01-29_031818.json.gz'

response = requests.get(URL)

if response.status_code == 200:
    response.raise_for_status()

    with gzip.GzipFile(fileobj=BytesIO(response.content)) as f:
        json_data = json.load(f)
    df = pd.json_normalize(json_data)

    df.to_csv('/Users/sa22/Desktop/code/ticketMasterProject/TicketMasterAPI/data/csv/jsonData.csv')

else:
    print("Error: Status response is: " + str(response.status_code))
