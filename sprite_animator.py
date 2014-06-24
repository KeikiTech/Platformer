import sys
import sfml as sf

from player import Player
from world import World

def calculate_frame_loop_args(row):
    start = (row - 1) * 6
    end = start + 5
    return start, end

# create the main window
window = sf.RenderWindow(sf.VideoMode(800, 480), "pySFML Window")
window.key_repeat_enabled = False
view = window.default_view
player = Player(0, 0)
player._sprite.set_frame_loop(12, 17)
row_number = int(sys.argv[1])
frame_start, frame_end = calculate_frame_loop_args(row_number)
player._sprite.set_frame_loop(frame_start, frame_end)
player._sprite._frame_delay = float(sys.argv[2])
    

WORLD_FILENAME = "Content/world1.tsv"

clock = sf.Clock()
dt_accum = 0

# start the game loop
while window.is_open:
    dt = clock.restart().seconds

    ## Update
    player._sprite.update(dt)

    ## Draw
    window.clear(sf.Color(120, 120, 120)) # clear screen
    window.view = view
    
    # Draw the world
    window.draw(player)

    #### Draw GUI stuff, reset view
    window.view = window.default_view
   
    window.display() # update the window


