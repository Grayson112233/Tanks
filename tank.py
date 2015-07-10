import pygame
import globals
import math
from input import isKeyPressed, isKeyJustPressed


class Tank():

    FORWARD_SPEED = 1
    BACKWARD_SPEED = 0.7
    TURNSPEED = 1
    TURRET_TURNSPEED = 1
    TURRET_OFFSET = 12
    GUN_LENGTH = 76
    GUN_WIDTH = 4
    GUN_COOLDOWN = 60 * 3

    def __init__(self, x, y, angle=0):

        # LOAD RESOURCES

        self.img = pygame.image.load("res/pics/tank_base.png")
        self.img_turret = pygame.image.load("res/pics/tank_turret.png")

        self.sound_shoot = pygame.mixer.Sound("res/sounds/tank_shoot.wav")
        self.sound_explode = pygame.mixer.Sound("res/sounds/tank_shoot.wav")
        self.sound_dryfire = pygame.mixer.Sound("res/sounds/tank_dryfire.wav")
        self.sound_finish_reload = pygame.mixer.Sound("res/sounds/tank_finish_reload.wav")

        # VARS

        self.x = x
        self.y = y
        self.speed = 0
        self.angle = angle
        self.turret_angle = angle
        self.gun_length_modifier = 0
        self.gun_shoot_delay = -1
        self.gun_cooldown_timer = -1

        pygame.mixer.init()

    def update(self):
        # manage forward and backward acceleration
        if isKeyPressed(pygame.K_w):
            self.speed = self.FORWARD_SPEED
        if isKeyPressed(pygame.K_s):
            self.speed = -self.BACKWARD_SPEED
        if(not isKeyPressed(pygame.K_w) and not
           isKeyPressed(pygame.K_s)):
                self.speed = 0
        # if tank is turning right,
        # the way the tracks function
        # will move it forward a bit,
        # not just spin it on a dime
        if isKeyPressed(pygame.K_d):
            self.angle -= self.TURNSPEED
            if self.speed < 0:
                self.angle += self.TURNSPEED * 2
            if self.speed == 0:
                self.speed = self.FORWARD_SPEED

        if isKeyPressed(pygame.K_a):
            self.angle += self.TURNSPEED
            if self.speed < 0:
                self.angle -= self.TURNSPEED * 2
            if self.speed == 0:
                self.speed = self.FORWARD_SPEED
        # trig gives us the correct position to draw the turret
        self.y += self.speed * math.sin(math.radians(self.angle + 270))
        self.x -= self.speed * math.cos(math.radians(self.angle + 270))
        # turret moves left and right with arrow keys
        if isKeyPressed(pygame.K_RIGHT):
            self.turret_angle -= self.TURRET_TURNSPEED
        if isKeyPressed(pygame.K_LEFT):
            self.turret_angle += self.TURRET_TURNSPEED

        # GUN COOLDOWN
        if self.gun_cooldown_timer > 0:
            self.gun_cooldown_timer -= 1
        if self.gun_cooldown_timer == 0:
            self.sound_finish_reload.play()  # play a reloading sound
            self.gun_cooldown_timer = -1

        # GUN BARREL BLOWBACK
        if self.gun_length_modifier < 0:
            self.gun_length_modifier += 0.5

        # FIRE GUN
        if self.gun_shoot_delay > 0:
            self.gun_shoot_delay -= 1
        if self.gun_shoot_delay == 0:
            self.gun_length_modifier = -12
            self.gun_shoot_delay = -1

        # TRIGGER GUN TO FIRE
        if isKeyJustPressed(pygame.K_SPACE):
            if self.gun_cooldown_timer < 1:
                self.gun_cooldown_timer = self.GUN_COOLDOWN
                self.gun_shoot_delay = 10
                self.sound_shoot.play()

        # CLAMP TO WINDOW
        self.clamp()

    def draw(self):
        # Rotation in pygame requires a rect object to be rotated,
        # then for the surface object drawn with the rect as a position argument

        # TANK BASE
        rot_img = pygame.transform.rotate(self.img, self.angle)
        img_rect = rot_img.get_rect()
        img_rect.center = self.img.get_rect(top=self.y, left=self.x).center
        globals.window.blit(rot_img, img_rect)

        # TANK GUN
        turret_x = self.x - self.TURRET_OFFSET * math.cos(math.radians(self.angle + 270))
        turret_y = self.y + self.TURRET_OFFSET * math.sin(math.radians(self.angle + 270))
        rot_img = pygame.transform.rotate(self.img_turret, self.angle + self.turret_angle)
        gun_breach = self.img.get_rect(top=turret_y, left=turret_x).center
        gun_tip = [0, 0]
        gun_tip[0] = gun_breach[0] - (self.GUN_LENGTH + self.gun_length_modifier) * math.cos(math.radians(self.angle + 270 + self.turret_angle))
        gun_tip[1] = gun_breach[1] + (self.GUN_LENGTH + self.gun_length_modifier) * math.sin(math.radians(self.angle + 270 + self.turret_angle))
        gun_tip = tuple(gun_tip)
        pygame.draw.line(globals.window, (0, 0, 0), gun_breach, gun_tip, self.GUN_WIDTH)

        # TANK TURRET
        turret_x = self.x - self.TURRET_OFFSET * math.cos(math.radians(self.angle + 270))
        turret_y = self.y + self.TURRET_OFFSET * math.sin(math.radians(self.angle + 270))
        rot_img = pygame.transform.rotate(self.img_turret, self.angle + self.turret_angle)
        img_rect = rot_img.get_rect()
        img_rect.center = self.img.get_rect(top=turret_y, left=turret_x).center
        globals.window.blit(rot_img, img_rect)

    def clamp(self):
        if(self.x < 0):
            self.x = 0
        if(self.y < 0):
            self.y = 0
        if(self.x > globals.width):
            self.x = globals.width
        if(self.y > globals.height):
            self.y = globals.height
