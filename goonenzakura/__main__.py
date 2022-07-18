import argparse
import sys
from goonenzakura import fantasy, sumodb, output
from pprint import pprint


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="goonenzakura",
        description='Find the "optimal" sumo fantasy stable according to the Something Awful forums fantasy sumo competition',
    )
    args = parser.parse_args()

    starting_year = 1958
    months = [1, 3, 5, 7, 9, 11]

    output.start_csv()

    for year in range(starting_year, 1962):
        for month in months:
            results = sumodb.get_basho_stats(year=year, month=month)
            fantasy_banzuke = fantasy.FantasyBanzuke(results)
            result_dict = fantasy_banzuke.results_to_dict()
            output.convert_results_to_csv(result_dict, year, month)

    return 0


sys.exit(main())
