import numpy as np


def weird_car(xs):
    out = np.zeros(xs.shape)
    out[(xs >= 0) & (xs < 1)] = 1
    out[(xs >= 1) & (xs < 2)] = 2 - xs[(xs >= 1) & (xs < 2)]
    return out


def relu(xs):
    return np.maximum(0, xs)


def impulse(xs):
    out = np.zeros(xs.shape)
    out[(xs >= 0) & (xs < 1)] = 1
    return out

def bell(xs, mu=0, sig=.5):
    return 1. / (np.sqrt(2. * np.pi) * sig) * np.exp(-np.power((xs - mu) / sig, 2.) / 2)