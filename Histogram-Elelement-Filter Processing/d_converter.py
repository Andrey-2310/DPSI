class DConverter:
    def __init__(self, g_min, g_max):
        self.g_min = g_min / 255
        self.g_max = g_max / 255

    def convert_image(self, source):
        return (self.g_max - self.g_min) * source + self.g_min

    def show_logic(self, source, basis):
        return (self.g_max - self.g_min) * source + self.g_min * basis

