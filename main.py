import sys
import sfml as sf

from input_system import InputSystem
from physics import Physics
from res import Res
from player import Player
from platform import *
from world import World
from world_editor import WorldEditor

# create the main window
window = sf.RenderWindow(sf.VideoMode(800, 480), "Platformer")
window.key_repeat_enabled = False
view = window.default_view

input = InputSystem(window)
physics = Physics()

WORLD_FILENAME = "Content/world1.tsv"

try:
    font = sf.Font.from_file("Content/8bit.ttf")

    world = World(physics, font)
    with open(WORLD_FILENAME, "r") as worldfile:
        world.load(worldfile)

    editor = WorldEditor(view, world)

    # create some graphical text to display
    frame_rate = sf.Text("0", font, 20)

except IOError: exit(1)

input.add_key_handler(world.player)
input.add_key_handler(editor)
input.add_mouse_handler(editor)

clock = sf.Clock()
frame_accum = 0
dt_accum = 0

Res.loop = True
Res.music.play()

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

    # Update world
    world.update(dt)
	
    # Update camera
    view.center = world.player._sprite.position
    
    ## Draw
    
    window.clear(sf.Color(120, 120, 120)) # clear screen
    window.view = view
    
    # Draw the world
    world.draw(window)

    #### Draw GUI stuff, reset view
    window.view = window.default_view
   
    # Draw framerate
    window.draw(frame_rate)
    
    window.display() # update the window
