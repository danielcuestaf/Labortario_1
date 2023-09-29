import numpy as np
import matplotlib.pyplot as plt

y = [0.749956,0.732736,0.685584,0.6561,0.4096,0.25]
x = [0.1900,0.1800,0.1700,0.1600,0.1000,0.0500]

errorX = 0.0001
errorY = 0.0001

plt.errorbar(x,y,errorY,errorX,fmt="+")


plt.ylabel("(T^2/4π^2) (s^2)")
plt.xlabel("masa(kg)")
plt.title("T^2 vs m")
plt.show()