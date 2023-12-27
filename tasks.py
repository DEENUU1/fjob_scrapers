import json
from dataclasses import asdict

import requests

from scrapers.justjoinit import (
    process as process_justjoinit,
)
from scrapers.justjoinit.get_content import CATEGORIES
from scrapers.justjoinit.get_content import scrape_jjit


def run_jjit():
    parsed_data = []

    try:
        for cat in CATEGORIES:
            scraped_data = scrape_jjit(category=cat)

            for content in scraped_data:
                process = process_justjoinit.JJITProcess()
                process.parse_html(content)
                processed_data = process.process()
                parsed_data.append(asdict(processed_data))
    except:
        pass

    headers = {'Content-Type': 'application/json'}
    print(json.dumps(parsed_data))
    requests.post("http://127.0.0.1:8000/api/offer/scrape/", data=json.dumps(parsed_data), headers=headers)


run_jjit()
