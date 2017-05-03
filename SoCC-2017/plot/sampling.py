'''
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
'''

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np

orage = '#FF8C00'
light_orange = '#FFE4B5'
blue = '#4682B4'
green = '#2E8B57'

f = open('./sampling')

X = np.zeros((10, 6))
Y = np.zeros((10, 6))
Z = np.zeros((10, 6))

i = 0
j = 0
for line in f:
    args = line.split()
    X[i][j] = args[0]
    Y[i][j] = args[1]
    Z[i][j] = args[2]
    j += 1
    if j == 6:
        j = 0
        i += 1
verts = []
zs = []

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(0, 10):
    ax.plot(X[i], Y[i], Z[i], color=blue, ls='--', linewidth=2.0)

for i in range(0, 6):
    zs.append(Y[:, i][0])
    points = []
    points.append((X[:, i][0], 1.0))
    points = points + list(zip(X[:, i], Z[:, i]))
    points.append((X[:, i][-1], 1.0))
    verts.append(points)
    ax.plot(X[:, i], Y[:, i], Z[:, i], color=orage, ls='-', linewidth=2.0)

poly = PolyCollection(verts, facecolors=light_orange, linewidths=0)
poly.set_alpha(0.3)
ax.add_collection3d(poly, zs=zs, zdir='y')

ax.set_xlabel('Cluster Size', fontsize=16)
ax.set_ylabel('Size Per Node(GB)', fontsize=16)
ax.set_zlabel('Sampling Time(S)', fontsize=16)

plt.show()
