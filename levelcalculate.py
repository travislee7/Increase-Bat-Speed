class levelcalculate():
    def __init__(self, milb, independent, college, hs):
        self.milb = milb
        self.independent = independent
        self.college = college
        self.hs = hs

    # method for calculating average bat speed of hitters who played milb
    def milbAvg(self):
        total = 0
        for speed in self.milb:
            total += speed
        average = total / len(self.milb)
        return ("%.2f" % average)

    # method for calculating average bat speed of hitters who played independent
    def independentAvg(self):
        total = 0
        for speed in self.independent:
            total += speed
        average = total / len(self.independent)
        return ("%.2f" % average)

    # method for calculating average bat speed of hitters who played college
    def collegeAvg(self):
        total = 0
        for speed in self.college:
            total += speed
        average = total / len(self.college)
        return ("%.2f" % average)

    # method for calculating average bat speed of hitters who played high school
    def hsAvg(self):
        total = 0
        for speed in self.hs:
            total += speed
        average = total / len(self.hs)
        return ("%.2f" % average)