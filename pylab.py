from math import pi
from matplotlib import pylab as pl
x = pl.linspace(-pi, pi , 200)
y = pl.sin(x)
y1 = pl.sin(x*x)
pl.plot(x,y)
pl.plot(x,y1, 'r')
pl.show()
