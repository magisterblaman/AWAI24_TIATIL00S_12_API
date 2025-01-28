import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

params = {
    "api_key": os.environ.get("CALENDARIFIC_API_KEY"),
    "country": "de",
    "year": 2025
}

my_headers = {
    "API-Key": os.environ.get("CALENDARIFIC_API_KEY")
}

body = {
    "hej": "då"
}

response = requests.get("https://calendarific.com/api/v2/holidays",
                        params, headers=my_headers, data=json.dumps(body))

data = response.json()

print(data)