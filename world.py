from player import Player
from platform import *

class World:

    def __init__(self, physics):
        self.physics = physics

        self.player = Player(100, 50)
        self.physics.add_collideable(self.player)
        
        self.platforms = []

    def create_big_platform(self, x, y):
        platform = BigPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)
        
    def create_small_platform(self, x, y):
        platform = SmallPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)

    def update(self, dt):
        self.player.update(dt)

        self.physics.handle_collisions()

    def draw(self, target):
        for platform in self.platforms:
            target.draw(platform)

        target.draw(self.player)
