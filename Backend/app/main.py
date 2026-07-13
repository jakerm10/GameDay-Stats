from Etl.fetch.teams import fetch_teams

from Etl.transform.teams import transform_teams
from Etl.load.teams import load_teams

from Etl.transform.stadiums import transform_stadiums
from Etl.load.stadiums import load_stadiums


def main():

    # Extract teams from CFBD API
    raw_teams = fetch_teams()

    print(f"Fetched {len(raw_teams)} teams")


    # Transform + load teams
    clean_teams = transform_teams(raw_teams)

    load_teams(clean_teams)

    print("Teams loaded")


    # Extract stadiums from team locations
    raw_stadiums = [
        team["location"]
        for team in raw_teams
        if team.get("location")
    ]

    # Transform + load stadiums
    clean_stadiums = transform_stadiums(raw_stadiums)

    print(f"Transformed {len(clean_stadiums)} stadiums")

    load_stadiums(clean_stadiums)

    print("Stadiums loaded")


    print("Done!")


if __name__ == "__main__":
    main()