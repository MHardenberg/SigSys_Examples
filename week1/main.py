import numpy as np
import helper as h

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


if __name__ == "__main__":
    points = [(-1., 0.), (0., 0.), (0., 1.), (1., 1.), (2., 0.), (3., 0.)]

    ts = np.linspace(-2, 3, 50)
    ys = h.interpolate_signal(ts, points)

    plt.stem(ts, ys, use_line_collection=True)
    plt.show()

    foo = lambda x: x + 1

    plt.stem(ts, h.transform_signal(ts, points, foo), use_line_collection=True)
    plt.show()
