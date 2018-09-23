from numpy import clip


class EConverter:
    def __init__(self, f_min, f_max):
        self.f_min = f_min / 255
        self.f_max = f_max / 255

    def convert_image(self, image):
        return clip((1 / (self.f_max - self.f_min) * (image - self.f_min)), 0, 1)

    def show_logic(self, image, basis):
        return clip((1 / (self.f_max - self.f_min) * (image - self.f_min * basis)), 0, 1 * basis)
