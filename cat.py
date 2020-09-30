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
cat_colour1 = (244, 164, 96)
cat_colour2 = (105, 105, 105)
eyes_colour1 =(60, 179, 113)
eyes_colour2 = (0, 0, 205)
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


def cat_left(x, y, k, cat_colour, eyes_colour):
    # tale
    ellipse(screen, cat_colour, (x + 250 * k, y + 45 * k, 200 * k, 50 * k))
    ellipse(screen, (0, 0, 0), (x + 250 * k, y + 45 * k, 200 * k, 50 * k), 1)
    #body
    ellipse(screen, cat_colour, (x, y, int(320 * k), int(160 * k)))
    ellipse(screen, (0, 0, 0), (x, y, int(320 * k), int(160 * k)), 1)
    #back leg
    circle(screen, cat_colour, (int(x + 270 * k) , int(y + 130 * k)), int(50 * k), 0)
    circle(screen, (0, 0, 0), (int(x + 270 * k) , int(y + 130 * k) ), int(50 * k), 1)
    ellipse(screen, cat_colour, (x + 290 * k, y + 130 * k, 50 * k, 100 * k), 0)
    ellipse(screen, (0, 0, 0), (x + 290 * k, y + 130 * k, 50 * k, 100 * k), 1)
    #front legs
    ellipse(screen, cat_colour, (x + 15 * k, y + 135 * k, 100 * k, 40 * k))
    ellipse(screen, (0, 0, 0), (x + 15 * k, y + 135 * k, 100 * k, 40 * k), 1)
    ellipse(screen, cat_colour, (x - 30 * k, y + 65 * k, 50 * k, 100 * k))
    ellipse(screen, (0, 0, 0), (x - 30 * k, y + 65 * k, 50 * k, 100 * k), 1)
    #head
    circle(screen, cat_colour, (int(x + 10 * k), int(y + 75 * k)), int(70 * k))
    circle(screen, (0, 0, 0), (int(x + 10 * k),  int(y + 75 * k)), int(70 * k), 1)
    #eyes
    circle(screen, eyes_colour, (int(x - 20 * k), int(y + 70 * k)), int(18 * k), 0)
    circle(screen, eyes_colour, (int(x + 40 * k), int(y + 70 * k)), int(18 * k), 0)
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


