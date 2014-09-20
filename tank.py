import globals
import pygame
import math
from entity import Entity

class Tank(Entity):

	def __init__(self, x, y):

		Entity.__init__(self)

		self.x = x
		self.y = y

		self.img = pygame.image.load("res/pics/tank_base.png")
		self.img_turret = pygame.image.load("res/pics/tank_turret.png")

		self.sound_shoot = pygame.mixer.Sound("res/sounds/tank_shoot.wav")
		self.sound_explode = pygame.mixer.Sound("res/sounds/tank_shoot.wav")
		self.sound_dryfire = pygame.mixer.Sound("res/sounds/tank_dryfire.wav")
		self.sound_finish_reload = pygame.mixer.Sound("res/sounds/tank_finish_reload.wav")
		
		self.forward_speed = 1
		self.backward_speed = 0.7
		self.turnspeed = 1
		self.turret_turnspeed = 1
		self.turret_offset = 12
		self.gun_length = 76
		self.gun_width = 4
		self.gun_cooldown = 60 * 3

		self.speed = 0
		self.angle = 0
		self.turret_angle = 0
		self.gun_length_modifier = 0
		self.gun_shoot_delay = -1
		self.gun_cooldown_timer = -1

		pygame.mixer.init()
		
	def update(self):
		# manage forward and backward acceleration
		if globals.inputs.isKeyDown("w"): self.speed = self.forward_speed
		if globals.inputs.isKeyDown("s"): self.speed = -self.backward_speed
		if not globals.inputs.isKeyDown("w") and not globals.inputs.isKeyDown("s"): self.speed = 0
		# if tank is turning right,
		# the way the tracks function
		# will move it forward a bit,
		# not just spin it on a dime
		if globals.inputs.isKeyDown("d"): 
			self.angle -= self.turnspeed
			if self.speed < 0: self.angle += self.turnspeed * 2
			if self.speed == 0: self.speed = self.forward_speed

		if globals.inputs.isKeyDown("a"): 
			self.angle += self.turnspeed
			if self.speed < 0: self.angle -= self.turnspeed * 2
			if self.speed == 0: self.speed = self.forward_speed
		# trig gives us the correct position to draw the turret
		self.y += self.speed * math.sin(math.radians(self.angle + 270))
		self.x -= self.speed * math.cos(math.radians(self.angle + 270))
		# turret moves left and right with arrow keys
		if globals.inputs.isKeyDown("right"): self.turret_angle -= self.turret_turnspeed
		if globals.inputs.isKeyDown("left"): self.turret_angle += self.turret_turnspeed
		# gun cooldown
		if self.gun_cooldown_timer > 0: self.gun_cooldown_timer -= 1
		if self.gun_cooldown_timer == 0:
			self.sound_finish_reload.play() # play a reloading sound
			self.gun_cooldown_timer = -1
		# push gun barrel back out after firing
		if self.gun_length_modifier < 0: self.gun_length_modifier += 0.5
		# FIRE GUN
		if self.gun_shoot_delay > 0: self.gun_shoot_delay -= 1
		if self.gun_shoot_delay == 0:
			self.gun_length_modifier = -12
			self.gun_shoot_delay = -1
		# TRIGGER GUN TO FIRE
		if globals.inputs.isKeyDown("space"):
			if self.gun_cooldown_timer < 1:
				self.gun_cooldown_timer = self.gun_cooldown
				self.gun_shoot_delay = 10
				self.sound_shoot.play()
		# clamp to window
		self.clamp()

	def draw(self):
		# Rotation in pygame requires a rect object to be rotated,
		# then for the surface object drawn with the rect as a position argument

		# TANK BASE
		rot_img = pygame.transform.rotate(self.img, self.angle)
		img_rect = rot_img.get_rect()
		img_rect.center = self.img.get_rect(top = self.y, left=self.x).center
		globals.window.blit(rot_img, img_rect)
		# TANK GUN
		turret_x = self.x - self.turret_offset * math.cos(math.radians(self.angle + 270))
		turret_y = self.y + self.turret_offset * math.sin(math.radians(self.angle + 270))
		rot_img = pygame.transform.rotate(self.img_turret, self.angle + self.turret_angle)
		gun_breach = self.img.get_rect(top = turret_y, left=turret_x).center
		gun_tip = [0, 0]
		gun_tip[0] = gun_breach[0] - (self.gun_length + self.gun_length_modifier) * math.cos(math.radians(self.angle + 270 + self.turret_angle))
		gun_tip[1] = gun_breach[1] + (self.gun_length + self.gun_length_modifier) * math.sin(math.radians(self.angle + 270 + self.turret_angle))
		gun_tip = tuple(gun_tip)
		pygame.draw.line(globals.window, (0, 0, 0), gun_breach, gun_tip, self.gun_width)
		# TANK TURRET
		turret_x = self.x - self.turret_offset * math.cos(math.radians(self.angle + 270))
		turret_y = self.y + self.turret_offset * math.sin(math.radians(self.angle + 270))
		rot_img = pygame.transform.rotate(self.img_turret, self.angle + self.turret_angle)
		img_rect = rot_img.get_rect()
		img_rect.center = self.img.get_rect(top = turret_y, left=turret_x).center
		globals.window.blit(rot_img, img_rect)



	