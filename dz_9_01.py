class Auto(object):
    def __init__(self, marka, color, engine_volume):
        self.marka = marka
        self.color = color
        self.engine_volume = engine_volume

    def move_forward (self):
        return "moving forward"

    def mone_back (self):
        return "moving back"

class Auto2 (Auto):
    def rotate_right (self):
        return "rotate right"

    def rotate_left (self):
        return "rotate left"