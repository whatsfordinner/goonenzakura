import unittest
from goonenzakura import rikishi


class RikishigroupTestCase(unittest.TestCase):
    tests = [
        {"rank": "Y1e", "group": rikishi.StableGroup.YO},
        {"rank": "O1w", "group": rikishi.StableGroup.YO},
        {"rank": "S2e", "group": rikishi.StableGroup.SK},
        {"rank": "K1w", "group": rikishi.StableGroup.SK},
        {"rank": "M1w", "group": rikishi.StableGroup.M1},
        {"rank": "M4e", "group": rikishi.StableGroup.M1},
        {"rank": "M6w", "group": rikishi.StableGroup.M6},
        {"rank": "M10e", "group": rikishi.StableGroup.M6},
        {"rank": "M11w", "group": rikishi.StableGroup.M11},
        {"rank": "M14e", "group": rikishi.StableGroup.M11},
    ]

    def setUp(self):
        self.testRikishi = rikishi.Rikishi("", "", "0-0", 0)

    def test_group(self):
        for test in self.tests:
            with self.subTest(rank=test["rank"]):
                self.testRikishi.rank = test["rank"]
                self.assertEqual(test["group"], self.testRikishi.group())


class RikishiPickableTestCase(unittest.TestCase):
    tests = [
        {"kyujo": 0, "pickable": True},
        {"kyujo": 8, "pickable": True},
        {"kyujo": 15, "pickable": False},
    ]

    def setUp(self):
        self.testRikishi = rikishi.Rikishi("", "", "0-0", 0)

    def test_pickable(self):
        for test in self.tests:
            with self.subTest(kyujo=test["kyujo"]):
                self.testRikishi.kyujo = test["kyujo"]
                self.assertEqual(test["pickable"], self.testRikishi.pickable())


class RikishiParseResultsTestCase(unittest.TestCase):
    tests = [
        {
            "result": "8-7",
            "wins": 8,
            "losses": 7,
            "kyujo": 0,
            "yusho": False,
            "junyusho": False,
            "sansho": 0,
        },
        {
            "result": "0-0-15",
            "wins": 0,
            "losses": 0,
            "kyujo": 15,
            "yusho": False,
            "junyusho": False,
            "sansho": 0,
        },
        {
            "result": "3-1-11",
            "wins": 3,
            "losses": 1,
            "kyujo": 11,
            "yusho": False,
            "junyusho": False,
            "sansho": 0,
        },
        {
            "result": "15-0 Y",
            "wins": 15,
            "losses": 0,
            "kyujo": 0,
            "yusho": True,
            "junyusho": False,
            "sansho": 0,
        },
        {
            "result": "12-3 JG",
            "wins": 12,
            "losses": 3,
            "kyujo": 0,
            "yusho": False,
            "junyusho": True,
            "sansho": 1,
        },
        {
            "result": "11-4 K",
            "wins": 11,
            "losses": 4,
            "kyujo": 0,
            "yusho": False,
            "junyusho": False,
            "sansho": 1,
        },
        {
            "result": "14-1 GS",
            "wins": 14,
            "losses": 1,
            "kyujo": 0,
            "yusho": False,
            "junyusho": False,
            "sansho": 2,
        },
    ]

    def setUp(self):
        self.testRikishi = rikishi.Rikishi("", "", "0-0", 0)

    def test_parse_results(self):
        for test in self.tests:
            with self.subTest(result=test["result"]):
                self.testRikishi.parse_results(test["result"])
                self.assertEqual(test["wins"], self.testRikishi.wins)
                self.assertEqual(test["losses"], self.testRikishi.losses)
                self.assertEqual(test["kyujo"], self.testRikishi.kyujo)
                self.assertEqual(test["yusho"], self.testRikishi.yusho)
                self.assertEqual(test["junyusho"], self.testRikishi.junyusho)
                self.assertEqual(test["sansho"], self.testRikishi.sansho)


class RikishiPointsTestCase(unittest.TestCase):
    tests = [
        {"result": "12-3", "kinboshi": 0, "points": 13},
        {"result": "7-8", "kinboshi": 1, "points": 8.5},
        {"result": "11-1-3 J", "kinboshi": 0, "points": 15},
        {"result": "14-1 YGS", "kinboshi": 2, "points": 30},
    ]

    def setUp(self):
        self.testRikishi = rikishi.Rikishi("", "", "0-0", 0)

    def test_score(self):
        for test in self.tests:
            with self.subTest(
                result=test["result"], kinboshi=test["kinboshi"], points=test["points"]
            ):
                self.testRikishi.parse_results(test["result"])
                self.testRikishi.kinboshi = test["kinboshi"]
                self.assertEqual(test["points"], self.testRikishi.points())
