import numpy as np
import matplotlib.pyplot as plt

y = [1.418,1.301,1.27,1.171,1.141,1]
x = [0.480,0.435,0.400,0.350,0.330,0.250]
errorX = 0.01
errorY = 0.001
plt.errorbar(x,y,errorY,errorX,fmt="o")

plt.ylabel("(T^2/4π^2) (s^2)")
plt.xlabel("longitud(m)")
plt.title("TvsL")
plt.show()