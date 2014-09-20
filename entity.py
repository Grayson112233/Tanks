import globals
import pygame

class Entity(): # the base for all objects that will be drawn on the screen in the game

	def __init__(self):
		self.img = pygame.image.load("res/pics/box.png") # default image
		self.x = 0 # default x coord
		self.y = 0 # default y coord

	def draw(self): # draw the entity's image on the screen at its coords
		globals.window.blit(self.img, (self.x, self.y))

	def update(self): # move the entity with the arrow keys
		if(globals.inputs.isKeyDown("up")):
			self.y -= 5
		if(globals.inputs.isKeyDown("down")):
			self.y += 5
		if(globals.inputs.isKeyDown("right")):
			self.x += 5
		if(globals.inputs.isKeyDown("left")):
			self.x -= 5
		self.clamp() # clamp entity to the screen

	def clamp(self):
		if self.x < 0: self.x = 0
		if self.y < 0: self.y = 0
		if self.x > globals.window.get_width() - self.img.get_width(): self.x = globals.window.get_width() - self.img.get_width()
		if self.y > globals.window.get_height() - self.img.get_height(): self.y = globals.window.get_height() - self.img.get_height()