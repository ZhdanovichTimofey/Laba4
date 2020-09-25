import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

rect(screen, (184, 134, 60), (0, 0, 500, 300), 0)
rect(screen, (218, 165, 32), (0, 300, 500, 400), 0)
rect(screen, (240, 255, 255), (290, 10, 200, 280), 0)
rect(screen, (135, 206, 250), (300, 20, 80, 70), 0)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()