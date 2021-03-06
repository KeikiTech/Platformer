import sfml as sf

class Collideable:
    def __init__(self, x, y, width, height, stationary=False):
        self.position = sf.Vector2(x, y)
        self.width = width
        self.height = height
        self.stationary = stationary
        self.colliding = set() # Currently colliding objects
    
    def on_collision_begin(self, other, side):
        return True
    
    def on_collision_end(self, other):
        pass
