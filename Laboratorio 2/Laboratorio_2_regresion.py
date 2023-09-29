import numpy as np
import matplotlib.pyplot as plt

y = [0.0509,0.0429,0.0409,0.0347,0.0330,0.0253]
x = [0.480,0.435,0.400,0.350,0.330,0.250]
errorX = 0.001
errorY = 0.00001
plt.errorbar(x,y,errorY,errorX,fmt="+")

a = np.arange(0.215,0.515,0.01)
plt.plot(a,0.108*a-0.0024,linestyle='--',color='green')
plt.ylabel("(T^2/4π^2) (s^2)")
plt.xlabel("longitug(m)")
plt.title("Regresión lineal")
plt.show()