import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))
screen2 = pygame.transform.rotate(screen, 45)

back_up_colour = (184, 134, 60)
back_down_colour = (218, 165, 32)
back_window_colour = (240, 255, 255)
small_window_colour = (135, 206, 250)
cat_colour = (244, 164, 96)

def background():
    rect(screen, (back_up_colour), (0, 0, 500, 300), 0)
    rect(screen, (back_down_colour), (0, 300, 500, 400), 0)
    return None

def window():
    rect(screen, (back_window_colour), (290, 10, 200, 280), 0)
    rect(screen, (small_window_colour), (300, 20, 80, 70), 0)
    rect(screen, (small_window_colour), (400, 20, 80, 70), 0)
    rect(screen, (small_window_colour), (300, 110, 80, 170), 0)
    rect(screen, (small_window_colour), (400, 110, 80, 170), 0)
    return None

def cat():
    ellipse(screen, (cat_colour), (80, 320, 320, 150))
    ellipse(screen, (0, 0, 0), (80, 320, 320, 150), 1)
    circle(screen, (cat_colour), (350, 450), 50, 0)
    circle(screen, (0, 0, 0), (350, 450), 50, 1)
    circle(screen, (cat_colour), (90, 395), 70)
    circle(screen, (0, 0, 0), (90, 395), 70, 1)


    return None

background()
window()
cat()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()