import requests
import json


def save_scraped_data(data) -> bool:
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            "http://127.0.0.1:8000/api/offer/scrape/",
            headers=headers,
            data=json.dumps(data)
        )
        if response.status_code == 201:
            return True
        return False

    except Exception as e:
        print(e)
        return False
