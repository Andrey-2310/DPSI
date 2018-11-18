import numpy as np


def get_image_from_file(filename):
   return np.array(np.matrix(np.loadtxt(f'teaching/{filename}')).astype(int)).flatten()


def get_noised_image_from_file(filename, percentage):
   return np.array(np.matrix(np.loadtxt(f'noise/{filename}_img/{filename}_{percentage}')).astype(int)).flatten()
