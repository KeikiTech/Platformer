import sfml as sf
from res import *
from spritesheet import *
from input_system import KeyHandler

class Player(sf.Drawable, KeyHandler):
    def __init__(self):
        self._sprite = SpriteSheet(Res.blue_peewee)
        self._sprite.init(36, 6, 0.1)
        self._sprite.set_frame_loop(12, 17)
        self._sprite.position = sf.Vector2(100, 100)
    
    def draw(self, target, render_states):
        target.draw(self._sprite, render_states)
    
    def update(self, dt):
        self._sprite.update(dt)