class heightcalculate():
    def __init__(self, tallData, mediumData, shortData):
        self.tallerData = tallData
        self.mediumData = mediumData
        self.shorterData = shortData

    # method for calculating average bat speed of hitters taller than 6'0
    def TallAvgBatSpeed(self):
        total = 0
        for speed in self.tallerData:
            total += speed
        average = total/len(self.tallerData)
        return ("%.2f" % average)

    # method for calculating average bat speed of hitters 5'9 - 6'0
    def MediumAvgBatSpeed(self):
        total = 0
        for speed in self.mediumData:
            total += speed
        average = total / len(self.mediumData)
        return ("%.2f" % average)

    # method for calculating average bat speed of hitters shorter than 5'9
    def ShortAvgBatSpeed(self):
        total = 0
        for speed in self.shorterData:
            total += speed
        average = total/len(self.shorterData)
        return ("%.2f" % average)