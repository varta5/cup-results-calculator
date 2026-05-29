# cup-results-calculator

Simple Python script which calculates the results of a cup competition

## Setup

The rules for applying points based on the individual results needs to be provided in a file called _calculation_logic.json_. This is a JSON structured file, which includes the rules on how many points a competitor achieves, based on their individual ranking (place) and the number of competitors in the given category.

Example file showing the following logic:

- in categories where there is only one competitor, they receive 5 points
- in categories where there are two competitors, first place receives 6 points, second receives 4 points
- in categories where there are three competitors, first place receives 7 points, second receives 5 points, third receives 3 points
- in categories where there are four competitors, first place receives 8 points, second receives 6 points, all the rest receive 2 points
- in categories where there are more than four competitors, first place receives 9 points, second receives 7 points, third receives 5 points, all the rest receive 1 points

```json
// calculation_logic.json - available in the directory where the script is invoked from

{
  "1": {
    "1": 5
  },
  "2": {
    "1": 6,
    "2": 4
  },
  "3": {
    "1": 7,
    "2": 5,
    "3": 3
  },
  "4": {
    "1": 8,
    "2": 6,
    "rest": 2
  },
  "more": {
    "1": 9,
    "2": 7,
    "3": 5,
    "rest": 1
  }
}
```

## Running the script

The script needs to be invoked by providing the path and name of an input file as argument. This input file is the CSV formatted results of a competition, exported from FjwW application.

```sh
python calculate_cup_results.py individual_results.csv
```
