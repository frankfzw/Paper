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

f = open('./tera')

input_size = []
scache_reduce = []
spark_reduce = []

for line in f:
    args = line.split()
    if len(args) == 0:
        continue
    input_size.append(int(args[0]))
    spark_reduce.append(float(args[2]))
    scache_reduce.append(float(args[1]))

input_size = np.asarray(input_size)
xs = np.arange(len(input_size)) * 20
scache_reduce = np.asarray(scache_reduce)
spark_reduce = np.asarray(spark_reduce)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
# plt.rc('hatch', linewidth=2)


fig, ax = plt.subplots()
width = 8

ax.barh(xs, scache_reduce, width, 
        linewidth=2, color='none', 
        edgecolor=orage, hatch="/////",
        label='Spark With SCache')
ax.barh(xs + width, spark_reduce, width, 
        linewidth=2, color='none', 
        edgecolor=blue, hatch="+++++", label='Spark')
ax.set_yticks(xs + width)
ax.set_yticklabels(input_size)
# ax.legend(loc=4, fontsize=16, frameon=False)
ax.set_xlabel('Redcue Stage Completion Time (s)', fontsize=22)
ax.set_ylabel('Input Size (GB)', fontsize=22)
ax.set_aspect(0.4 / ax.get_data_ratio())
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
        loc=3, ncol=2, mode="expand", borderaxespad=0., 
        fontsize=16, frameon=False)
plt.savefig("tera.pdf")
f.close()

f = open('./tera_shuffle')

input_size = []
scache_shuffle = []
spark_shuffle = []

for line in f:
    args = line.split()
    if len(args) == 0:
        continue
    input_size.append(int(args[0]))
    spark_shuffle.append(float(args[1]))
    scache_shuffle.append(float(args[2]))
    
input_size = np.asarray(input_size)
xs = np.arange(len(input_size)) * 20
scache_shuffle = np.asarray(scache_shuffle)
spark_shuffle = np.asarray(spark_shuffle)
# plt.show()
fig, ax = plt.subplots()
width = 8

ax.barh(xs, scache_shuffle, width, 
        linewidth=2, color='none', 
        edgecolor=orage, hatch="/////",
        label='Spark With SCache')
ax.barh(xs + width, spark_shuffle, width, 
        linewidth=2, color='none', 
        edgecolor=blue, hatch="+++++", label='Spark')
ax.set_yticks(xs + width)
ax.set_yticklabels(input_size)
# ax.legend(loc=4, fontsize=16, frameon=False)
ax.set_xlabel('Shuffle through Network (GB)', fontsize=22)
ax.set_ylabel('Input Size (GB)', fontsize=22)
ax.set_aspect(0.4 / ax.get_data_ratio())
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
        loc=3, ncol=2, mode="expand", borderaxespad=0., 
        fontsize=16, frameon=False)
plt.savefig("tera_shuffle.pdf")
