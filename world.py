from player import Player
from platform import *
from fireball import Fireball

class World:

    MAX_Y = 1000

    def __init__(self, physics, font):
        self.physics = physics
        self.font = font

        self.player = Player(100, 50)
        self.physics.add_collideable(self.player)
        
        self.platforms = []
        self.fireballs = []
        self.text = []

    def load(self, iostream):
        for line in iostream:
            if line.startswith("#"):
                continue
            fields = line.strip().split("\t")
            if len(fields) < 3:
                continue
            x = int(fields[1])
            y = int(fields[2])
            if fields[0] == "Text":
                text = fields[3]
                text = text.replace("\\n", "\n")
                self.create_text(x, y, text)
            elif fields[0] == "BigPlatform":
                self.create_big_platform(x, y)
            elif fields[0] == "SmallPlatform":
                self.create_small_platform(x, y)
            elif fields[0] == "SmallHMovingPlatform":
                self.create_small_hmoving_platform(x, y)
            elif fields[0] == "SmallVMovingPlatform":
                self.create_small_vmoving_platform(x, y)
            elif fields[0] == "Fireball":
                self.create_fireball(x, y)

    def create_text(self, x, y, text):
        text_object = sf.Text(text, self.font, 20)
        text_object.position = sf.Vector2(x, y)
        self.text.append(text_object)

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
    
        # Check for game over; respawn if necessary
        if self.player.position.y > self.MAX_Y:
            self.player.position.x = self.player.current_checkpoint.x
            self.player.position.y = self.player.current_checkpoint.y

        self.player.update(dt)

        self.physics.handle_collisions()

    def draw(self, target):
        for platform in self.platforms:
            target.draw(platform)

        for fireball in self.fireballs:
            target.draw(fireball)

        target.draw(self.player)
        
        for text in self.text:
            target.draw(text)
