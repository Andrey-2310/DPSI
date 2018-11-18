import numpy as np

import init
import image_service
import image_draw
import rbf_cell
import noise_generation


N = 36
H = 5
M = 5

ALPHA = 1
D = 0.02

letter_map = {
    'K': 0,
    'L': 1,
    'O': 2,
    'T': 3,
    'U': 4
}

image_list = []
letter_vector_map = {}

for letter in letter_map:
    image_list.append(image_service.get_image_from_file(letter))

for letter in letter_map:
    letter_vector_map[letter] = init.get_y_vector(letter_map[letter], M)


hidden_values = np.zeros(H)
hidden_cells_std = np.zeros(H)

hidden_outer_weights = init.init_weights(M, H)
outer_neurons = np.zeros(M)


for iter in range(image_list.__len__()):
    hidden_cells_std[iter] = rbf_cell.calculate_cell_std(image_list[iter], image_list[:iter] + image_list[iter+1:])


def calculate_outer_sum(index):
    return sum(np.multiply(hidden_outer_weights[index], hidden_values))


def calculate_hidden_values(image):
    for index in range(H):
        hidden_values[index] = rbf_cell.gauss_bell(image, image_list[index], hidden_cells_std[index])


def calculate_outer_activations():
    for index in range(M):
        outer_neurons[index] = calculate_outer_sum(index)


def get_image_activations(image):
    calculate_hidden_values(image)
    calculate_outer_activations()


mistake_vector = [1, 1, 1, 1, 1]


def recalculate_hidden_outer_weights():
    for outer_index in range(M):
        for hidden_index in range(H):
            hidden_outer_weights[outer_index][hidden_index] += ALPHA * \
                                                               mistake_vector[outer_index] * \
                                                               hidden_values[hidden_index]


def calculate_error_for_hidden_weight(index):
    return sum(list(map(lambda i: mistake_vector[i] * outer_neurons[i] * \
                                  (1 - outer_neurons[i]) * hidden_outer_weights[i][index], range(M))))


def teach_network(letter):
    global mistake_vector
    mistake_vector = np.subtract(letter_vector_map[letter], outer_neurons)
    recalculate_hidden_outer_weights()


# for letter in letter_map:
#     noise_generation.generate_noise_for_single_image(letter)

for image in image_list:
    image_draw.show_image(image)

while abs(np.amax(mistake_vector)) >= D:
    print(abs(np.amax(mistake_vector)))
    for letter in letter_map:
        get_image_activations(image_list[letter_map[letter]])
        teach_network(letter)

print(np.amax(mistake_vector), ' - Teaching finished')

while True:
    image = image_service.get_noised_image_from_file(input('\nLetter: '), int(input('Noise: ')))
    image_draw.show_image(image)
    get_image_activations(image)
    print(outer_neurons)



