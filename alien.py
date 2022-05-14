import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):

	def __init__(self, ai_game): # конструктор
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		self.green_costume = pygame.image.load('images/alieng.bmp')
		self.green_costume = pygame.transform.scale(self.green_costume,
            (self.screen_rect.width // 15, self.screen_rect.height // 10))
		
		self.purple_costume = pygame.image.load('images/alienp.bmp')
		self.purple_costume = pygame.transform.scale(self.purple_costume,
            (self.screen_rect.width // 15, self.screen_rect.height // 10))

		self.orange_costume = pygame.image.load('images/alieno.bmp')
		self.orange_costume = pygame.transform.scale(self.orange_costume,
            (self.screen_rect.width // 15, self.screen_rect.height // 10))

		self.alien_costumes = [self.green_costume, self.purple_costume, self.orange_costume]
		self.carrent_costume = 0
		self.image = self.alien_costumes[self.carrent_costume]
		self.rect = self.image.get_rect()

		self.rect.x = 50
		self.rect.y = 50

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.hp = self.settings.start_health_alien #


	def update(self):
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x
		# self.y = self.rect.y

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True






















