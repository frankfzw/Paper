import matplotlib.pyplot as plt
import numpy as np

orage = '#FF8C00'
light_orange = '#FFA500'
blue = '#4682B4'
green = '#2E8B57'
light_blue = '#87CEFA'


def plot_sim(f):
    random = []
    fifo = []
    heap = []
    for line in f:
        args = line.split()
        if len(args) == 0:
            continue
        random.append(float(args[0]))
        fifo.append(float(args[1]))
        heap.append(float(args[2]))
        
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize=18)
    plt.rc('ytick', labelsize=18)
    # plt.rc('hatch', linewidth=2)

    
    fig, ax = plt.subplots()
    xs = np.arange(len(random)) + 1
    ys = np.zeros(len(random))
    print xs
    print random
    
    ax.plot(xs, random, 
            linewidth=3,
            color=blue, 
            marker='o',
            markersize=10,
            mec='none',
            label='Random Mapping')
    ax.plot(xs, fifo, 
            linewidth=3,
            color=orage, 
            marker="s",
            markersize=10,
            mec='none',
            label='Spark')
    ax.plot(xs, heap, 
            linewidth=3,
            color=green, 
            marker="^",
            markersize=10,
            mec='none',
            label='Heuristic MinHeap')
    ax.plot(xs, ys, linewidth=3, color='r', ls='--')
    ax.legend(loc=4, fontsize=16, frameon=False)
    # ax.set_xticklabels(['1','','2','','3','','4','','5','','6','','7','','8','','9','','10',''])
    ax.set_ylabel('Avg. Improvement \%', fontsize=22)
    ax.set_xlabel('Round', fontsize=22)
    ax.set_aspect(0.6 / ax.get_data_ratio())
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
            loc=3, ncol=2, mode="expand", borderaxespad=0., 
            fontsize=18, frameon=False)

    plt.savefig('sim.pdf')
    # plt.show()





# f = open('./hash_pre')
# plot_hash(f)
# f = open('./range_pre')
# plot_range(f)
f = open('./sim')
plot_sim(f)
