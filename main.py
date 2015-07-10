import globals
import pygame
from display import update_display_mode, toggle_fullscreen
from input import isKeyJustPressed
from tank import Tank

globals.width = 640
globals.height = 480


def main():

    pygame.init()
    globals.pygame = pygame
    update_display_mode()
    clock = pygame.time.Clock()

    entities = []

    entities.append(Tank(100, 100))

    loop = True

    while(loop):
        clock.tick(60)  # 60 FPS
        globals.window.fill((255, 255, 255))  # Fill window white

        globals.events = pygame.event.get()

        for entitiy in entities:
            entitiy.update()

        for entitiy in entities:
            entitiy.draw()

        if isKeyJustPressed(pygame.K_RETURN):
            toggle_fullscreen()

        if isKeyJustPressed(pygame.K_ESCAPE):
            globals.pygame.quit()
            loop = False

        # Flip the buffer
        pygame.display.flip()

main()
