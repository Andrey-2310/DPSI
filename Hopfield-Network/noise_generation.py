import random
import numpy as np

all_noise_percentage = [10, 20, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100]


def generate_noise_images(letters):
    for letter in letters:
        generate_noise_for_single_image(letter)


def generate_noise_for_single_image(letter):
    for percentage in all_noise_percentage:
        noise_image(np.array(np.loadtxt(f'images/teaching/{letter}')).astype(int), percentage, letter)


def noise_image(img, noise_percentage, letter):
    for coord in get_pixels_according_to_percentage(noise_percentage):
        img[coord[0]][coord[1]] *= -1
    save_noised_image(img, noise_percentage, letter)


def get_pixels_according_to_percentage(noise_percentage):
    pixel_set = set()
    while len(pixel_set) < noise_percentage:
        pixel_set.add((random.randint(0, 9), random.randint(0, 9)))
    return pixel_set


def save_noised_image(image, percentage, letter):
    address = f'images/{letter}_img/{letter}_{percentage}'
    with open(address, 'x') as f:
        for row in image:
            for item in row:
                f.write('%s ' % item)
            f.write('\n')

