import matplotlib.pyplot as plt
import numpy as np

orage = '#FF8C00'
light_orange = '#FFA500'
blue = '#4682B4'
green = '#2E8B57'
light_blue = '#87CEFA'


def plot_hash(f):
    reduce_dis = []
    observed_dis = []
    predict_dis = []
    for line in f:
        args = line.split()
        if len(args) == 0:
            continue
        reduce_dis.append(float(args[0]))
        observed_dis.append(float(args[2]))
        predict_dis.append(float(args[1]))
        
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize=18)
    plt.rc('ytick', labelsize=18)
    # plt.rc('hatch', linewidth=2)
    
    
    fig, ax = plt.subplots()
    width = 8
    xs = np.arange(len(reduce_dis)) * 20
    ax.bar(xs, reduce_dis, width, 
            linewidth=2, color='none', 
            edgecolor=orage, hatch="/////",
            label='Reduce Distribution')
    ax.bar(xs + width, observed_dis, width, 
            linewidth=2, color='none', 
            edgecolor=blue, hatch="+++++", label='Obeserved Distribution')
    ax.plot(xs + width, predict_dis, 
            linewidth=3,
            color=green, 
            marker='o',
            markersize=10,
            mec='none',
            label='Regression Prediction')
    ax.set_xticks(xs + width)
    ax.set_xticklabels(np.arange(len(reduce_dis)))
    # ax.legend(loc=4, fontsize=16, frameon=False)
    ax.set_ylabel('Normalized Size', fontsize=22)
    ax.set_aspect(0.6 / ax.get_data_ratio())
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
            loc=3, ncol=2, mode="expand", borderaxespad=0., 
            fontsize=16, frameon=False)

    plt.savefig('hash_pre.pdf')

def plot_err(f):
    regression = []
    sampling = []
    for line in f:
        args = line.split()
        if len(args) == 0:
            continue
        regression.append(float(args[0]))
        sampling.append(float(args[1]))
        
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize=18)
    plt.rc('ytick', labelsize=18)
    # plt.rc('hatch', linewidth=2)
    
    
    fig, ax = plt.subplots()
    xs = np.arange(len(regression))
    
    ax.plot(xs, regression, 
            linewidth=3,
            color=green, 
            marker='o',
            markersize=10,
            mec='none',
            label='Regression Prediction')
    ax.plot(xs, sampling, 
            linewidth=3,
            color='k', 
            ls='--',
            marker="D",
            markersize=10,
            mec='none',
            label='Sampling Prediction')
    # ax.legend(loc=4, fontsize=16, frameon=False)
    ax.set_xticks(xs)
    ax.set_xticklabels(xs)
    ax.set_ylabel('Relative Error', fontsize=22)
    ax.set_aspect(0.6 / ax.get_data_ratio())
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
            loc=3, ncol=2, mode="expand", borderaxespad=0., 
            fontsize=16, frameon=False)

    plt.savefig('prediction_relative_error.pdf')



def plot_range(f):
    reduce_dis = []
    observed_dis = []
    predict_dis = []
    range_dis = []
    for line in f:
        args = line.split()
        if len(args) == 0:
            continue
        reduce_dis.append(float(args[0]))
        observed_dis.append(float(args[2]))
        predict_dis.append(float(args[1]))
        range_dis.append(float(args[3]))
        
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize=18)
    plt.rc('ytick', labelsize=18)
    # plt.rc('hatch', linewidth=2)
    
    
    fig, ax = plt.subplots()
    width = 8
    xs = np.arange(len(reduce_dis)) * 20
    ax.bar(xs, reduce_dis, width, 
            linewidth=2, color='none', 
            edgecolor=orage, hatch="/////",
            label='Reduce Distribution')
    ax.bar(xs + width, observed_dis, width, 
            linewidth=2, color='none', 
            edgecolor=blue, hatch="+++++", label='Obeserved Distribution')
    ax.plot(xs + width, predict_dis, 
            linewidth=3,
            color=green, 
            marker='o',
            markersize=10,
            mec='none',
            label='Regression Prediction')
    ax.plot(xs + width, range_dis, 
            linewidth=3,
            color='k', 
            ls='--',
            marker="D",
            markersize=10,
            mec='none',
            label='Sampling Prediction')
    ax.set_xticks(xs + width)
    ax.set_xticklabels(np.arange(len(reduce_dis)))
    # ax.legend(loc=4, fontsize=16, frameon=False)
    ax.set_ylabel('Normalized Size', fontsize=22)
    ax.set_aspect(0.6 / ax.get_data_ratio())
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), 
            loc=3, ncol=2, mode="expand", borderaxespad=0., 
            fontsize=16, frameon=False)

    plt.savefig('range_pre.pdf')



f = open('./hash_pre')
plot_hash(f)
f = open('./range_pre')
plot_range(f)
f = open('./prediction_relative_error')
plot_err(f)
