import numpy as np

import init
import image_service
import image_draw
import perceptron
import noise_generation


N = 36
H = 30
M = 5

ALPHA = 1
BETA = 1
D = 0.02

letter_map = {
    'K': 0,
    'L': 1,
    'O': 2,
    'T': 3,
    'U': 4
}

letter_image_map = {}
letter_vector_map = {}

for letter in letter_map:
    letter_image_map[letter] = image_service.get_image_from_file(letter)

for letter in letter_map:
    letter_vector_map[letter] = init.get_y_vector(letter_map[letter], 5)


inner_hidden_weights = init.init_weights(H, N)
hidden_threshold = init.init_threshold(H)
hidden_neurons = np.zeros(H)

hidden_outer_weights = init.init_weights(M, H)
outer_threshold = init.init_threshold(M)
outer_neurons = np.zeros(M)


def calculate_hidden_neuron_sum(index, image):
    return perceptron.sum_function(inner_hidden_weights[index],
                                   image, hidden_threshold[index])


def calculate_outer_neuron_sum(index):
    return perceptron.sum_function(hidden_outer_weights[index], hidden_neurons,
                                   outer_threshold[index])


def calculate_hidden_activations(image):
    for index in range(H):
        hidden_neurons[index] = perceptron.activation_function(calculate_hidden_neuron_sum(index, image))


def calculate_outer_activations():
    for index in range(M):
        outer_neurons[index] = perceptron.activation_function(calculate_outer_neuron_sum(index))


def get_image_activations(image):
    calculate_hidden_activations(image)
    calculate_outer_activations()


mistake_vector = [1, 1, 1, 1, 1]


def recalculate_hidden_outer_weights():
    for outer_index in range(M):
        for hidden_index in range(H):
            hidden_outer_weights[outer_index][hidden_index] += ALPHA * \
                                                               outer_neurons[outer_index] * \
                                                               (1 - outer_neurons[outer_index]) * \
                                                               mistake_vector[outer_index] * \
                                                               hidden_neurons[hidden_index]


def recalculate_outer_threshold():
    for outer_index in range(M):
        outer_threshold[outer_index] += ALPHA * \
                                        outer_neurons[outer_index] * \
                                        (1 - outer_neurons[outer_index]) * \
                                        mistake_vector[outer_index]


def calculate_error_for_hidden_weight(index):
    return sum(list(map(lambda i: mistake_vector[i] * outer_neurons[i] * \
                                  (1 - outer_neurons[i]) * hidden_outer_weights[i][index], range(M))))


def recalculate_inner_hidden_weights(letter):
    for hidden_index in range(H):
        for inner_index in range(N):
            inner_hidden_weights[hidden_index][inner_index] += BETA * \
                                                               hidden_neurons[hidden_index] * \
                                                               (1 - hidden_neurons[hidden_index]) * \
                                                               calculate_error_for_hidden_weight(hidden_index) * \
                                                               letter_image_map[letter][inner_index]


def recalculate_hidden_threshold():
    for hidden_index in range(H):
        hidden_threshold[hidden_index] += BETA * \
                                          hidden_neurons[hidden_index] * \
                                          (1 - hidden_neurons[hidden_index]) * \
                                          calculate_error_for_hidden_weight(hidden_index)


def back_propagation(letter):
    global mistake_vector
    mistake_vector = np.subtract(letter_vector_map[letter], outer_neurons)
    recalculate_hidden_outer_weights()
    recalculate_outer_threshold()
    recalculate_inner_hidden_weights(letter)
    recalculate_hidden_threshold()


# for letter in letter_map:
#     noise_generation.generate_noise_for_single_image(letter)

for letter in letter_image_map:
    image_draw.show_image(letter_image_map[letter])

while abs(np.amax(mistake_vector)) >= D:
    print(abs(np.amax(mistake_vector)))
    for letter in letter_map:
        get_image_activations(letter_image_map[letter])
        back_propagation(letter)

print(np.amax(mistake_vector), ' - Teaching finished')

while True:
    image = image_service.get_noised_image_from_file(input('\nLetter: '), int(input('Noise: ')))
    image_draw.show_image(image)
    get_image_activations(image)
    print(outer_neurons)



