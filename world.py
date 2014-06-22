from player import Player
from platform import *
from fireball import Fireball

class World:

    def __init__(self, physics):
        self.physics = physics

        self.player = Player(100, 50)
        self.physics.add_collideable(self.player)
        
        self.platforms = []
        self.fireballs = []

    def load(self, iostream):
        for line in iostream:
            if line.startswith("#"):
                continue
            fields = line.strip().split()
            if len(fields) < 3:
                continue
            x = int(fields[1])
            y = int(fields[2])
            if fields[0] == "BigPlatform":
                self.create_big_platform(x, y)
            elif fields[0] == "SmallPlatform":
                self.create_small_platform(x, y)
            elif fields[0] == "SmallHMovingPlatform":
                self.create_small_hmoving_platform(x, y)
            elif fields[0] == "SmallVMovingPlatform":
                self.create_small_vmoving_platform(x, y)
            elif fields[0] == "Fireball":
                self.create_fireball(x, y)


    def create_big_platform(self, x, y):
        platform = BigPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)
        
    def create_small_platform(self, x, y):
        platform = SmallPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)

    def create_small_hmoving_platform(self, x, y):
        platform = SmallHMovingPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)

    def create_small_vmoving_platform(self, x, y):
        platform = SmallVMovingPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)

    def create_fireball(self, x, y):
        fireball = Fireball(x, y)
        self.fireballs.append(fireball)
        self.physics.add_collideable(fireball)

    def update(self, dt):
        for platform in self.platforms:
            platform.update(dt)

        for fireball in self.fireballs:
            fireball.update(dt)
    
        self.player.update(dt)

        self.physics.handle_collisions()

    def draw(self, target):
        for platform in self.platforms:
            target.draw(platform)

        for fireball in self.fireballs:
            target.draw(fireball)

        target.draw(self.player)
