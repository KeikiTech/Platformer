import sfml as sf
import sys
from res import Res
import physics
from spritesheet import SpriteSheet
from collideable import Collideable

class UFO(sf.Drawable, Collideable):
    def __init__(self, x, y, world):
        Collideable.__init__(self, x, y, 128, 64, True)
        self._sprite = SpriteSheet(Res.ufo)
        self._sprite.init(7, 7, 0.1)
        self._sprite.set_frame_loop(0, 5)
        self._sprite.position = sf.Vector2(x, y)
        self.world = world
        self.time = 3
        self.timer = 0
        self.shoot_time = 1
        self.shoot_timer = 0
        self.direction = 1
        
    def draw(self, target, render_states):
        target.draw(self._sprite, render_states)
    
    def update(self, dt):
        self._sprite.update(dt)
        
        self.timer += dt
        if self.timer >= self.time:
            # Switch directions
            self.direction *= -1
            # Reset the timer
            self.timer=0
        
        self.shoot_timer += dt
        if self.shoot_timer >= self.shoot_time:
            # Reset the timer
            self.shoot_timer=0
            self.world.create_fireball(self.position.x, self.position.y+70)

        self.position = self.position + sf.Vector2(75*dt, 0)*self.direction
            
        # Update player sprite position
        self._sprite.position = self.position
        
    def on_collision_begin(self, other, side):
        return False

    def on_collision_end(self, other):
        pass
