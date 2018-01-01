import matplotlib.pyplot as plt
import numpy as np

orage = '#FF8C00'
light_orange = '#FFA500'
blue = '#4682B4'
green = '#2E8B57'
light_blue = '#87CEFA'


def plot_coflow(f):
    fair = []
    sebf = []
    for line in f:
        args = line.split()
        if len(args) == 0:
            continue
        sebf.append(float(args[0]))
        fair.append(float(args[1]))

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize=18)
    plt.rc('ytick', labelsize=18)
    # plt.rc('hatch', linewidth=2)


    fig, ax = plt.subplots()
    xs = np.arange(len(fair)) + 1
    print(xs)
    print(fair)

    ax.plot(xs, fair,
            linewidth=3,
            color=blue,
            marker='o',
            markersize=10,
            mec='none',
            label='Per-flow Fairness')
    ax.plot(xs, sebf,
            linewidth=3,
            color=orage,
            marker="s",
            markersize=10,
            mec='none',
            label='SEBF with MADD')
    ax.legend(loc=4, fontsize=16, frameon=False)
    ax.set_ylabel('Avg. Coflow Completion Time (S)', fontsize=22)
    ax.set_xlabel('Number of Concurrent Shuffles', fontsize=22)
    ax.set_aspect(0.6 / ax.get_data_ratio())
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102),
               loc=3, ncol=2, mode="expand", borderaxespad=0.,
               fontsize=16, frameon=False)

    plt.savefig('coflow.pdf')
    # plt.show()


# f = open('./hash_pre')
# plot_hash(f)
# f = open('./range_pre')
# plot_range(f)
f = open('./coflow')
plot_coflow(f)