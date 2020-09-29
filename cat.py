import pygame
from pygame.draw import *
from math import pi

pygame.init()

FPS = 30
screen_width = 500
screen_heigth = 700
screen = pygame.display.set_mode((screen_width, screen_heigth))

back_up_colour = (184, 134, 60)
back_down_colour = (218, 165, 32)
big_window_colour = (240, 255, 255)
small_window_colour = (135, 206, 250)
cat_colour = (244, 164, 96)
grey = (192, 192, 192)


def background():
    rect(screen, (back_up_colour), (0, 0, screen_width, screen_heigth // 7 * 3), 0)
    rect(screen, (back_down_colour), (0, screen_heigth // 7 * 3, screen_width, screen_heigth // 7 * 4), 0)
    return None


def window(x, y):
    rect(screen, big_window_colour, (x, y, 200, 280), 0)
    rect(screen, small_window_colour, (x + 10, y + 10, 80, 70), 0)
    rect(screen, small_window_colour, (x + 110, y + 10, 80, 70), 0)
    rect(screen, small_window_colour, (x + 10, y + 100, 80, 170), 0)
    rect(screen, small_window_colour, (x + 110, y + 100, 80, 170), 0)
    return None


def cat(x, y, k):
    # tale
    ellipse(screen, cat_colour, (x + 250 * k, y + 45 * k, 200 * k, 50 * k))
    ellipse(screen, (0, 0, 0), (x + 250 * k, y + 45 * k, 200 * k, 50 * k), 1)
    #body
    ellipse(screen, cat_colour, (x, y, int(320 * k), int(160 * k)))
    ellipse(screen, (0, 0, 0), (x, y, int(320 * k), int(160 * k)), 1)
    #back leg
    circle(screen, cat_colour, (int(x + 270 * k) , int(y + 130 * k) ), int(50 * k), 0)
    circle(screen, (0, 0, 0), (int(x + 270 * k) , int(y + 130 * k) ), int(50 * k), 1)
    ellipse(screen, cat_colour, (x + 290 * k, y + 130 * k, 50 * k, 100 * k), 0)
    ellipse(screen, (0, 0, 0), (x + 290 * k, y + 130 * k, 50 * k, 100 * k), 1)
    #front legs
    ellipse(screen, cat_colour, (x + 15 * k, y + 135 * k, 100 * k, 40 * k))
    ellipse(screen, (0, 0, 0), (x + 15 * k, y + 135 * k, 100 * k, 40 * k), 1)
    ellipse(screen, cat_colour, (x - 30 * k, y + 65 * k, 50 * k, 100 * k))
    ellipse(screen, (0, 0, 0), (x - 30 * k, y + 65 * k, 50 * k, 100 * k), 1)
    #head
    circle(screen, cat_colour, (int(x + 10 * k),  int(y + 75 * k)), int(70 * k))
    circle(screen, (0, 0, 0), (int(x + 10 * k),  int(y + 75 * k)), int(70 * k), 1)
    #eyes
    circle(screen, (60, 179, 113), (int(x - 20 * k), int(y + 70 * k)), int(18 * k), 0)
    circle(screen, (60, 179, 113), (int(x + 40 * k), int(y + 70 * k)), int(18 * k), 0)
    circle(screen, (0, 0, 0), (int(x - 20 * k), int(y + 70 * k)), int(18 * k), 1)
    circle(screen, (0, 0, 0), (int(x + 40 * k), int(y + 70 * k)), int(18 * k), 1)
    ellipse(screen, (0, 0, 0), (x - 18 * k, y + 58 * k, 8 * k, 25 * k))
    ellipse(screen, (0, 0, 0), (x + 42 * k, y + 58 * k, 8 * k, 25 * k))
    #right ear
    polygon(screen, cat_colour,
            ((int(x + 62 * k), int(y + 2 * k)), (int(x + 32 * k), int(y + 23 * k)), (int(x + 63 * k), int(y + 43 * k))))
    polygon(screen, (0, 0 ,0),
            ((int(x + 62 * k), int(y + 2 * k)), (int(x + 32 * k), int(y + 23 * k)), (int(x + 63 * k), int(y + 43 * k))), 1)
    polygon(screen, (255, 192, 203),
            ((int(x + 58 * k), int(y + 7 * k)), (int(x + 37 * k), int(y + 22 * k)), (int(x + 60 * k), int(y + 40 * k))))
    #left ear
    polygon(screen, cat_colour,
            ((int(x - 52 * k), int(y + 2 * k)), (int(x - 22 * k), int(y + 23 * k)), (int(x - 53 * k), int(y + 43 * k))))
    polygon(screen, (0, 0, 0),
            ((int(x - 52 * k), int(y + 2 * k)), (int(x - 22 * k), int(y + 23 * k)), (int(x - 53 * k), int(y + 43 * k))),
            1)
    polygon(screen, (255, 192, 203),
            ((int(x - 48 * k), int(y + 7 * k)), (int(x - 27 * k), int(y + 22 * k)), (int(x - 50 * k), int(y + 40 * k))))
    #nose
    polygon(screen, (255, 192, 203),
            ((int(x + 10 * k), int(y + 100 * k)), (int(x + 1 * k), int(y + 95 * k)), (int(x + 19 * k), int(y + 95 * k))))
    polygon(screen, (0, 0, 0),
            ((int(x + 10 * k), int(y + 100 * k)), (int(x + 1 * k), int(y + 95 * k)), (int(x + 19 * k), int(y + 95 * k))), 1)
    #mouth
    arc(screen, (0, 0, 0), (x + 10 * k, y + 80 * k, 40 * k, 40 * k), pi , 3 * pi / 2, 1)
    arc(screen, (0, 0, 0), (x - 30 * k, y + 80 * k, 40 * k, 40 * k), 3 * pi / 2, 2 * pi, 1)
    #whiskers
    arc(screen, (0, 0, 0), (x - 55 * k, y + 95 * k, 150 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, (0, 0, 0), (x - 45 * k, y + 98 * k, 130 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, (0, 0, 0), (x - 35 * k, y + 101 * k, 110 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, (0, 0, 0), (x - 80 * k, y + 95 * k, 150 * k, 40 * k),  pi / 2, pi - 0.2, 1)
    arc(screen, (0, 0, 0), (x - 70 * k, y + 98 * k, 130 * k, 40 * k), pi / 2, pi - 0.2, 1)
    arc(screen, (0, 0, 0), (x - 60 * k, y + 101 * k, 110 * k, 40 * k), pi / 2, pi - 0.2, 1)
    return None


def clew(x ,y ,k):
    circle(screen, grey,  (x, y), 50 * k, 0)
    circle(screen, (0, 0, 0), (x, y), 50 * k, 1)
    arc(screen, (0, 0, 0), (x - 85 * k, y - 30 * k, 120 * k, 100 * k), 0, pi / 2, 1)
    arc(screen, (0, 0, 0), (x - 80 * k, y - 40 * k, 120 * k, 100 * k), 0, pi / 2, 1)
    arc(screen, (0, 0, 0), (x - 20 * k, y - 30 * k, 120 * k, 120 * k), 3 * pi/ 4,  pi , 1)
    arc(screen, (0, 0, 0), (x - 10 * k, y - 20 * k, 120 * k, 120 * k), 3 * pi / 4, pi, 1)
    arc(screen, (0, 0, 0), (x - 5 * k, y - 16 * k, 120 * k, 120 * k), 3 * pi / 4, pi, 1)
    return None


background()
window(290, 10)
cat(80, 320, 0.5)
clew(330, 600, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()