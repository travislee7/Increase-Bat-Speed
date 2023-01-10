import csv
from heightcalculate import heightcalculate
import matplotlib.pyplot as plt
from levelcalculate import levelcalculate
from masscalculate import masscalculate

# storing each row from hitting metadata csv file into its own list
file = open('metadata.csv', 'r')
data = list(csv.reader(file))
file.close()

# convert entire "session_height_in" column into floats for calculations
for i in data[1:]:
    i[2] = float(i[2])

# convert entire "session_mass_in" column into floats for calculations
for i in data[1:]:
    i[1] = float(i[1])

# convert entire "bat_speed_mph_max_x" column into floats for calculations
for i in data[1:]:
    i[8] = float(i[8])

# array that will store the bat speeds of all hitters taller than 6'0
TallBatSpeed = []

# array that will store the bat speeds of all hitters 5'9 - 6'0
MediumBatSpeed = []

# array that will store the bat speeds of all hitters shorter than 5'9
ShortBatSpeed = []

for i in data[1:]:
    if i[2] > 72.0:
        TallBatSpeed.append(i[8])
    elif 69.0 <= i[2] <= 72.0:
        MediumBatSpeed.append(i[8])
    else:
        ShortBatSpeed.append(i[8])

# array that will store the bat speeds of all hitters over 200 pounds
twoHundred = []
# array that will store the bat speeds of all hitters 191-200 pounds
oneNinety = []
# array that will store the bat speeds of all hitters 181-190 pounds
oneEighty = []
# array that will store the bat speeds of all hitters 170-180 pounds
oneSeventy = []
# array that will store the bat speeds of all hitters lower than 170 pounds
lightWeight = []

for j in data[1:]:
    if j[1] > 200:
        twoHundred.append(j[8])
    elif 190 < j[1] <= 200:
        oneNinety.append(j[8])
    elif 180 < j[1] <= 190:
        oneEighty.append(j[8])
    elif 170 <= j[1] <= 180:
        oneSeventy.append(j[8])
    else:
        lightWeight.append(j[8])

# array that will store the bat speeds of all hitters whose highest level is milb
milb = []
# array that will store the bat speeds of all hitters whose highest level is independent
independent = []
# array that will store the bat speeds of all hitters whose highest level is college
college = []
# array that will store the bat speeds of all hitters whose highest level is high school
hs = []

for h in data[1:]:
    if h[4] == 'milb':
        milb.append(h[8])
    elif h[4] == 'independent':
        independent.append(h[8])
    elif h[4] == 'college':
        college.append(h[8])
    else:
        hs.append(h[8])

# height correlation findings
obj = heightcalculate(TallBatSpeed, MediumBatSpeed, ShortBatSpeed)
print("The average bat speed for hitters taller than 6'0 is " + obj.TallAvgBatSpeed() + "mph.")
print("The average bat speed for hitters 5'9 - 6'0 is " + obj.MediumAvgBatSpeed() + "mph.")
print("The average bat speed for hitters shorter than 5'9 is " + obj.ShortAvgBatSpeed() + "mph.")

# bar chart for height vs bat speed
x_height = range(3)
height_labels = ["Shorter than 5'9", "5'9 - 6'0", "Taller than 6'0"]
y = [float(obj.ShortAvgBatSpeed()), float(obj.MediumAvgBatSpeed()), float(obj.TallAvgBatSpeed())]
plt.bar(x_height, y, color='green', align='center')
plt.title('Height vs Bat Speed')
plt.ylabel("Average Bat Speed (mph)")
plt.xticks(x_height, height_labels, rotation='horizontal')
plt.show()

print("")

# weight correlation findings
obj2 = masscalculate(twoHundred, oneNinety, oneEighty, oneSeventy, lightWeight)
print("The average bat speed for hitters weighing over 200 pounds is " + str(obj2.twoHundredAvg()) + "mph.")
print("The average bat speed for hitters weighing 191-200 pounds is " + str(obj2.oneNinetyAvg()) + "mph.")
print("The average bat speed for hitters weighing 181-190 pounds is " + str(obj2.oneEightyAvg()) + "mph.")
print("The average bat speed for hitters weighing 170-180 pounds is " + str(obj2.oneSeventyAvg()) + "mph.")
print("The average bat speed for hitters weighing less than 170 pounds is " + str(obj2.lightWeightAvg()) + "mph.")

# bar chart for weight vs bat speed
x_mass = range(5)
mass_labels = ['Less than 170', '170-180', '181-190','191-200', 'Over 200']
y = [float(obj2.lightWeightAvg()), float(obj2.oneSeventyAvg()), float(obj2.oneEightyAvg()),
     float(obj2.oneNinetyAvg()), float(obj2.twoHundredAvg())]
plt.bar(x_mass, y, color='blue', align='center')
plt.title('Weight vs Bat Speed')
plt.xlabel("LBS")
plt.ylabel("Average Bat Speed (mph)")
plt.xticks(x_mass, mass_labels, rotation='horizontal')
plt.show()

print("")

# playing level correlation findings
obj3 = levelcalculate(milb, independent, college, hs)

print("The average bat speed for hitters who play milb is " + str(obj3.milbAvg()) + "mph.")
print("The average bat speed for hitters who play independent is " + str(obj3.independentAvg()) + "mph.")
print("The average bat speed for hitters who play college is " + str(obj3.collegeAvg()) + "mph.")
print("The average bat speed for hitters who play high school is " + str(obj3.hsAvg()) + "mph.")

# bar chart for playing level vs bat speed
x_level = range(4)
level_labels = ["High School", "College", "Independent", "MILB"]
y = [float(obj3.hsAvg()), float(obj3.collegeAvg()), float(obj3.independentAvg()), float(obj3.milbAvg())]
plt.bar(x_level, y, color='red', align='center')
plt.title('Playing Level vs Bat Speed')
plt.xlabel("Highest playing level")
plt.ylabel("Average Bat Speed (mph)")
plt.xticks(x_level, level_labels, rotation='horizontal')
plt.show()