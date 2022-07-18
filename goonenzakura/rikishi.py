import re
from enum import Enum


class Rikishi:
    def __init__(self, shikona: str, rank: str, results: str, kinboshi: int) -> object:
        self.shikona = shikona
        self.rank = rank
        self.parse_results(results)
        self.award_kinboshi(kinboshi)

    def parse_results(self, results):
        parse = re.match(
            r"^(?P<wins>\d{1,2})-(?P<losses>\d{1,2})(?:-(?P<kyujo>\d{1,2}))?(?:d)?(?P<prizes>\s[YJDGSK]+)?$",
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

    def award_kinboshi(self, kinboshi: int):
        if self.group() in [StableGroup.M1, StableGroup.M6, StableGroup.M11]:
            self.kinboshi = kinboshi
        else:
            self.kinboshi = 0

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

    def points(self) -> float:
        points = self.wins
        points += self.kinboshi * 2
        points += self.sansho * 3

        if self.wins >= 8:
            points += 1
        else:
            points -= 0.5

        if self.yusho:
            points += 5

        if self.junyusho:
            points += 3

        return points

    def to_dict(self):
        return {
            "shikona": self.shikona,
            "rank": self.rank,
            "wins": self.wins,
            "losses": self.losses,
            "kyujo": self.kyujo,
            "sansho": self.sansho,
            "yusho": self.yusho,
            "junyusho": self.junyusho,
            "kinboshi": self.kinboshi,
            "points": self.points(),
        }


class StableGroup(Enum):
    YO = 1
    SK = 2
    M1 = 3
    M6 = 4
    M11 = 5
