import sfml as sf
import sys
from res import Res
import physics
from spritesheet import SpriteSheet
from collideable import Collideable

FIREBALL_MOVE_SPEED = 400

class Fireball(sf.Drawable, Collideable):
    def __init__(self, x, y, world):
        Collideable.__init__(self, x, y, 100, 100, False)
        self._sprite = SpriteSheet(Res.fireball)
        self._sprite.init(10, 10, 0.1)
        self._sprite.position = sf.Vector2(x, y)
        self.world = world
        self.dead = False
        
    def draw(self, target, render_states):
        target.draw(self._sprite, render_states)
    
    def update(self, dt):
        self._sprite.update(dt)
        
        self.position.y += FIREBALL_MOVE_SPEED*dt 

        # Update player sprite position
        self._sprite.position = self.position
        
    def on_collision_begin(self, other, side):
        if self.dead:
            return False
        self.world.create_explosion(self.position.x, self.position.y)
        self.dead = True
        if hasattr(other, "health"):
            other.health -= 1
        return False
    
    def on_collision_end(self, other):
        pass
