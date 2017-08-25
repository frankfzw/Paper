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

f = open('./stage')

input_size = []
scache_map = []
spark_map = []
scache_reduce = []
spark_reduce = []

for line in f:
    args = line.split()
    if len(args) == 0:
        continue
    input_size.append(int(args[0]))
    scache_map.append(float(args[1]))
    spark_map.append(float(args[2]))
    scache_reduce.append(float(args[3]))
    spark_reduce.append(float(args[4]))

input_size = np.asarray(input_size)
scache_map = np.asarray(scache_map)
spark_map = np.asarray(spark_map)
scache_reduce = np.asarray(scache_reduce)
spark_reduce = np.asarray(spark_reduce)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)

# plt.rc('hatch', linewidth=2)

fig, ax = plt.subplots()
width = 8

ax.barh(input_size, scache_map, width, 
        linewidth=2, color='none', 
        edgecolor=orage, hatch="///",
        label='Spark With SCache')
ax.barh(input_size + width, spark_map, width, 
        linewidth=2, color='none', 
        edgecolor=blue, hatch="+++", label='Spark')
ax.set_yticks(input_size + width)
ax.set_yticklabels(input_size)
# ax.legend(loc=4, fontsize=16, frameon=False)
ax.set_xlabel('Map Stage Completion Time (s)', fontsize=22)
ax.set_ylabel('Input Size (GB)', fontsize=22)
ax.set_aspect(0.4 / ax.get_data_ratio())
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
        loc=3, ncol=2, mode="expand", borderaxespad=0., 
        fontsize=16, frameon=False)

plt.savefig("groupbymapstage.pdf")
# size = fig.get_size_inches()
# print size
# 
# plt.show()


fig, ax = plt.subplots()

ax.barh(input_size, scache_reduce, width, 
        linewidth=2, color='none', 
        edgecolor=orage, hatch="///",
        label='Spark With SCache')
ax.barh(input_size + width, spark_reduce, width, 
        linewidth=2, color='none', 
        edgecolor=blue, hatch="+++", label='Spark')
ax.set_yticks(input_size + width)
ax.set_yticklabels(input_size)
# ax.legend(loc=4, fontsize=16, frameon=False)
ax.set_xlabel('Reduce Stage Completion Time (s)', fontsize=22)
ax.set_ylabel('Input Size (GB)', fontsize=22)
ax.set_aspect(0.4 / ax.get_data_ratio())
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
        loc=3, ncol=2, mode="expand", borderaxespad=0., 
        fontsize=16, frameon=False)
plt.savefig("groupbyreducestage.pdf")
# plt.show()
