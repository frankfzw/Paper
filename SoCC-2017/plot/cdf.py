"""
====================
Horizontal bar chart
====================

This example showcases a simple horizontal bar chart.
"""
import matplotlib.pyplot as plt
import numpy as np

orage = '#FF8C00'
light_orange = '#FFA500'
blue = '#4682B4'
green = '#2E8B57'
light_blue = '#87CEFA'

f = open('./cdf')

x = []
y = []


for line in f:
    args = line.split()
    if len(args) == 0:
        continue
    x.append(float(args[0]))
    y.append(float(args[1]))

x = np.asarray(x)
y = np.asarray(y)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
# plt.rc('hatch', linewidth=2)

fig, ax = plt.subplots()
width = 9.5

ax.plot(x, y, linewidth=3, color=blue)

# ax.legend(loc=4, fontsize=16, frameon=False)
ax.set_xlabel('Shuffle Time Fraction', fontsize=16)
ax.set_ylabel('CDF', fontsize=16)
ax.set_aspect(1. / ax.get_data_ratio())
ax.grid(True)
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
#         loc=3, ncol=2, mode="expand", borderaxespad=0., 
#         fontsize=16, frameon=False)
plt.savefig("reduce_cdf.pdf")
# size = fig.get_size_inches()
# print size
# 
# plt.show()