def cat_right(x, y, k, cat_colour, eyes_colour):
    # tale
    ellipse(screen, cat_colour, (x - 100 * k, y + 45 * k, 200 * k, 50 * k))
    ellipse(screen, (0, 0, 0), (x - 100 * k, y + 45 * k, 200 * k, 50 * k), 1)
    # body
    ellipse(screen, cat_colour, (x, y, int(320 * k), int(160 * k)))
    ellipse(screen, (0, 0, 0), (x, y, int(320 * k), int(160 * k)), 1)
    # back leg
    circle(screen, cat_colour, (int(x + 50 * k), int(y + 130 * k)), int(50 * k), 0)
    circle(screen, (0, 0, 0), (int(x + 50 * k), int(y + 130 * k)), int(50 * k), 1)
    ellipse(screen, cat_colour, (x - 10 * k, y + 130 * k, 50 * k, 100 * k), 0)
    ellipse(screen, (0, 0, 0), (x - 10 * k, y + 130 * k, 50 * k, 100 * k), 1)
    # front legs
    ellipse(screen, cat_colour, (x + 210 * k, y + 135 * k, 100 * k, 40 * k))
    ellipse(screen, (0, 0, 0), (x + 210 * k, y + 135 * k, 100 * k, 40 * k), 1)
    ellipse(screen, cat_colour, (x + 310 * k, y + 65 * k, 50 * k, 100 * k))
    ellipse(screen, (0, 0, 0), (x + 310 * k, y + 65 * k, 50 * k, 100 * k), 1)
    # head
    circle(screen, cat_colour, (int(x + 320 * k), int(y + 75 * k)), int(70 * k))
    circle(screen, (0, 0, 0), (int(x + 320 * k), int(y + 75 * k)), int(70 * k), 1)
    # eyes
    circle(screen, eyes_colour, (int(x + 350 * k), int(y + 70 * k)), int(18 * k), 0)
    circle(screen, eyes_colour, (int(x + 290 * k), int(y + 70 * k)), int(18 * k), 0)
    circle(screen, (0, 0, 0), (int(x + 350 * k), int(y + 70 * k)), int(18 * k), 1)
    circle(screen, (0, 0, 0), (int(x + 290 * k), int(y + 70 * k)), int(18 * k), 1)
    ellipse(screen, (0, 0, 0), (x + 352 * k, y + 58 * k, 8 * k, 25 * k))
    ellipse(screen, (0, 0, 0), (x + 292 * k, y + 58 * k, 8 * k, 25 * k))
    # nose
    polygon(screen, (255, 192, 203),
            ((int(x + 320 * k), int(y + 100 * k)), (int(x + 311 * k), int(y + 95 * k)), (int(x + 329 * k), int(y + 95 * k))))
    polygon(screen, (0, 0, 0),
           ((int(x + 320 * k), int(y + 100 * k)), (int(x + 311 * k), int(y + 95 * k)), (int(x + 329 * k), int(y + 95 * k))),1)
    # mouth
    arc(screen, (0, 0, 0), (x + 320 * k, y + 80 * k, 40 * k, 40 * k), pi, 3 * pi / 2, 1)
    arc(screen, (0, 0, 0), (x + 280 * k, y + 80 * k, 40 * k, 40 * k), 3 * pi / 2, 2 * pi, 1)
    # whiskers
    arc(screen, (0, 0, 0), (x + 255 * k, y + 95 * k, 150 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, (0, 0, 0), (x + 265 * k, y + 98 * k, 130 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, (0, 0, 0), (x + 275 * k, y + 101 * k, 110 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, (0, 0, 0), (x + 230 * k, y + 95 * k, 150 * k, 40 * k), pi / 2, pi - 0.2, 1)
    arc(screen, (0, 0, 0), (x + 240 * k, y + 98 * k, 130 * k, 40 * k), pi / 2, pi - 0.2, 1)
    arc(screen, (0, 0, 0), (x + 250 * k, y + 101 * k, 110 * k, 40 * k), pi / 2, pi - 0.2, 1)
    # right ear
    polygon(screen, cat_colour,
            ((int(x + 372 * k), int(y + 2 * k)), (int(x + 342 * k), int(y + 23 * k)), (int(x + 373 * k), int(y + 43 * k))))
    polygon(screen, (0, 0, 0),
            ((int(x + 372 * k), int(y + 2 * k)), (int(x + 342 * k), int(y + 23 * k)), (int(x + 373 * k), int(y + 43 * k))),
            1)
    polygon(screen, (255, 192, 203),
            ((int(x + 368 * k), int(y + 7 * k)), (int(x + 347 * k), int(y + 22 * k)), (int(x + 370 * k), int(y + 40 * k))))
    # left ear
    polygon(screen, cat_colour,
            ((int(x + 258 * k), int(y + 2 * k)), (int(x + 288 * k), int(y + 23 * k)), (int(x + 257 * k), int(y + 43 * k))))
    polygon(screen, (0, 0, 0),
            ((int(x + 258 * k), int(y + 2 * k)), (int(x + 288 * k), int(y + 23 * k)), (int(x + 257 * k), int(y + 43 * k))),
            1)
    polygon(screen, (255, 192, 203),
            ((int(x + 262 * k), int(y + 7 * k)), (int(x + 283 * k), int(y + 22 * k)), (int(x + 260 * k), int(y + 40 * k))))
    return None


def clew_right(x ,y ,k):
    circle(screen, grey,  (x, y), int(50 * k), 0)
    circle(screen, (0, 0, 0), (x, y), int(50 * k), 1)
    arc(screen, (0, 0, 0), (x - 85 * k, y - 30 * k, 120 * k, 100 * k), 0, pi / 2, 1)
    arc(screen, (0, 0, 0), (x - 80 * k, y - 40 * k, 120 * k, 100 * k), 0, pi / 2, 1)
    arc(screen, (0, 0, 0), (x - 20 * k, y - 30 * k, 120 * k, 120 * k), 3 * pi/ 4,  pi , 1)
    arc(screen, (0, 0, 0), (x - 10 * k, y - 20 * k, 120 * k, 120 * k), 3 * pi / 4, pi, 1)
    arc(screen, (0, 0, 0), (x - 5 * k, y - 16 * k, 120 * k, 120 * k), 3 * pi / 4, pi, 1)
    return None


def clew_left(x ,y ,k):
    circle(screen, grey,  (x, y), int(50 * k), 0)
    circle(screen, (0, 0, 0), (x, y), int(50 * k), 1)
    arc(screen, (0, 0, 0), (x - 40 * k, y - 30 * k, 120 * k, 100 * k), pi / 2, pi, 1)
    arc(screen, (0, 0, 0), (x - 40 * k, y - 40 * k, 120 * k, 100 * k), pi / 2, pi,  1)
    arc(screen, (0, 0, 0), (x - 90 * k, y - 30 * k, 120 * k, 120 * k), 0,  pi / 4, 1)
    arc(screen, (0, 0, 0), (x - 95 * k, y - 20 * k, 120 * k, 120 * k), 0,  pi / 4, 1)
    arc(screen, (0, 0, 0), (x - 100 * k, y - 16 * k, 120 * k, 120 * k), 0,  pi / 4, 1)
    return None


background()
window(290, 10)
window(60, 10)
window(-170, 10)
cat_right(80, 420, 0.5, cat_colour2, eyes_colour2)
clew_left(350, 500, 0.8)
cat_right(430, 470, 0.18, cat_colour1, eyes_colour1)
clew_left(430, 440, 0.5)
cat_left(300, 300, 0.5, cat_colour1, eyes_colour1)
clew_right(180, 360, 0.5)
cat_right(60, 340, 0.2, cat_colour1, eyes_colour1)
clew_right(260, 600, 1.3)
cat_right(80, 650, 0.2, cat_colour2, eyes_colour2)
clew_right(140, 590, 0.5)
clew_left(450, 600, 0.8)
cat_left(340, 550, 0.2, cat_colour1, eyes_colour1)
clew_right(370, 650, 0.4)
cat_left(420, 650, 0.2, cat_colour2, eyes_colour2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()