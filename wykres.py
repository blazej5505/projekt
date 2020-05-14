import matplotlib.pyplot as plt 
from matplotlib import style
import random

style.use('seaborn')
fig = plt.figure()

def values():
    xs = []
    ys = []

    for i in range (0,11,2):
        x = i
        y = random.randrange(11)

        xs.append(x)
        ys.append(y)

    return xs, ys

plot1 = plt.subplot2grid((1,2), (0,0), colspan = 1, rowspan = 1)
plot2 = plt.subplot2grid((1,2), (0,1), colspan = 1, rowspan = 1)

x,y = values()
plot1.bar(x,y, label = 'Kinetic energy', color = 'orange')
plot1.set_xlabel("Electrone/Alfa/Protone")
plot1.set_ylabel("value in Joules")

x,y = values()
plot2.bar(x,y, label = 'velocity')
plot2.set_xlabel('Electrone/Aflfa/Protone')
plot2.set_ylabel("Value in elobws per 9192631770 periods of radiation corresponding to the transition between two superfine levels of the ground state of the cesium atom 133")
plot1.legend()
plot2.legend()
plt.show()