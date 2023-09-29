import numpy as np
import matplotlib.pyplot as plt

y = [0.0190,0.0186,0.0174,0.0166,0.0104,0.0063]
x = [0.1900,0.1800,0.1700,0.1600,0.1000,0.0500]
errorX = 0.0001
errorY = 0.0001
plt.errorbar(x,y,errorY,errorX,fmt="+")

a = np.arange(0.04,0.2,0.01)
plt.plot(a,0.0937*a+0.0014,linestyle='--',color='green')
plt.ylabel("(T^2/4π^2) (s^2)")
plt.xlabel("masa(kg)")
plt.title("Regresión lineal")
plt.show()