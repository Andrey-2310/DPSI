from skimage.io import imread
from skimage import img_as_float, exposure
from skimage.filters.rank import minimum, maximum
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from d_converter import DConverter
from e_converter import EConverter


def show_image_hist(image):
    hist, bin_centers = exposure.histogram(image)
    plt.plot(bin_centers, hist, lw=2)
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.show()


def show_image(image):
    plt.imshow(image)
    plt.show()


def show_conversion_function(converter, basis):
    x_values = np.arange(0, 1 * basis, 1 / 255 * basis)
    plt.plot(x_values, converter.show_logic(x_values, basis), lw=2)
    plt.axis([0, 1 * basis, 0, 1.005 * basis])
    plt.show()


def initiate_d_conversion():
    d_converter = DConverter(int(input('Enter Gmin: ')), int(input('Enter Gmax: ')))
    common_conversion(d_converter)


def initiate_e_conversion():
    e_converter = EConverter(int(input('Enter Fmin: ')), int(input('Enter Fmax: ')))
    common_conversion(e_converter)


def common_conversion(converter):
    show_conversion_function(converter, 255)
    show_conversion_function(converter, 1)
    e_converted_image = converter.convert_image(img)
    show_image(e_converted_image)
    show_image_hist(e_converted_image)


def initiate_min_filtering():
    show_image(stars_img)
    show_image_hist(stars_img)
    min_star_image = ndimage.minimum_filter(stars_img, size=3)
    show_image(min_star_image)
    show_image_hist(min_star_image)


def initiate_max_filtering():
    max_star_image = ndimage.maximum_filter(stars_img, size=3)
    show_image(max_star_image)
    show_image_hist(max_star_image)


def initiate_min_max_filtering():
    mm_star_image = ndimage.maximum_filter(ndimage.minimum_filter(stars_img, size=3), size=3)
    show_image(mm_star_image)
    show_image_hist(mm_star_image)


def gamma_conversion():
    show_image(astronaut_img)
    gamma_img = exposure.adjust_gamma(astronaut_img, 0.5, 0.7)
    show_image(gamma_img)
    # show_image_hist(gamma_img)


action_map = {
    1: initiate_d_conversion,
    2: initiate_e_conversion,
    3: initiate_min_filtering,
    4: initiate_max_filtering,
    5: initiate_min_max_filtering,
    6: gamma_conversion
}


img = img_as_float(imread('tiger.jpg'))
stars_img = img_as_float(imread('stars.jpg'))
astronaut_img = img_as_float(imread('astronaut.jpg'))
show_image(img)
show_image_hist(img)

while True:
    action = int(input('1 - D-conversion\n2 - E-conversion\n3 - Min-filter\n'
                       '4 - Max-filter\n5 - MinMax-filter\n6 - Gamma-conversion\n'))
    action_map[action]()

