from skimage import img_as_float, exposure
from skimage.io import imread, imsave
from skimage.filters import threshold_isodata, try_all_threshold, rank
from skimage.morphology import disk
from skimage.color import rgb2grey, grey2rgb
from skimage.measure import regionprops

import matplotlib.pyplot as plt
import scipy.ndimage as ndimage

from sklearn.cluster import KMeans

import numpy as np


def image_to_binary(image):
    th_image = threshold_isodata(image)
    return image > th_image


def show_image_hist(image):
    hist, bin_centers = exposure.histogram(image)
    plt.plot(bin_centers, hist, lw=2)
    plt.show()


def show_image(image):
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.show()


def print_stat(header, array):
    print(header)
    for x in array:
        print(x)


def calculate_elongation(bbox):
    width = bbox[3] - bbox[1]
    height = bbox[2] - bbox[0]
    return max([width / height, height / width])


color_map = {
    0: 50,
    1: 100,
    2: 150,
    3: 200,
    4: 250
}


def change_colours_for_clusters(labeled_img, k_means_labels, amount_of_objects):
    for i_object in range(1, amount_of_objects + 1):
        np.place(labeled_img, labeled_img == i_object, color_map[k_means_labels[i_object - 1]])


img = img_as_float(imread('P0001460.jpg'))
binary_img = rank.maximum(rank.minimum(image_to_binary(rgb2grey(img)), selem=disk(2)), selem=disk(2))

show_image(img)
show_image(binary_img)


labeled_array, num_features = ndimage.label(binary_img)


properties = regionprops(labeled_array, coordinates='xy')

k_means_list = list(map(lambda x: [
    x.area,
    x.perimeter,
    x.perimeter ** 2 / x.area,
    calculate_elongation(x.bbox),
    x.orientation,
    x.extent
], properties))
# print(k_means_list)


kmeans = KMeans(n_clusters=2, random_state=0).fit(np.array(k_means_list))

print(kmeans.labels_)

change_colours_for_clusters(labeled_array, kmeans.labels_, num_features)

# print(a)



# for x in properties:
    # print(x.area, x.perimeter, x.perimeter ** 2 / x.area)
    # print(x.bbox, x.orientation)
# show_image(binary_img)


show_image(labeled_array)


print(num_features)
# imsave('grey-scale', binary_img)
