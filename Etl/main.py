import os
import requests
from dotenv import load_dotenv

load_dotenv("../backend/.env")

API_KEY = os.getenv("CFBD_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

url = "https://api.collegefootballdata.com/teams/fbs"

response = requests.get(url, headers=headers)

print(response.status_code)

print(response.json()[:3])

import json

if response.status_code == 200:
    teams = response.json()

    with open("teams.json", "w") as file:
        json.dump(teams, file, indent=4)

    print("Saved team data to teams.json")