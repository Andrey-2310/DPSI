import math
from scipy.spatial import distance


def gauss_bell(x_vector, t_vector, std):
    return math.exp(-((distance.euclidean(x_vector, t_vector) / std) ** 2))


def calculate_cell_std(t_image, images):
    return min(list(map(lambda x: distance.euclidean(x, t_image), images)))
