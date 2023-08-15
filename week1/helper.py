import numpy as np
import matplotlib.pyplot as plt


def plot_transforms(ts, ys, transforms_dict):
    """ Takes original set of times: ts and signal: ys and plots them,
    with the entries of transformed signals: ys_i in transforms_dict."""
    
    num_figs = len(transforms_dict) +1
    fig, axes = plt.subplots(num_figs, figsize=(18, 4*num_figs))
    fig.subplots_adjust(hspace=0.)
    
    # plot original
    axes[0].plot(ts, ys, label='Original signal')
    
    # plot entries in dict
    for i, key in enumerate(transforms_dict):
        axes[i+1].plot(ts, ys, label='Original signal', alpha=.3)
        axes[i+1].plot(ts, transforms_dict[key], label=key)

    # draw legends and grids
    for ax in axes:
        ax.grid(True, alpha=.2)
        ax.legend()
    plt.show()