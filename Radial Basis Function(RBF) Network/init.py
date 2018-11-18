import numpy as np
import random as rnd


def map_to_interval(number, fr, to):
    return number * (to - fr) + fr


def get_number_from_range(a, b):
    return map_to_interval(rnd.random(), a, b)


def init_weights(width, height):
    arr = []
    for it in range(width * height):
        arr.append(get_number_from_range(-1, 1))
    return np.array(arr).reshape(width, height)


def init_threshold(size):
    return list(map(lambda x: map_to_interval(x, -1, 1), np.random.rand(1, size)))[0]


def get_y_vector(hot_spot, y_size):
    y_vector = np.zeros(y_size).astype(int)
    y_vector[hot_spot] = 1
    return y_vector