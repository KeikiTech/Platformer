import sfml as sf

from input_system import InputSystem
from physics import Physics
from player import Player
from platform import *

# create the main window
window = sf.RenderWindow(sf.VideoMode(800, 480), "pySFML Window")
window.key_repeat_enabled = False
view = window.default_view

input = InputSystem(window)
physics = Physics()

try:
    # Create player
    player = Player(100, 50)
    physics.add_collideable(player)
    
    # Create platforms
    platform0 = BigPlatform(100, 200)
    physics.add_collideable(platform0)
    
    platform1 = SmallPlatform(400, 150)
    physics.add_collideable(platform1)

    platform2 = BigPlatform(0, 300)
    physics.add_collideable(platform2)

    # create some graphical text to display
    font = sf.Font.from_file("Content/8bit.ttf")
    frame_rate = sf.Text("0", font, 20)

except IOError: exit(1)

input.add_key_handler(player)

clock = sf.Clock()
frame_accum = 0
dt_accum = 0

# start the game loop
while window.is_open:
    dt = clock.restart().seconds
    
    # Calculate framerate
    frame_accum += 1
    dt_accum += dt
    if dt_accum >= 1:
        frame_rate.string = str(frame_accum)
        dt_accum = 0
        frame_accum = 0

    # process events
    input.handle()

    player.update(dt)

    # Update camera
    view.center = player._sprite.position
    
    physics.handle_collisions()
    
    ## Draw
    
    window.clear(sf.Color(120, 120, 120)) # clear screen
    window.view = view
    
    # Draw the platforms
    window.draw(platform0)
    window.draw(platform1)
    window.draw(platform2)
    
    # Draw the player
    window.draw(player)

    #### Draw GUI stuff, reset view
    #window.view = window.default_view
    
    # Draw framerate
    window.draw(frame_rate)
    
    window.display() # update the window
