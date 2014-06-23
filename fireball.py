import sfml as sf
import sys
from res import Res
import physics
from spritesheet import SpriteSheet
from collideable import Collideable

class Fireball(sf.Drawable, Collideable):
    def __init__(self, x, y):
        Collideable.__init__(self, x, y, 24, 44, True)
        self._sprite = SpriteSheet(Res.blue_peewee)
        self._sprite.init(36, 6, 0.1)
        self._sprite.set_frame_loop(0, 5)
        self._sprite.position = sf.Vector2(x, y)
    
    def draw(self, target, render_states):
        target.draw(self._sprite, render_states)
    
    def update(self, dt):
        self._sprite.update(dt)

        # Update player sprite position
        self._sprite.position = self.position-sf.Vector2(23, 10)
        
    def on_collision_begin(self, other, side):
        if other.stationary:
            return False

    def on_collision_end(self, other):
        pass
