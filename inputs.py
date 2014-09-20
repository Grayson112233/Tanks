import pygame

class Inputs():

	def __init__(self, pygame):
		self.pygame = pygame
		self.k_w = False
		self.k_a = False
		self.k_s = False
		self.k_d = False
		self.k_i = False
		self.k_j = False
		self.k_k = False
		self.k_l = False
		self.k_up = False
		self.k_down = False
		self.k_left = False
		self.k_right = False
		self.kp_8 = False
		self.kp_4 = False
		self.kp_5 = False
		self.kp_6 = False
		self.kp_0 = False
		self.kp_enter = False
		self.k_space = False
		self.k_escape = False
		self.k_return = False
		self.e_quit = False
		self.update()

	def update(self):
		pygame = self.pygame
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.e_quit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					self.k_w = True
				if event.key == pygame.K_a:
					self.k_a = True
				if event.key == pygame.K_s:
					self.k_s = True
				if event.key == pygame.K_d:
					self.k_d = True
				if event.key == pygame.K_i:
					self.k_i = True
				if event.key == pygame.K_j:
					self.k_j = True
				if event.key == pygame.K_k:
					self.k_k = True
				if event.key == pygame.K_l:
					self.k_l = True
				if event.key == pygame.K_SPACE:
					self.k_space = True
				if event.key == pygame.K_ESCAPE:
					self.k_escape = True
				if event.key == pygame.K_RETURN:
					self.k_return = True
				if event.key == pygame.K_UP:
					self.k_up = True
				if event.key == pygame.K_DOWN:
					self.k_down = True
				if event.key == pygame.K_RIGHT:
					self.k_right = True
				if event.key == pygame.K_LEFT:
					self.k_left = True
				if event.key == pygame.K_KP8:
					self.kp_8 = True
				if event.key == pygame.K_KP4:
					self.kp_4 = True
				if event.key == pygame.K_KP5:
					self.kp_5 = True
				if event.key == pygame.K_KP6:
					self.kp_6 = True
				if event.key == pygame.K_KP0:
					self.kp_0 = True
				if event.key == pygame.K_KP_ENTER:
					self.kp_enter = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					self.k_w = False
				if event.key == pygame.K_a:
					self.k_a = False
				if event.key == pygame.K_s:
					self.k_s = False
				if event.key == pygame.K_d:
					self.k_d = False
				if event.key == pygame.K_i:
					self.k_i = False
				if event.key == pygame.K_j:
					self.k_j = False
				if event.key == pygame.K_k:
					self.k_k = False
				if event.key == pygame.K_l:
					self.k_l = False
				if event.key == pygame.K_SPACE:
					self.k_space = False
				if event.key == pygame.K_ESCAPE:
					self.k_escape = False
				if event.key == pygame.K_RETURN:
					self.k_return = False
				if event.key == pygame.K_UP:
					self.k_up = False
				if event.key == pygame.K_DOWN:
					self.k_down = False
				if event.key == pygame.K_RIGHT:
					self.k_right = False
				if event.key == pygame.K_LEFT:
					self.k_left = False
				if event.key == pygame.K_KP8:
					self.kp_8 = False
				if event.key == pygame.K_KP4:
					self.kp_4 = False
				if event.key == pygame.K_KP5:
					self.kp_5 = False
				if event.key == pygame.K_KP6:
					self.kp_6 = False
				if event.key == pygame.K_KP0:
					self.kp_0 = False
				if event.key == pygame.K_KP_ENTER:
					self.kp_enter = False

	def isKeyDown(self, key):
		key = key.lower()
		if key == "up": return self.k_up
		if key == "down": return self.k_down
		if key == "left": return self.k_left
		if key == "right": return self.k_right
		if key == "w": return self.k_w
		if key == "a": return self.k_a
		if key == "s": return self.k_s
		if key == "d": return self.k_d
		if key == " ": return self.k_space
		if key == "space": return self.k_space
		if key == "return": return self.k_return
		if key == "enter": return self.k_return
		if key == "escape": return self.k_escape
		if key == "i": return self.k_i
		if key == "j": return self.k_j
		if key == "k": return self.k_k
		if key == "l": return self.k_l
		if key == "kp8": return self.kp_8
		if key == "kp4": return self.kp_4
		if key == "kp5": return self.kp_5
		if key == "kp6": return self.kp_6
		if key == "kp0": return self.kp_0
		if key == "kp_enter": return self.kp_enter

	def isQuitPressed(self):
		return self.e_quit
