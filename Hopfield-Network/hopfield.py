import numpy as np

weights = np.zeros((100, 100)).astype(int)


def write_weights_to_file(weights):
    with open('weights', 'w') as f:
        for item in weights:
            f.write("%s\n" % item)


def teach_network(img_array):
    calculate_weights(img_array)
    delete_self_feedback()
    write_weights_to_file(weights)


def calculate_weights(img_array):
    for img in img_array:
        for index, x in np.ndenumerate(weights):
            weights[index[0]][index[1]] += img[index[0]] * img[index[1]]


def delete_self_feedback():
    for diag_index in range(0, 100):
        weights[diag_index][diag_index] = 0


def check_match(image, img_list):
    return any(np.array_equal(image, img) for img in img_list)


def reproduce(noise_image, img_list, iter):
    return noise_image if not iter or check_match(noise_image, img_list) \
        else reproduce(reproduction(noise_image), img_list, iter - 1)


def reproduction(img):
    new_img = []
    for i in range(0, 100):
        coef = 0
        for j in range(0, 100):
            coef += weights[i][j] * img[j]
        new_img.append(1 if coef >= 0 else -1)
    return new_img
