import globals
import pygame
from inputs import Inputs
from entity import Entity
from render import render
from display import update_display_mode, toggle_fullscreen
from update import update
from tank import Tank

globals.width = 640
globals.height = 480
globals.fullscreen = False

def main():

	pygame.init()
	globals.pygame = pygame # assign global pygame for other modules to reference
	globals.inputs = Inputs(pygame) # assign global inputs for other modules to reference
	update_display_mode() # now that the global display properties have been set up, update the display
	clock = pygame.time.Clock() # clock to tick / manage delta

	entities = [] # contains every object that will be drawn in the game

	entities.append(Tank(100, 100)) # create a new tank entity at (100, 100)

	loop = True # for controlling the game loop

	while(loop):
		clock.tick(60) # tick the clock with a target 60 fps
		globals.window.fill((255, 255, 255))

		globals.inputs.update() # refresh inputs

		update(entities) # update all entities
		render(entities) # draw all entities

		if(globals.inputs.isKeyDown("enter")): toggle_fullscreen() # enter toggles fullscreen
		if(globals.inputs.isKeyDown("escape")): loop = False # escape key exits game
		if(globals.inputs.isQuitPressed()): loop = False # red 'x' button exits game

		pygame.display.flip() # flip the display, which finally shows our render

	pygame.quit() # unload pygame modules

main() # initiate game