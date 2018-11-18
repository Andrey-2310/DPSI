from PIL import Image
import pytesseract
import cv2
import os
import matplotlib.pyplot as plt
from skimage import img_as_float
from skimage.io import imread, imsave
from skimage.filters import threshold_isodata, threshold_otsu,threshold_mean, threshold_triangle, threshold_li, threshold_yen, try_all_threshold, rank
from skimage.filters import threshold_local
from skimage.color import rgb2grey


def show_image(image):
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.show()


def find_text(image):
    filename = "{}.png".format(os.getpid())
    imsave(filename, image)

    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)


def global_thresholding(image_name, border):
    image = rgb2grey(img_as_float(imread(image_name))*255)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x][y] = 0 if image[x][y] < border else 1
    return image


def local_thresholding(image_name, block_size):
    image = rgb2grey(img_as_float(imread(image_name))*255)
    local_thresh = threshold_local(image, block_size, offset=10)
    return image > local_thresh


def show_locally_thresholded_image():
    show_image(local_thresholding(input('Path: '), int(input('Amount of neighbours: '))))


def get_text_from_locally_thresholded_image():
    find_text(local_thresholding(input('Path: '), int(input('Amount of neighbours: '))))


def show_globally_thresholded_image():
    show_image(global_thresholding(input('Path: '), int(input('Border: '))))


def get_text_from_globally_thresholded_image():
    find_text(global_thresholding(input('Path: '), int(input('Border: '))))


# image = 'alice_images/alice_page_3.jpg'
image = 'images/img7.png'


action_map = {
    1: show_locally_thresholded_image,
    2: get_text_from_locally_thresholded_image,
    3: show_globally_thresholded_image,
    4: get_text_from_globally_thresholded_image,
}

while True:
    action = int(input('1 - Show Image with Local Thresholding\n'
                       '2 - Get text from Image with Local Thresholding\n'
                       '3 - Show Image with Global Thresholding\n'
                       '4 - Get text from Image with Global Thresholding\n'))
    action_map[action]()




