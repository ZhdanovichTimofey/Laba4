import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400), 0)
circle(screen, (255, 255, 0), (200, 200), 100, 0)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
circle(screen, (255, 0, 0), (150, 170), 20, 0)
circle(screen, (0, 0, 0), (150, 170), 20, 1)
circle(screen, (0, 0, 0), (150, 170), 10, 0)
circle(screen, (255, 0, 0), (250, 170), 15, 0)
circle(screen, (0, 0, 0), (250, 170), 15, 1)
circle(screen, (0, 0, 0), (250, 170), 8, 0)
rect(screen, (0, 0, 0), (150, 250, 100, 20), 0)
polygon(screen, (0, 0, 0), [(90, 85), (85, 95), (175, 155), (180, 145)], 0)
polygon(screen, (0, 0, 0), [(210, 160), (220, 170), (250, 150), (240, 140)], 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()