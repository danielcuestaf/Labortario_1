import numpy as np
import matplotlib.pyplot as plt

y = [0.0509,0.0428,0.0408,0.0347,0.0329,0.0253]
x = [0.480,0.435,0.400,0.350,0.330,0.250]
errorX = 0.01
errorY = 0.0001
plt.errorbar(x,y,errorY,errorX,fmt="o")


plt.ylabel("(T^2/4π^2) (s^2)")
plt.xlabel("longitud(m)")
plt.title("T^2vsL")
plt.show()