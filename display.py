import globals


def update_display_mode():
    if(globals.fullscreen):
        # if fullscreen is True
        globals.window = globals.pygame.display.set_mode(
            (globals.width, globals.height),
            globals.pygame.FULLSCREEN)
    else:
        # if fullscreen is False
        globals.window = globals.pygame.display.set_mode(
            (globals.width, globals.height))


def toggle_fullscreen():
    # flip the global fullscreen boolean
    globals.fullscreen = not globals.fullscreen
    # update the display mode, which will apply our toggle
    update_display_mode()


def set_fullscreen(is_fullscreen):
    globals.fullscreen = is_fullscreen
    update_display_mode()
