import sfml as sf
from res import Res
from collideable import Collideable

class Platform(sf.Drawable, Collideable):
    def __init__(self, x, y):
        Collideable.__init__(self, x, y, 242, 100, True)
        self._sprite = sf.Sprite(Res.big_platform)
        self._sprite.position = sf.Vector2(x, y)
    
    def draw(self, target, render_states):
        self._sprite.position = self.position-sf.Vector2(0, 24)
        target.draw(self._sprite, render_states)