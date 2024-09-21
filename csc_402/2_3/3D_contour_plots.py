import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-5.0, 5.0, 100)
ylist = np.linspace(-5.0, 5.0, 100)
X, Y = np.meshgrid(xlist, ylist)
#Z = 9 + X**2 + Y**2
Z = np.sin(X) + np.sin(Y)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(X,Y,Z)

plt.show()

##############
### IMAGE? ###
##############

xlist = np.linspace(-5.0, 5.0, 100)
ylist = np.linspace(-5.0, 5.0, 100)
X, Y = np.meshgrid(xlist, ylist)
#Z = 9 + X**2 + Y**2
Z = np.sin(X) + np.sin(Y)

fig,ax=plt.subplots(1,1)
cp = ax.contour(X, Y, Z)
#cp = ax.contourf(X, Y, Z) #'filled in' Contour Plot
fig.colorbar(cp)
ax.set_title('Contours Plot')

plt.show()

##############
### IMAGE? ###
##############