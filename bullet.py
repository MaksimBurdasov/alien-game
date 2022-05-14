import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self, ai_game):

		super().__init__()
		self.screen = ai_game.screen

		self.settings = ai_game.settings
		self.color  = self.settings.bullet_color

		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		self.y = float(self.rect.y)
		self.x = float(self.rect.x)
	
		self.x_axis_speed = 0

		if ai_game.ship.moving_right:
			self.x_axis_speed = 1
		elif ai_game.ship.moving_left:
			self.x_axis_speed = -1



	def update(self):
		self.y -= self.settings.bullet_speed
		self.rect.y = self.y
		self.x += self.x_axis_speed
		self.rect.x = self.x


	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)