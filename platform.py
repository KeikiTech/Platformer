import sfml as sf
from res import Res
import physics
from collideable import Collideable

class Platform:
    def update(self, dt):
        pass

class BigPlatform(sf.Drawable, Platform, Collideable):
    def __init__(self, x, y):
        Collideable.__init__(self, x, y, 242, 110, True)
        self._sprite = sf.Sprite(Res.big_platform)
        self._sprite.position = sf.Vector2(x, y)
    
    def draw(self, target, render_states):
        self._sprite.position = self.position-sf.Vector2(0, 14)
        target.draw(self._sprite, render_states)
        
class SmallPlatform(sf.Drawable, Platform, Collideable):
    def __init__(self, x, y):
        Collideable.__init__(self, x, y, 45, 30, True)
        self._sprite = sf.Sprite(Res.small_platform)
        self._sprite.position = sf.Vector2(x, y)
    
    def draw(self, target, render_states):
        self._sprite.position = self.position-sf.Vector2(3, 7)
        target.draw(self._sprite, render_states)
		
class AcidPlatform(sf.Drawable, Platform, Collideable):
    def __init__(self, x, y):
        Collideable.__init__(self, x, y, 242, 110, True)
        self.deadly = False
        self._sprite = sf.Sprite(Res.acid_platform)
        self._sprite.position = sf.Vector2(x, y)
    
    def draw(self, target, render_states):
        self._sprite.position = self.position-sf.Vector2(0, 14)
        target.draw(self._sprite, render_states)

    def on_collision_begin(self, other, side):
        if hasattr(other, "health"):
            other.health -= 1
        return False
		
class SmallHMovingPlatform(sf.Drawable, Platform, Collideable):
    def __init__(self, x, y):
        Collideable.__init__(self, x, y, 45, 30, True)
        self._sprite = sf.Sprite(Res.small_platform)
        self._sprite.position = sf.Vector2(x, y)
        self._on_me = []
        self._time = 3
        self._accum = 0
        self._direction = 1
    
    def update(self, dt):
        # Update accumulator and direction stuff
        self._accum += dt
        if self._accum >= self._time:
            self._accum = 0
            self._direction *= -1
    
        self.position = self.position + sf.Vector2(75*dt, 0)*self._direction
        for object in self._on_me:
            object.position = object.position + sf.Vector2(75*dt, 0)*self._direction
    
    def draw(self, target, render_states):
        self._sprite.position = self.position-sf.Vector2(3, 7)
        target.draw(self._sprite, render_states)
        
    def on_collision_begin(self, other, side):
        if not other.stationary and side == physics.side_up:
            self._on_me.append(other)
        return True
    
    def on_collision_end(self, other):
        if other in self._on_me:
            self._on_me.remove(other)

class SmallVMovingPlatform(sf.Drawable, Platform, Collideable):
    def __init__(self, x, y):
        Collideable.__init__(self, x, y, 45, 30, True)
        self._sprite = sf.Sprite(Res.small_platform)
        self._sprite.position = sf.Vector2(x, y)
        self._on_me = []
        self._time = 3
        self._accum = 0
        self._direction = 1
    
    def update(self, dt):
        # Update accumulator and direction stuff
        self._accum += dt
        if self._accum >= self._time:
            self._accum = 0
            self._direction *= -1
    
        self.position = self.position + sf.Vector2(0, 75*dt)*self._direction
        for object in self._on_me:
            object.position = object.position + sf.Vector2(0, 75*dt)*self._direction
    
    def draw(self, target, render_states):
        self._sprite.position = self.position-sf.Vector2(3, 7)
        target.draw(self._sprite, render_states)
        
    def on_collision_begin(self, other, side):
        if not other.stationary and side == physics.side_up:
            self._on_me.append(other)
        return True
    
    def on_collision_end(self, other):
        if other in self._on_me:
            self._on_me.remove(other)
