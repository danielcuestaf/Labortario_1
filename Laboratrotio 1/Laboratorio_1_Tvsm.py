import numpy as np
import matplotlib.pyplot as plt

y = [0.866,0.856,0.828,0.81,0.64,0.5]
x = [0.1900,0.1800,0.1700,0.1600,0.1000,0.0500]

errorX = 0.0001
errorY = 0.0001

plt.errorbar(x,y,errorY,errorX,fmt="+")


plt.ylabel("(T^2/4π^2) (s^2)")
plt.xlabel("masa(kg)")
plt.title("T vs m")
plt.show()