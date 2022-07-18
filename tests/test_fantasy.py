import unittest
from goonenzakura import fantasy, rikishi


class FantasyPicksPointsTestCase(unittest.TestCase):
    full_picks = {
        rikishi.StableGroup.YO: rikishi.Rikishi("Hakuho", "Y1e", "15-0 Y", 0),
        rikishi.StableGroup.SK: rikishi.Rikishi("Mitakeumi", "S1e", "8-7", 0),
        rikishi.StableGroup.M1: rikishi.Rikishi("Takanosho", "M2w", "11-4 GS", 1),
        rikishi.StableGroup.M6: rikishi.Rikishi("Enho", "M8e", "7-8", 0),
        rikishi.StableGroup.M11: rikishi.Rikishi("Terutsuyoshi", "M12w", "10-5", 0),
    }

    tests = [{"picks": {}, "points": 0}, {"picks": full_picks, "points": 67.5}]

    def setUp(self):
        self.testPicks = fantasy.FantasyPicks()

    def test_fantasy_picks_points(self):
        for test in self.tests:
            with self.subTest():
                self.testPicks.picks = test["picks"]
                self.testPicks.calculate_points()
                self.assertEqual(test["points"], self.testPicks.points)


class FantasyPicksToStringTestCase(unittest.TestCase):
    picks = {
        rikishi.StableGroup.YO: rikishi.Rikishi("Hakuho", "Y1e", "15-0 Y", 0),
        rikishi.StableGroup.SK: rikishi.Rikishi("Mitakeumi", "S1e", "8-7", 0),
        rikishi.StableGroup.M1: rikishi.Rikishi("Takanosho", "M2w", "11-4 GS", 1),
        rikishi.StableGroup.M6: rikishi.Rikishi("Enho", "M8e", "7-8", 0),
        rikishi.StableGroup.M11: rikishi.Rikishi("Terutsuyoshi", "M12w", "10-5", 0),
    }

    string = """
Y/O: Hakuho
S/K: Mitakeumi
M1-M5: Takanosho
M6-M10: Enho
M11+: Terutsuyoshi

Total: 67.5
"""

    def setUp(self):
        self.testPicks = fantasy.FantasyPicks()

    def test_fantasy_picks_to_string(self):
        self.testPicks.picks = self.picks
        self.testPicks.calculate_points()
        self.assertEqual(self.string, self.testPicks.to_string())


class FantasyBanzukePerGroupTestCase(unittest.TestCase):
    test_roster = [
        rikishi.Rikishi("Hakuho", "Y1e", "15-0 Y", 0),
        rikishi.Rikishi("Shodai", "O1w", "7-8", 0),
        rikishi.Rikishi("Wakatakakage", "S1e", "13-2 JG", 0),
        rikishi.Rikishi("Hoshoryu", "K1e", "9-6", 0),
        rikishi.Rikishi("Ura", "M2w", "10-3-2 S", 1),
        rikishi.Rikishi("Kiribayama", "M3e", "6-9", 0),
        rikishi.Rikishi("Tochinoshin", "M6e", "12-3 K", 1),
        rikishi.Rikishi("Chiyoshoma", "M8e", "8-7", 0),
        rikishi.Rikishi("Midorifuji", "M13w", "8-7", 0),
        rikishi.Rikishi("Tokushoryu", "M15e", "5-10", 0),
    ]

    def setUp(self):
        self.fantasy_banzuke = fantasy.FantasyBanzuke(self.test_roster)

    def test_find_highest_points(self):
        tests = [
            {
                "group": rikishi.StableGroup.YO,
                "shikona": "Hakuho",
            },
            {
                "group": rikishi.StableGroup.SK,
                "shikona": "Wakatakakage",
            },
            {
                "group": rikishi.StableGroup.M1,
                "shikona": "Ura",
            },
            {
                "group": rikishi.StableGroup.M6,
                "shikona": "Tochinoshin",
            },
            {
                "group": rikishi.StableGroup.M11,
                "shikona": "Midorifuji",
            },
        ]

        for test in tests:
            with self.subTest(group=test["group"]):
                self.assertEqual(
                    test["shikona"],
                    self.fantasy_banzuke.find_highest_points(test["group"]).shikona,
                )

    def test_find_lowest_points(self):
        tests = [
            {
                "group": rikishi.StableGroup.YO,
                "shikona": "Shodai",
            },
            {
                "group": rikishi.StableGroup.SK,
                "shikona": "Hoshoryu",
            },
            {
                "group": rikishi.StableGroup.M1,
                "shikona": "Kiribayama",
            },
            {
                "group": rikishi.StableGroup.M6,
                "shikona": "Chiyoshoma",
            },
            {
                "group": rikishi.StableGroup.M11,
                "shikona": "Tokushoryu",
            },
        ]

        for test in tests:
            with self.subTest(group=test["group"]):
                self.assertEqual(
                    test["shikona"],
                    self.fantasy_banzuke.find_lowest_points(test["group"]).shikona,
                )


class FantasyBanzukePicksTestCase(unittest.TestCase):
    test_roster = [
        rikishi.Rikishi("Hakuho", "Y1e", "15-0 Y", 0),
        rikishi.Rikishi("Kakuryu", "Y1w", "0-0-15", 0),
        rikishi.Rikishi("Shodai", "O1w", "7-8", 0),
        rikishi.Rikishi("Wakatakakage", "S1e", "13-2 JG", 0),
        rikishi.Rikishi("Hoshoryu", "K1e", "9-6", 0),
        rikishi.Rikishi("Ura", "M2w", "10-3-2 S", 1),
        rikishi.Rikishi("Kiribayama", "M3e", "6-9", 0),
        rikishi.Rikishi("Chiyoshoma", "M8e", "8-7", 0),
        rikishi.Rikishi("Tochinoshin", "M6e", "12-3 K", 1),
        rikishi.Rikishi("Midorifuji", "M13w", "8-7", 0),
        rikishi.Rikishi("Tokushoryu", "M15e", "5-10", 0),
    ]

    def setUp(self):
        self.fantasy_banzuke = fantasy.FantasyBanzuke(self.test_roster)

    def test_calculate_best(self):
        test = {
            rikishi.StableGroup.YO: "Hakuho",
            rikishi.StableGroup.SK: "Wakatakakage",
            rikishi.StableGroup.M1: "Ura",
            rikishi.StableGroup.M6: "Tochinoshin",
            rikishi.StableGroup.M11: "Midorifuji",
        }

        for group in test:
            self.assertEqual(
                test[group], self.fantasy_banzuke.best.picks[group].shikona
            )

    def test_calculate_worst(self):
        test = {
            rikishi.StableGroup.YO: "Shodai",
            rikishi.StableGroup.SK: "Hoshoryu",
            rikishi.StableGroup.M1: "Kiribayama",
            rikishi.StableGroup.M6: "Chiyoshoma",
            rikishi.StableGroup.M11: "Tokushoryu",
        }

        for group in test:
            self.assertEqual(
                test[group], self.fantasy_banzuke.worst.picks[group].shikona
            )
