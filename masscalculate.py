class masscalculate():
    def __init__(self, twoHundred, oneNinety, oneEighty, oneSeventy, lightWeight):
        self.twoHundred = twoHundred
        self.oneNinety = oneNinety
        self.oneEighty = oneEighty
        self.oneSeventy = oneSeventy
        self.lightWeight = lightWeight

    # method for calculating average bat speed of hitters over 200 pounds
    def twoHundredAvg(self):
        total = 0
        for speed in self.twoHundred:
            total += speed
        average = total / len(self.twoHundred)
        return ("%.2f" % average)

    # method for calculating average bat speed of hitters 191-200 pounds
    def oneNinetyAvg(self):
        total = 0
        for speed in self.oneNinety:
            total += speed
        average = total / len(self.oneNinety)
        return ("%.2f" % average)

    # method for calculating average bat speed of hitters 181-190 pounds
    def oneEightyAvg(self):
        total = 0
        for speed in self.oneEighty:
            total += speed
        average = total / len(self.oneEighty)
        return ("%.2f" % average)

    # method for calculating average bat speed of hitters 170-180 pounds
    def oneSeventyAvg(self):
        total = 0
        for speed in self.oneSeventy:
            total += speed
        average = total / len(self.oneSeventy)
        return ("%.2f" % average)

    # method for calculating average bat speed of hitters less than 170 pounds
    def lightWeightAvg(self):
        total = 0
        for speed in self.lightWeight:
            total += speed
        average = total / len(self.lightWeight)
        return ("%.2f" % average)