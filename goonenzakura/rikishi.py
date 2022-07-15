import re
from enum import Enum


class Rikishi:
    def __init__(self, shikona, rank, results) -> object:
        self.shikona = shikona
        self.rank = rank
        self.parse_results(results)

    def parse_results(self, results):
        parse = re.match(
            r"^(?P<wins>\d{1,2})-(?P<losses>\d{1,2})(?:-(?P<kyujo>\d{1,2}))?(?P<prizes>\s[YJGSK]+)?$",
            results,
        )
        parse_dict = parse.groupdict()

        self.wins = int(parse_dict["wins"])
        self.losses = int(parse_dict["losses"])

        if parse_dict["kyujo"] is None:
            self.kyujo = 0
        else:
            self.kyujo = int(parse_dict["kyujo"])

        self.yusho = False
        self.junyusho = False
        self.sansho = 0

        if parse_dict["prizes"] is not None:
            if "Y" in parse_dict["prizes"]:
                self.yusho = True

            if "J" in parse_dict["prizes"]:
                self.junyusho = True

            if "G" in parse_dict["prizes"]:
                self.sansho = self.sansho + 1

            if "S" in parse_dict["prizes"]:
                self.sansho = self.sansho + 1

            if "K" in parse_dict["prizes"]:
                self.sansho = self.sansho + 1

    def group(self) -> Enum:
        parse = re.match(r"^(?P<title>[YOSKM]{1})(?P<tier>\d{1,2})", self.rank)
        parse_dict = parse.groupdict()

        if parse_dict["title"] == "Y" or parse_dict["title"] == "O":
            return StableGroup.YO

        if parse_dict["title"] == "S" or parse_dict["title"] == "K":
            return StableGroup.SK

        if int(parse_dict["tier"]) >= 11:
            return StableGroup.M11

        if int(parse_dict["tier"]) >= 6:
            return StableGroup.M6

        return StableGroup.M1

    def pickable(self) -> bool:
        return self.kyujo < 15

    def score(self) -> int:
        pass


class StableGroup(Enum):
    YO = 1
    SK = 2
    M1 = 3
    M6 = 4
    M11 = 5