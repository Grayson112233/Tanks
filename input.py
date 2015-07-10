import pygame
import globals


def isKeyJustPressed(key):
    for event in globals.events:
        if event.type == pygame.KEYDOWN:
            if event.key == key:
                return True
    return False


def isKeyPressed(key):
    states = globals.pygame.key.get_pressed()
    if states[key] == 1:
        return True
    return False
