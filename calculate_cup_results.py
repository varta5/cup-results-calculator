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

def assign_points_to_competitors():
    pass

def assign_points_to_clubs():
    pass

def rank_clubs():
    pass

def render_results():
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Missing argument: path and name of CSV input file containing the individual results")
    filename_with_path = sys.argv[1]
    competitors = read_csv_file_of_individual_results(filename_with_path)
    points_mapping = read_calculation_logic_file("calculation_logic.json")
    assign_points_to_competitors()
    assign_points_to_clubs()
    rank_clubs()
    render_results()
