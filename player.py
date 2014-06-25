import sfml as sf
import sys
from res import Res
import physics
from spritesheet import SpriteSheet
from collideable import Collideable
from input_system import KeyHandler

DIR_LEFT = 0
DIR_RIGHT = 1

# TUTORIAL 2:
# Change the following value from 400 to 500
PLAYER_JUMP_VELOCITY = 500
PLAYER_MOVE_SPEED = 200

class Player(sf.Drawable, Collideable, KeyHandler):
    def __init__(self, x, y):
        Collideable.__init__(self, x, y, 24, 44)
        self._sprite = SpriteSheet(Res.blue_peewee)
        self._sprite.init(36, 6, 0.1)
        self._sprite.set_frame_loop(0, 5)
        self._sprite.position = sf.Vector2(x, y)
        self.current_checkpoint = sf.Vector2(x, y)
        
        # Controls
        self._move_left = False
        self._move_right = False
        self._on_ground = False

        # Direction -- for animating stuff
        self._direction = DIR_RIGHT
        
        self._vertical_velocity = 0
    
    def draw(self, target, render_states):
        target.draw(self._sprite, render_states)
    
    def update(self, dt):
        self._sprite.update(dt)

        ### TUTORIAL 1:
        # Uncomment the following 4 lines
        if self._move_left:
            self.position.x -= PLAYER_MOVE_SPEED*dt
        elif self._move_right:
            self.position.x += PLAYER_MOVE_SPEED*dt
        
        # Apply Vertical velocity
        self.position.y += self._vertical_velocity*dt

        if not self._on_ground:
            # Apply gravity
            self._vertical_velocity += 1000*dt

            # Animations when player is off ground
            if self._vertical_velocity <= 0: # Going up
                if self._direction == DIR_LEFT:
                    self._sprite.set_frame_loop(33, 33)
                elif self._direction == DIR_RIGHT:
                    self._sprite.set_frame_loop(30, 30)
            elif self._vertical_velocity > 0: # Going down
                if self._direction == DIR_LEFT:
                    self._sprite.set_frame_loop(33, 35, False)
                elif self._direction == DIR_RIGHT:
                    self._sprite.set_frame_loop(30, 32, False)
        else: # On ground
            if self._move_left:
                self._sprite.set_frame_loop(12, 17)
            elif self._move_right:
                self._sprite.set_frame_loop(18, 23)
            else: # Not moving
                if self._direction == DIR_LEFT:
                    self._sprite.set_frame_loop(1, 1)
                elif self._direction == DIR_RIGHT:
                    self._sprite.set_frame_loop(6, 6)

        # Update player sprite position
        self._sprite.position = self.position-sf.Vector2(23, 10)
    
    def on_key_pressed(self, key_code):
        if key_code == sf.Keyboard.A and not self._move_right:
            self._move_left = True
            self._direction = DIR_LEFT
        elif key_code == sf.Keyboard.D and not self._move_left:
            self._move_right = True
            self._direction = DIR_RIGHT
        elif key_code == sf.Keyboard.SPACE and self._on_ground:
            self._vertical_velocity = -PLAYER_JUMP_VELOCITY
    
    def on_key_released(self, key_code):
        if key_code == sf.Keyboard.A:
            self._move_left = False
        elif key_code == sf.Keyboard.D:
            self._move_right = False
    
    def on_collision_begin(self, other, side):
        if other.stationary and side == physics.side_down and self._vertical_velocity > 0:
            self._vertical_velocity = 0
            self._on_ground = True
        return True
    
    def on_collision_end(self, other):
        self._on_ground = False
