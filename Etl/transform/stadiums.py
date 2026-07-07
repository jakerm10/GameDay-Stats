def transform_stadium(stadium):
    return {
        "cfbd_id": stadium.get("id"),
        "name": stadium.get("name"),
        "city": stadium.get("city"),
        "state": stadium.get("state"),
        "timezone": stadium.get("timezone"),
        "elevation": stadium.get("elevation"),
        "capacity": stadium.get("capacity"),
        "construction_year": stadium.get("constructionYear"),
        "grass": stadium.get("grass"),
        "dome": stadium.get("dome"),
    }


def transform_stadiums(stadiums):

    seen = set()
    clean_stadiums = []

    for stadium in stadiums:
        stadium_id = stadium.get("id")

        if stadium_id and stadium_id not in seen:
            clean_stadiums.append(transform_stadium(stadium))
            seen.add(stadium_id)

    return clean_stadiums