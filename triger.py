import pygame
from pygame.sprite import Sprite

class Triger(Sprite):

	def __init__(self, ai_game):

		super().__init__()
		self.screen = ai_game.screen

		self.settings = ai_game.settings
		self.color  = (255, 255, 255)

		self.rect = pygame.Rect(0, 0, 50, 50)
		self.rect.center = 350, 350

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.r = .2


	def update(self, x_ship, y_ship):
		x_tr, y_tr = self.rect.center
		a = x_tr - x_ship
		b = y_tr - y_ship
		R = (a ** 2 + b ** 2) ** .5
		dx = a * self.r / R
		dy = b * self.r / R

		self.x -= dx
		self.rect.x = self.x
		self.y -= dy
		self.rect.y = self.y


	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)