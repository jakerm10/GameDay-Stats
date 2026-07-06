from Etl.fetch.teams import fetch_teams
from Etl.transform.teams import transform_teams
from Etl.load.teams import load_teams


def main():

    print("Fetching teams...")
    raw_teams = fetch_teams()
    print(f"Fetched {len(raw_teams)} teams")

    print("Transforming teams...")
    clean_teams = transform_teams(raw_teams)
    print(f"Transformed {len(clean_teams)} teams")

    print("Loading teams...")
    load_teams(clean_teams)

    print("Done!")


if __name__ == "__main__":
    main()