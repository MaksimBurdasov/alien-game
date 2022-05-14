import pygame
from pygame.sprite import Sprite

class Ship_grey(Sprite):
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings
       
        self.image = pygame.image.load('images/ship_grey.png')
        self.image = pygame.transform.scale(self.image,
            (self.screen_rect.width // 25, self.screen_rect.height // 25))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #флаг перемещения вправо
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False # движение вверх
        self.moving_down = False #движение вниз


    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed_factor 
            self.rect.x = self.x
        if self.moving_left:
            self.x -= self.settings.ship_speed_factor
            self.rect.x = self.x 
        if self.moving_up: #если нажата кнопка вверх перемешение вверх по оси y
            self.y -= self.settings.ship_speed_factor
            self.rect.y = self.y 
        if self.moving_down: #если нажата кнопка вниз перемешение вниз по оси y
            self.y += self.settings.ship_speed_factor
            self.rect.y = self.y 
        # Блокировка сторон(Не выходит за рамки)
        if self.rect.right < 0: 
            self.x = self.screen_rect.width
            self.rect.x = self.x
            # self.rect.left = self.screen_rect.width
        elif self.rect.left > self.screen_rect.width:
            self.x = -self.rect.width
            self.rect.x = self.x 
            # self.rect.right = 0

        if self.rect.top < self.screen_rect.height // 3:
            self.rect.top = self.screen_rect.height // 3 
        if self.rect.bottom > self.screen_rect.height + 1:
            self.rect.bottom = self.screen_rect.height


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.rect.x = self.x
        self.y = float(self.rect.y)
        self.rect.y = self.y