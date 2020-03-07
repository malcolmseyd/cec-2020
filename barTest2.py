# What we based plot3d() off of, from https://stackoverflow.com/questions/38086972/stacked-3d-bar-chart-with-matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")

ax.set_xlabel("x")
ax.set_ylabel("y") 
ax.set_zlabel("z")
ax.set_xlim3d(0,10)
ax.set_ylim3d(0,10) 
ax.set_zlim3d(0,10) 

alpha_base=0.5

xpos = [1,1,2,2,1,1,2,3] #x coordinates of each bar
ypos = [1,2,1,2,1,2,1,2] #y coordinates of each bar
zpos = [0,0,0,0,1,1,1,1] #z coordinates of each bar
colors = [(1, 0, 0, alpha_base), 'r', 'g', 'g', 'b','b','y','y']

dx = np.ones(8) #width of each bar
dy = np.ones(8) #depth of each bar
dz = np.ones(8) #height of each bar

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors)

plt.gca().invert_xaxis()
plt.show()