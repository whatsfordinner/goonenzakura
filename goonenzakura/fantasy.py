from goonenzakura import rikishi


class FantasyBanzuke:
    def __init__(self, competitors: list):
        self.banzuke = {}
        self.worst = FantasyPicks()
        self.best = FantasyPicks()

        for group in rikishi.StableGroup:
            self.banzuke[group] = []

        for competitor in competitors:
            self.banzuke[competitor.group()].append(competitor)

        self.calculate_worst()
        self.calculate_best()

    def calculate_worst(self):
        for group in rikishi.StableGroup:
            self.worst.picks[group] = self.find_lowest_points(group)

        self.worst.calculate_points()

    def calculate_best(self):
        for group in rikishi.StableGroup:
            self.best.picks[group] = self.find_highest_points(group)

        self.best.calculate_points()

    def find_lowest_points(self, group):
        candidate = None

        for wrestler in self.banzuke[group]:
            if wrestler.pickable():
                if candidate is None:
                    candidate = wrestler
                elif wrestler.points() < candidate.points():
                    candidate = wrestler

        return candidate

    def find_highest_points(self, group):
        candidate = None

        for wrestler in self.banzuke[group]:
            if wrestler.pickable():
                if candidate is None:
                    candidate = wrestler
                elif wrestler.points() > candidate.points():
                    candidate = wrestler

        return candidate


class FantasyPicks:
    def __init__(self):
        self.picks = {}
        self.points = 0

    def calculate_points(self):
        for pick in self.picks:
            self.points += self.picks[pick].points()

    def to_string(self):
        return f"""
Y/O: {self.picks[rikishi.StableGroup.YO].shikona}
S/K: {self.picks[rikishi.StableGroup.SK].shikona}
M1-M5: {self.picks[rikishi.StableGroup.M1].shikona}
M6-M10: {self.picks[rikishi.StableGroup.M6].shikona}
M11+: {self.picks[rikishi.StableGroup.M11].shikona}

Total: {self.points}
"""
