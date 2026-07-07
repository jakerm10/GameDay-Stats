def transform_team(team):
    return {
        "id": team.get("id"),
        "school": team.get("school"),
        "abbreviation": team.get("abbreviation"),
        "mascot": team.get("mascot"),
        "conference": team.get("conference"),
        "division": team.get("division"),
        "classification": team.get("classification"),
        "color": team.get("color"),
        "alternate_color": team.get("alternateColor"),
        "logo_url": (
            team.get("logos")[0]
            if team.get("logos")
            else None
        )
    }


def transform_teams(teams):
    return [
        transform_team(team)
        for team in teams
    ]