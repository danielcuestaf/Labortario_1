import numpy as np
import math
import matplotlib.pyplot as plt

y = [math.sqrt(21.79),math.sqrt(15.72),math.sqrt(9.29),math.sqrt(5.9),math.sqrt(3.37),math.sqrt(2.09)]
x = [math.sqrt(0.09),math.sqrt(0.0625),math.sqrt(0.04),math.sqrt(0.0225),math.sqrt(0.01),math.sqrt(0.0025)]

errorX = 0.0001
errorY = 0.001

plt.errorbar(x,y,errorY,errorX,fmt="+")


plt.ylabel("T (s)")
plt.xlabel("Distancia(m)")
plt.title("T vs d")
plt.show()