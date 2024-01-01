from tasks import run_jjit
import json


def main_handler(event, context):
    site_id = event.get("site_id")

    if site_id == "jjit":
        run_jjit()
    else:
        return

    return {
        "statusCode": 200,
        "body": json.dumps(f"Scraping for site {site_id} completed")
    }
