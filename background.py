import pygame

from pygame.sprite import Sprite
from random import randint


class Around(Sprite): 
	
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		self.image = pygame.image.load('images/around.bmp') 
		self.image = pygame.transform.scale(self.image,
            (self.screen_rect.width // 10, self.screen_rect.height // 6))

		self.rect = self.image.get_rect()

		self.rect.x = 20
		self.rect.y = -20

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
	

	def update(self):
		self.y += self.settings.bg_image_speed_factor
		if self.y >= self.screen_rect.height:
			self.y = -20
			self.x = randint(1, self.screen_rect.width)
			self.rect.x = self.x
		self.rect.y = self.y



	def blitme(self):
		self.screen.blit(self.image, self.rect)
 	