import sfml as sf

from input_system import KeyHandler, MouseHandler
from world import World

class WorldEditor(KeyHandler, MouseHandler):
    def __init__(self, view, world):
        self.view = view
        self.world = world
        self.place_type = 0

    def on_key_pressed(self, key_code):
        if key_code == sf.Keyboard.NUM1:
            self.place_type = 0
        elif key_code == sf.Keyboard.NUM2:
            self.place_type = 1
        elif key_code == sf.Keyboard.NUM3:
            self.place_type = 2
        elif key_code == sf.Keyboard.NUM4:
            self.place_type = 3
        elif key_code == sf.Keyboard.NUM5:
            self.place_type = 4
        elif key_code == sf.Keyboard.NUM6:
            self.place_type = 5
    
    def on_mouse_button_pressed(self, button, position):
        if button == sf.Mouse.LEFT:
            ppos = position+(self.view.center-(self.view.size/2))
            if self.place_type == 0:
                self.world.create_big_platform(ppos.x, ppos.y)
            elif self.place_type == 1:
                self.world.create_small_platform(ppos.x, ppos.y)
            elif self.place_type == 2:
                self.world.create_small_hmoving_platform(ppos.x, ppos.y)
            elif self.place_type == 3:
                self.world.create_small_vmoving_platform(ppos.x, ppos.y)
            elif self.place_type == 4:
                self.world.create_fireball(ppos.x, ppos.y)
            elif self.place_type == 5:
                self.world.create_ufo(ppos.x, ppos.y)
    
    def on_mouse_moved(self, position, move):
        pass
