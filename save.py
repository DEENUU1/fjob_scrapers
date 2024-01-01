import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

STATUS = os.environ.get("STATUS")

if STATUS == "prod":
    BASE_URL = os.environ.get("URL_PROD")
    TOKEN = os.environ.get("TOKEN_PROD")
else:
    BASE_URL = os.getenv("URL_DEV")
    TOKEN = os.getenv("TOKEN_DEV")


def save_scraped_data(data) -> bool:
    try:
        headers = {"Content-Type": "application/json", "Authorization": f"Token {TOKEN}"}
        response = requests.post(
            BASE_URL,
            headers=headers,
            data=json.dumps(data)
        )
        if response.status_code == 201:
            return True
        return False

    except Exception as e:
        print(e)
        return False
