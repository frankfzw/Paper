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
light_green = '#CCFFCC'

# f = open('./util')
f = open('./scache_util')

net = []
cpu = []
disk = []

for line in f:
    args = line.split()
    if len(args) == 0:
        continue
    cpu.append(float(args[0]))
    disk.append(float(args[1]))
    net.append(float(args[2]))

cpu = np.asarray(cpu)
net = np.asarray(net)
disk = np.asarray(disk)

net = net / 1024
disk = disk / 1024

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)

# plt.rc('hatch', linewidth=2)

fig, ax = plt.subplots(figsize=(12,4))
width = 8

xs = np.arange(len(cpu))

line_cpu = ax.plot(xs, cpu, 
            linewidth=3,
            color=blue, 
            label='CPU Utilization')
# ax.set_xticks(xs + width)
# plot exe bar util
# exe_x = 10
# exe_width = 18
# s_write_x = 24
# s_write_width = 15
# s_read_x = 40
# s_read_width = 43

# plot exe bar scache
exe_x = 8
exe_width = 11
s_write_x = 17.5
s_write_width = 3.5
s_read_x = 21
s_read_width = 6

ax.bar(left=[exe_x,s_write_x,s_read_x], height=[1.1,1.1,1.1], width=[exe_width,s_write_width,s_read_width],
        linewidth=0, color=[light_blue, light_orange, light_green],
        alpha=0.2)

ax.set_xticklabels([])
ax.set_ylabel('CPU Utilization \%', fontsize=18)
ax.set_ylim(0, 1.1)
# ax.set_xlim(right=(xs[-1] + 20))
# ax.legend(loc=4, fontsize=16, frameon=False)
# ax.set_ylabel('CPU Utilization \%', fontsize=16)
# ax.set_aspect(0.3 / ax.get_data_ratio())
# plot net and disk
ax2 = ax.twinx()
ax2.set_ylim(0, 400)
line_disk = ax2.plot(xs, disk, 
            linewidth=3,
            ls=':',
            color=orage, 
            label='Disk Write')
line_net = ax2.plot(xs, net, 
            linewidth=3,
            ls='--',
            color=green,
            label='Network TX')
ax2.set_ylabel('Throughput (MB/s)', fontsize=18)

ax.annotate(s='', xy=(exe_x,0.2), xytext=((exe_x+exe_width),0.2), arrowprops=dict(arrowstyle='<->'))
ax.text(exe_x+2, 0.22, 'Execution', fontsize=20)

# plot util text
# ax.annotate(s='', xy=(s_write_x,0.75), xytext=((s_write_x+s_write_width),0.75), arrowprops=dict(arrowstyle='<->'))
# ax.text(s_write_x, 0.77, 'Shuffle Write', fontsize=16)
# ax.annotate(s='', xy=(s_read_x,0.96), xytext=((s_read_x+s_read_width),0.96), arrowprops=dict(arrowstyle='<->'))
# ax.text(s_read_x + 5, 0.98, 'Shuffle Read and Execution', fontsize=16)

# plot scache text
ax.annotate(s='', xy=(s_write_x,0.5), xytext=((s_write_x+s_write_width),0.5), arrowprops=dict(arrowstyle='<->'))
ax.text(s_write_x-0.5, 0.52, 'Shuffle Write', fontsize=16)
ax.annotate(s='', xy=(s_read_x,0.98), xytext=((s_read_x+s_read_width),0.98), arrowprops=dict(arrowstyle='<->'))
ax.text(s_read_x, 1, 'Reduce Execution', fontsize=16)
# ax2.set_aspect((350 / 1.1) * 0.3 / ax2.get_data_ratio())
# plt.legend(loc=1, fontsize=18, frameon=False)
lines = line_cpu + line_net + line_disk
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc=1, fontsize=18, 
        bbox_to_anchor=(0., 1.02, 1., .102), 
        ncol=3, mode="expand", borderaxespad=0., 
        frameon=False)


# plt.savefig("util.pdf")
plt.savefig("scache_util.pdf")
# size = fig.get_size_inches()
# print size
# 
# plt.show()


