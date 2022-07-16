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
