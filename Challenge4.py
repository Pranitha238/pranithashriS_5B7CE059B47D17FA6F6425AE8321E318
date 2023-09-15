class Batsman:
    def __init__(self, name, matches, total_score):
        self.name = name
        self.matches = matches
        self.total_score = total_score

    def calculate_avg(self):
        return self.total_score / self.matches

    def play(self):
        print("Batsman {} is batting.".format(self.name))


class Bowler:
    def __init__(self, name, matches, wickets):
        self.name = name
        self.matches = matches
        self.wickets = wickets

    def play(self):
        print("Bowler {} is bowling.".format(self.name))


batsman = Batsman("Sachin Tendulkar", 200, 15921)
bowler = Bowler("Shane Warne", 145, 708)

batsman.play()
bowler.play()