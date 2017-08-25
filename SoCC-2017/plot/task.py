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

f = open('./task')

input_size = []
scache_map_exe = []
scache_map_write = []
spark_map_exe = []
spark_map_write = []
scache_reduce_exe = []
scache_reduce_read = []
spark_reduce_exe = []
spark_reduce_read = []

for line in f:
    args = line.split()
    if len(args) == 0:
        continue
    input_size.append(int(args[0]))
    spark_map_exe.append(float(args[1]))
    spark_map_write.append(float(args[2]))
    scache_map_exe.append(float(args[3]))
    scache_map_write.append(float(args[4]))
    spark_reduce_read.append(float(args[5]))
    spark_reduce_exe.append(float(args[6]))
    scache_reduce_read.append(float(args[7]))
    scache_reduce_exe.append(float(args[8]))

input_size = np.asarray(input_size)
scache_map_exe = np.asarray(scache_map_exe)
scache_map_write= np.asarray(scache_map_write)
spark_map_exe = np.asarray(spark_map_exe)
spark_map_write= np.asarray(spark_map_write)
scache_reduce_read = np.asarray(scache_reduce_read)
scache_reduce_exe= np.asarray(scache_reduce_exe)
spark_reduce_read = np.asarray(spark_reduce_read)
spark_reduce_exe = np.asarray(spark_reduce_exe)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
# plt.rc('hatch', linewidth=2)

fig, ax = plt.subplots()
width = 8

ax.barh(input_size, scache_map_exe, width, 
        linewidth=2, color='none', 
        edgecolor=orage, hatch="///",
        label='SCache Computing')
ax.barh(input_size, scache_map_write, width,
        left=scache_map_exe, 
        linewidth=2, color='none', 
        edgecolor=orage, hatch="---",
        label='SCache Shuffle Write')
ax.barh(input_size + width, spark_map_exe, width, 
        linewidth=2, color='none', 
        edgecolor=blue, hatch="+++", 
        label='Spark Computing')
ax.barh(input_size + width, spark_map_write, width, 
        left=spark_map_exe,
        linewidth=2, color='none', 
        edgecolor=blue, hatch="xxx", 
        label='Spark Shuffle Write')
ax.set_yticks(input_size + width)
ax.set_yticklabels(input_size)
# ax.legend(loc=4, fontsize=16, frameon=False)
ax.set_xlabel('Time (s)', fontsize=22)
ax.set_ylabel('Input Size (GB)', fontsize=22)
ax.set_aspect(0.4 / ax.get_data_ratio())
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
        loc=3, ncol=2, mode="expand", borderaxespad=0., 
        fontsize=16, frameon=False)

plt.savefig("groupbymaptask.pdf")
# size = fig.get_size_inches()
# print size
# 
# plt.show()

fig, ax = plt.subplots()
ax.barh(input_size, scache_reduce_read, width, 
        linewidth=2, color='none', 
        edgecolor=orage, hatch="///",
        label='SCache Shuffle Read')
ax.barh(input_size, scache_reduce_exe, width,
        left=scache_reduce_read, 
        linewidth=2, color='none', 
        edgecolor=orage, hatch="---",
        label='SCache Computing')
ax.barh(input_size + width, spark_reduce_read, width, 
        linewidth=2, color='none', 
        edgecolor=blue, hatch="+++", 
        label='Spark Shuffle Read')
ax.barh(input_size + width, spark_reduce_exe, width, 
        left=spark_reduce_read,
        linewidth=2, color='none', 
        edgecolor=blue, hatch="xxx", 
        label='Spark Computing')
ax.set_yticks(input_size + width)
ax.set_yticklabels(input_size)
# ax.legend(loc=4, fontsize=16, frameon=False)
ax.set_xlabel('Time (s)', fontsize=22)
ax.set_ylabel('Input Size (GB)', fontsize=22)

ax.set_aspect(0.4 / ax.get_data_ratio())
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
        loc=3, ncol=2, mode="expand", borderaxespad=0., 
        fontsize=16, frameon=False)
plt.savefig("groupbyreducetask.pdf")
# # plt.show()
