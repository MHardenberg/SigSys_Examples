import numpy as np


def interpolate(x, A, B):
    """ This functions takes two points A, B and assumes a straightline 
    between them. It then returns the y value of some point (x, y) between A,B,
    by scaling the total y distance by the ratio of partial and total x
    distance."""

    ax, ay = A
    bx, by = B

    #assert ax <= x <= bx, ValueError('x outside defined range.')

    total_x_dist = bx - ax
    partial_x_dist = x - ax
    
    total_y_dist = by - ay

    interpolated_y = ay + total_y_dist * partial_x_dist / total_x_dist
    return interpolated_y


def interpolate_signal(xs, points_list):
    """ Given an arry of sample times and a list of point tuples as points,
    this function returns linearly interpolated sample values between defined
    points as an arrat. """
    
    points = points_list.copy()
    last_point_x, last_point_y = xs[0], 0
    next_point_x, next_point_y = points.pop(0) 
    ys = np.zeros(len(xs))

    for i, x in enumerate(xs):
        if x >= next_point_x:
            last_point_x, last_point_y = next_point_x, next_point_y
            
            if points:
                next_point_x, next_point_y = points.pop(0)
            else:
                next_point_x, next_point_y = xs[-1], 0
        ys[i] = interpolate(x, (last_point_x, last_point_y),
                            (next_point_x, next_point_y))
    return ys


def transform_signal(xs, points, fun):
    zs = fun(xs)
    return interpolate_signal(zs, points)


