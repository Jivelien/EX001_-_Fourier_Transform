import numpy as np
from math import pi, sqrt
from matplotlib import pyplot as plt

x = np.arange(0,5,1/1000)
y = np.cos(x*2*pi*3)+1
y=x
plt.plot(x,y)
plt.polar(x,y)

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

rho, phi = cart2pol(x,y)

BAC = (1)*(pi/180)
ABC = (90-BAC)*(pi/180)
BCA = 90*(pi/180)

AB = 1
BC = np.sin(BAC)
AC = np.cos(BAC)

plt.scatter(AC,BC)
plt.scatter(0,0)
plt.scatter(1,1)
