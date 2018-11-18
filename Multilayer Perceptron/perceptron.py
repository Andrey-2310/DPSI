import math
import numpy as np

def sum_function(weights, x_vector, threshold):
    return sum(np.multiply(weights, x_vector)) + threshold


def activation_function(sum):
    return 1 / (1 + math.exp(-sum))