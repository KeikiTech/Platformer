import sfml as sf
import sys
from res import Res
from spritesheet import SpriteSheet
from collideable import Collideable
from input_system import KeyHandler

class Player(sf.Drawable, Collideable, KeyHandler):
    def __init__(self, x, y):
        Collideable.__init__(self, x, y, 64, 64)
        self._sprite = SpriteSheet(Res.blue_peewee)
        self._sprite.init(36, 6, 0.1)
        self._sprite.set_frame_loop(0, 5)
        self._sprite.position = sf.Vector2(x, y)
        
        # Controls
        self._move_left = False
        self._move_right = False
        self._jump = False
        
        self._vertical_velocity = 0
    
    def draw(self, target, render_states):
        self._sprite.position = self.position
        target.draw(self._sprite, render_states)
    
    def update(self, dt):
        self._sprite.update(dt)
        
        if self._move_left:
            self.position.x -= 100*dt
        elif self._move_right:
            self.position.x += 100*dt
        
        if self._jump:
            self._vertical_velocity -= 0.1*dt
            self.position.y -= self._vertical_velocity
        else:
            self._vertical_velocity += 1*dt
            self.position.y += self._vertical_velocity

    
    def on_key_pressed(self, key_code):
        if key_code == sf.Keyboard.A and not self._move_right:
            self._move_left = True
            self._sprite.set_frame_loop(12, 17)
        elif key_code == sf.Keyboard.D and not self._move_left:
            self._move_right = True
            self._sprite.set_frame_loop(18, 23)
        elif key_code == sf.Keyboard.SPACE: # TODO I think we want on_key_down here
            self._jump = True
            self._vertical_velocity = -0.1
    
    def on_key_released(self, key_code):
        if key_code == sf.Keyboard.A:
            self._move_left = False
            self._sprite.set_frame_loop(0, 5)
        elif key_code == sf.Keyboard.D:
            self._move_right = False
            self._sprite.set_frame_loop(6, 11)
        elif key_code == sf.Keyboard.SPACE:
            self._jump = False
    
    def on_collision_begin(self, other):
        if other.stationary and self._vertical_velocity > 0:
            self._vertical_velocity = 0
        return True
    
    def on_collision_end(self, other):
        pass
