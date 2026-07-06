import requests
import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://api.collegefootballdata.com"


def get_teams():
    url = f"{BASE_URL}/teams"

    headers = {
        "Authorization": f"Bearer {os.getenv('CFBD_API_KEY')}"
    }

    response = requests.get(url, headers=headers)

    response.raise_for_status()

    return response.json()