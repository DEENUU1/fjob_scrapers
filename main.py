from tasks import run_jjit
import json


def lambda_handler(event, context):
    site_id = event.get("site_id")

    if site_id == "jjit":
        run_jjit()
    else:
        return {
            "statusCode": 400,
            "body": json.dumps(f"Site {site_id} not supported")
        }

    return {
        "statusCode": 200,
        "body": json.dumps(f"Scraping for site {site_id} completed")
    }
