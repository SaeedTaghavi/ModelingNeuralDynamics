import numpy as np
import matplotlib.pyplot as plt
from math import pi
theta = np.arange(0,101,1)
theta = theta /100.
theta = theta * 2.*pi

x=np.cos(theta)
y=np.sin(theta)

theta0=-0.4*pi
x0=np.cos(theta0)
y0=np.sin(theta0)
eps=0.15

plt.figure(figsize=(5,5))

plt.scatter(x0,y0,s=1000*eps)
#plt.fill(x0+eps*x,y0+eps*y)
y0=-y0
plt.scatter(x0,y0,s=1000*eps,facecolors='none', edgecolors='r')
#plt.fill(x0+eps*x,y0+eps*y,'r')
plt.plot(x,y)
plt.ylim((-1.5,1.50))
plt.xlim((-1.5,1.50))
plt.show()


exit()

