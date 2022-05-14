import pygame
import random

WIDTH = 360
HEIGHT = 480

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 145, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("My Game")

rectangle1 = pygame.Rect(10, 30, 50, 70) #продолжить с отображения этого прямоугольника
running = True 
while running:
	screen.fill(ORANGE)
	pygame.display.flip()

	
	pygame.draw.rect(ORANGE, rectangle1)

	for event in pygame.event.get(): #Проверка событий
		if event.type == pygame.QUIT:
			running = False
	


pygame.quit()