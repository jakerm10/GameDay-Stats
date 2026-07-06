from Backend.app.api.cfbd_client import get_teams
import json


def save_raw_teams(teams):

    with open("Etl/teams.json", "w") as file:
        json.dump(
            teams,
            file,
            indent=4
        )

def fetch_teams():
    return get_teams()