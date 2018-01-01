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

# f = open('./cdf')
f = open('./coflow_cdf')
x_label = 'Coflow Completion Time (S)'

x = []
y = []


for line in f:
    args = line.split()
    if len(args) == 0:
        continue
    x.append(float(args[0]))
    y.append(float(args[1]))


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)
# plt.rc('hatch', linewidth=2)

# fig, ax = plt.subplots(figsize=(6.5,6.5))
fig, ax = plt.subplots(figsize=(18, 6))
width = 9.5

xy = {}
for i in x:
    if i in xy:
        xy[i] += 1
    else:
        xy[i] = 1

xx = list(xy.keys())
yy = [i / len(x) for i in list(xy.values())]
xx = np.asarray(xx)
yy = np.asarray(yy)
ax.set_xlim(0, 50)
ax.plot(xx, yy, linewidth=3, color=blue)
avg = sum(x) / len(x)
# ax.plot(avg, y, linewidth=3, color=blue)

# ax.legend(loc=4, fontsize=16, frameon=False)
ax.set_xlabel(x_label, fontsize=22)
ax.set_ylabel('CDF', fontsize=22)
# ax.set_aspect(1. / ax.get_data_ratio())
ax.grid(True)
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102),
#         loc=3, ncol=2, mode="expand", borderaxespad=0.,
#         fontsize=16, frameon=False)
# plt.savefig("reduce_cdf.pdf")
# plt.savefig("coflow_cdf.pdf")
plt.show()
# size = fig.get_size_inches()
# print size
#
# plt.show()