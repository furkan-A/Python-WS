from matplotlib import pyplot
import numpy as np

x = [1,2,3,4]
y = [1,4,9,16]
"""
pyplot.plot(x, y, "o--r") # color = "green", linewidth = "7")
pyplot.axis([0,5,0,18])
pyplot.title("Kare Grafik")
pyplot.xlabel("x Ekseni")
pyplot.ylabel("y Ekseni")
"""
# toplu grafik 

x = np.linspace(0,2,100)

pyplot.plot(x, x, label = "Linear")
pyplot.plot(x, x**2, label = "Quadratic")
pyplot.plot(x, x**3, label = "Cubic")

pyplot.xlabel("x Ekseni")
pyplot.ylabel("y Ekseni")

pyplot.legend(loc = 2)

pyplot.savefig("fig.png")
pyplot.show()

# PASTA GRAFIK

goal_types = "Penalti", "Sut", "Serbest Vurus"

goals = [7,21,11]
colors = ["r", "g", "b"]

pyplot.pie(goals, labels = goal_types, colors = colors, shadow = True, explode = (0.05, 0.05, 0.05), autopct = "%1.1f%%")

pyplot.show()

# BAR GRAFIK

pyplot.bar([1,2,3,4], [20,40,10,30], label= "Volvo", width=.5)
pyplot.bar([1.5,2.5,3.5,4.5], [50,30,10,20], label= "Tesla", width=.5)

pyplot.legend()

pyplot.xlabel("Day")
pyplot.ylabel("Distance (km)")
pyplot.title("Car Information")

pyplot.show()
