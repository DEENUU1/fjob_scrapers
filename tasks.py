from scrapers.justjoinit import (
    get_content as get_content_justjoinit,
    process as process_justjoinit,
)
from scrapers.justjoinit.get_content import CATEGORIES
from dataclasses import asdict
import requests
import json

def run_justjoinit():
    parsed_data = []

    try:
        for cat in CATEGORIES:
            scraper = get_content_justjoinit.GetJustJoinITContent(cat)
            scraper.fetch_content()

            for content in scraper.data:
                process = process_justjoinit.JJITProcess()
                process.parse_html(content)
                processed_data = process.process()
                parsed_data.append(asdict(processed_data))
    except:
        pass

    # try:
    headers = {'Content-Type': 'application/json'}
    print(json.dumps(parsed_data))
    requests.post("http://127.0.0.1:8000/api/offer/scrape/", data=json.dumps(parsed_data), headers=headers)
    # except Exception as e:
    #     print(e)

run_justjoinit()
