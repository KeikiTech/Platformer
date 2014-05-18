import sfml as sf

class Collideable:
    def __init__(self, x, y, width, height):
        self.position = sf.Vector2(x, y)
        self.width = width
        self.height = height