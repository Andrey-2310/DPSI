import numpy as np

import noise_generation
import hopfield
import image_draw

letters = ['E', 'O', 'Ш']

img_list = list(map(lambda x: np.array(np.matrix(np.loadtxt(f'images/teaching/{x}')).astype(int)).flatten(), letters))


# noise_generation.generate_noise_images(letters)
hopfield.teach_network(img_list)

while True:
    letter = input('\nChoose letter: ')
    noised_image = np.matrix(np.loadtxt(f'images/{letter}_img/{letter}_{input("Choose noise: ")}')).astype(int)
    image_draw.show_image(noised_image)
    image_draw.show_image(np.array(hopfield.reproduce(np.array(noised_image).flatten(), img_list, 100)).reshape(10, 10))

