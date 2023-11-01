import numpy as np
import matplotlib.pyplot as plt

y = [21.79,15.72,9.29,5.9,3.37,2.09]
x = [0.09,0.0625,0.04,0.0225,0.01,0.0025]

errorX = 0.0001
errorY = 0.001

plt.errorbar(x,y,errorY,errorX,fmt="+")



a = np.arange(0.0025,0.1,0.01)
plt.plot(a,229.1*a+1.0,linestyle='--',color='green')
plt.ylabel("T^2 (s^2)")
plt.xlabel("Distancia(m^2)")
plt.title("Regresión lineal")
plt.show()
