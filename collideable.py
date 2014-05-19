import sfml as sf

class Collideable:
    def __init__(self, x, y, width, height, stationary=False):
        self.position = sf.Vector2(x, y)
        self.width = width
        self.height = height
        self.stationary = stationary
    
    def on_collision_begin(self, other):
        return True
    
    def on_collision_end(self, other):
        pass