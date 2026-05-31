import csv
import json
import sys

def read_csv_file_of_individual_results(filename_with_path):
    competitors = []
    with open(filename_with_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            competitors.append(row)
    print(f"Read {len(competitors)} competitors from input CSV file")
    return competitors

def read_calculation_logic_file(filename_with_path):
    with open(filename_with_path, "r", encoding="utf-8") as file:
        points_mapping = json.load(file)
    return points_mapping

def assign_points_to_competitors(competitors, points_mapping):
    for competitor in competitors:
        number_of_competitors_in_category = len([participant for participant in competitors if participant["Cat"] == competitor["Cat"]])
        competitor["NumberOfCompetitorsInCategory"] = number_of_competitors_in_category
        category_points_mapping = (
            points_mapping[str(number_of_competitors_in_category)]
            if str(number_of_competitors_in_category) in points_mapping
            else points_mapping["more"]
        )
        place = competitor["Pl"]
        try:
            int(place)
        except ValueError:
            competitor["CupPoints"] = 0
            continue
        competitor["CupPoints"] = (
            category_points_mapping[str(place)]
            if str(place) in category_points_mapping
            else category_points_mapping["rest"]
        )

def assign_points_to_clubs(competitors):
    club_points = {}
    for competitor in competitors:
        if competitor["Clb"] in club_points:
            club_points[competitor["Clb"]] += competitor["CupPoints"]
        else:
            club_points[competitor["Clb"]] = competitor["CupPoints"]
    return club_points

def convert_club_points_to_list(club_points):
    club_points_list = []
    for club in club_points:
        club_points_list.append({
            "ClubName": club,
            "Points": club_points[club]
        })
    return club_points_list

def order_clubs(club_points_list):
    club_points_list.sort(key=get_club_points, reverse=True)
    for index, club in enumerate(club_points_list, start=1):
        club["Place"] = index

def get_club_points(club):
    return club["Points"]

def rank_clubs(club_points_list):
    # handle ties as well
    points_to_places_map = {}
    for club in club_points_list:
        if str(club["Points"]) in points_to_places_map:
            points_to_places_map[str(club["Points"])].append(club["Place"])
        else:
            points_to_places_map[str(club["Points"])] = [club["Place"]]
    for club in points_to_places_map:
        points_to_places_map[club] = stringify_places(points_to_places_map[club])
    for club in club_points_list:
        club["Place"] = points_to_places_map[str(club["Points"])]
    return points_to_places_map

def stringify_places(places):
    places = [str(place) for place in places]
    return f'{"-".join(places)}.'

def render_results():
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Missing argument: path and name of CSV input file containing the individual results")
    filename_with_path = sys.argv[1]
    competitors = read_csv_file_of_individual_results(filename_with_path)
    points_mapping = read_calculation_logic_file("calculation_logic.json")
    assign_points_to_competitors(competitors, points_mapping)
    club_points = assign_points_to_clubs(competitors)
    club_points_list = convert_club_points_to_list(club_points)
    order_clubs(club_points_list)
    rank_clubs(club_points_list)
    render_results()
