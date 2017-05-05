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

f = open('./tpcds')

input_size = []
spark = []
scache = []

for line in f:
    args = line.split()
    if len(args) == 0:
        continue
    input_size.append(args[0])
    spark.append(float(args[2]))
    scache.append(float(args[1]))

input_size = np.asarray(input_size)
scache = np.asarray(scache)
spark = np.asarray(spark)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)

# plt.rc('hatch', linewidth=2)

fig, ax = plt.subplots()
width = 8

xs = np.arange(len(input_size)) * 20

ax.bar(xs, scache, width, 
        linewidth=2, color='none', 
        edgecolor=orage, hatch="/////",
        label='Spark With SCache')
ax.bar(xs + width, spark, width, 
        linewidth=2, color='none', 
        edgecolor=blue, hatch="+++++", label='Spark')
ax.set_xticks(xs + width)
ax.set_xlim(right=(xs[-1] + 20))
ax.set_xticklabels(input_size, rotation=60)
# ax.legend(loc=4, fontsize=16, frameon=False)
ax.set_ylabel('Query Completion Time (s)', fontsize=24)
ax.set_aspect(0.23 / ax.get_data_ratio())
plt.legend(loc=2, fontsize=24, frameon=False)

# plt.savefig("tpcds.pdf")
# size = fig.get_size_inches()
# print size
# 
plt.show()


