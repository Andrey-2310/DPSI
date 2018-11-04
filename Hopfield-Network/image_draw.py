import matplotlib.pyplot as plt
import numpy as np


def configure_grid():
    ax = plt.gca()
    ax.set_xticks(np.arange(0, 10, 1))
    ax.set_yticks(np.arange(0, 10, 1))
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='green', linestyle='-', linewidth=2)


def show_image(image):
    plt.imshow(image, cmap='gray')
    configure_grid()
    plt.show()