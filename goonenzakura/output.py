import csv


def start_csv():
    fields = [
        "year",
        "month",
        "type",
        "points",
    ]

    nested_objects = [
        "yo",
        "sk",
        "m1m5",
        "m6m10",
        "m11",
    ]

    rikishi_stats = [
        "shikona",
        "rank",
        "wins",
        "losses",
        "kyujo",
        "yusho",
        "junyusho",
        "sansho",
        "kinboshi",
        "points",
    ]

    for nested in nested_objects:
        for stat in rikishi_stats:
            fields.append(f"{nested}_{stat}")

    with open("basho.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()


def convert_results_to_csv(results: list, year: int, month: int):
    fields = [
        "year",
        "month",
        "type",
        "points",
    ]

    nested_objects = [
        "yo",
        "sk",
        "m1m5",
        "m6m10",
        "m11",
    ]

    rikishi_stats = [
        "shikona",
        "rank",
        "wins",
        "losses",
        "kyujo",
        "yusho",
        "junyusho",
        "sansho",
        "kinboshi",
        "points",
    ]

    for nested in nested_objects:
        for stat in rikishi_stats:
            fields.append(f"{nested}_{stat}")

    with open("basho.csv", "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        for result in results:
            result["year"] = year
            result["month"] = month
            writer.writerow(flatten_result(result))


def flatten_result(result: object):
    nested_objects = [
        "yo",
        "sk",
        "m1m5",
        "m6m10",
        "m11",
    ]

    for nested in nested_objects:
        for key, value in result[nested].items():
            result[f"{nested}_{key}"] = value
        del result[nested]

    return result
