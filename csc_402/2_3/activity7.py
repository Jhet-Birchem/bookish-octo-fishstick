import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-5.0, 5.0, 100)
ylist = np.linspace(-5.0, 5.0, 100)
X, Y = np.meshgrid(xlist, ylist)
#Z = np.sin(X*Y) #Function 1
#Z = np.exp(X)*np.sin(Y) #Function 2
#Z = np.sin(X - Y) #Function 3
#Z = np.sin(X) - np.sin(Y) #Function 4
#Z = (1-X**2)*(1-Y**2) #Function 5
Z = (X -Y)/(1 + X**2 + Y**2) #Function 6


fig,ax=plt.subplots(1,1)
cp = ax.contour(X, Y, Z)
#cp = ax.contourf(X, Y, Z) #'filled in' Contour Plot
fig.colorbar(cp)
ax.set_title('Contours Plot')

plt.show()

##############
### IMAGE? ###
##############

xlist = np.linspace(-5.0, 5.0, 50)
ylist = np.linspace(-5.0, 5.0, 50)
X, Y = np.meshgrid(xlist, ylist)
#Z = np.sin(X*Y) #Function 1
#Z = np.exp(X)*np.sin(Y) #Function 2
#Z = np.sin(X - Y) #Function 3
#Z = np.sin(X) - np.sin(Y) #Function 4
#Z = (1-X**2)*(1-Y**2) #Function 5
Z = (X -Y)/(1 + X**2 + Y**2) #Function 6


fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(X,Y,Z)

plt.show()

##############
### IMAGE? ###
##############

