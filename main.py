import numpy as np
from math import pi, sqrt
from matplotlib import pyplot as plt

def plotting(x,y):
    ax = plt.gca()
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.plot(x, y)

x = np.arange(0,30,1/10)
#y = np.cos(x*(2*pi)/3)
#y = np.cos(x)+1
y = x*2

plt.polar(x,y)
plt.plot(x,y)
# x will define angle
# y will define radius

# for training, value 2 will be a full circle
#value_circle = 2
#xx = np.sin(x*2*pi/value_circle )
length=100
xx = np.sin(x[:length])
yy = y[:length] * np.cos(xx[:length])
plotting(xx, yy)
