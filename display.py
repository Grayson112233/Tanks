import globals

def update_display_mode():
	if(globals.fullscreen): # if fullscreen is True
		globals.window = globals.pygame.display.set_mode((globals.width, globals.height), globals.pygame.FULLSCREEN)
	else: # if fullscreen is False
		globals.window = globals.pygame.display.set_mode((globals.width, globals.height))

def toggle_fullscreen():
	globals.fullscreen = not globals.fullscreen # flip the global fullscreen boolean
	update_display_mode() # update the display mode, which will apply our toggle