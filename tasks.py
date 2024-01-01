from save import save_scraped_data
from scrapers.justjoinit import (
    process as process_justjoinit,
)
from scrapers.justjoinit.get_content import CATEGORIES
from scrapers.justjoinit.get_content import scrape_jjit


def run_jjit():
    parsed_data = []

    for cat in CATEGORIES:
        scraped_data = scrape_jjit(category=cat)

        for content in scraped_data:
            process = process_justjoinit.JJITProcess(html=content)
            parsed_data.append(process.scraped_data)

    save = save_scraped_data(parsed_data)

    if save:
        print("Data saved successfully")
    else:
        print("Could not send scraped data via API")


run_jjit()
