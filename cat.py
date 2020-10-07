import pygame
from pygame.draw import *
from math import pi

pygame.init()
# Общие параметры
scale0 = 1
FPS = 30
screen_width = 500
screen_heigth = 700
screen = pygame.display.set_mode((screen_width, screen_heigth))
# Цвета
pink = (255, 192, 203)
black = (0, 0, 0)
back_up_colour = (184, 134, 60)
back_down_colour = (218, 165, 32)
big_window_colour = (240, 255, 255)
small_window_colour = (135, 206, 250)
cat_colour1 = (244, 164, 96)
cat_colour2 = (105, 105, 105)
eyes_colour1 = (60, 179, 113)
eyes_colour2 = (0, 0, 205)
grey = (192, 192, 192)
# Окна
# Размеры внешней рамы по x и y
x_window_r_0, y_window_r_0 = 200, 280
# Размеры малых(верхних) окон
x_window_s_0, y_window_s_0 = 80, 70
# Размеры больших(нижних) окон
x_window_b_0, y_window_b_0 = 80, 170
# Координаты окон
xw_1, yw_1 = 290, 10
xw_2, yw_2 = 60, 10
xw_3, yw_3 = -170, 10


def background():
    """
    Фунция рисует задний фон - 2 зоны, верхнюю и нижнюю
    """
    # Верхняя зона
    rect(screen, back_up_colour,
         (0, 0, screen_width, screen_heigth // 7 * 3), 0)
    # Нижняя зона
    rect(screen, back_down_colour,
         (0, screen_heigth // 7 * 3, screen_width, screen_heigth // 7 * 4), 0)


def window(x, y, x_window_r, y_window_r, x_window_s,
           y_window_s, x_window_b, y_window_b, scale):
    """
    функция рисует окно с заданным масштабом и верхним левым углом
    :param scale: масштаб относительно стандартного размера
    :param x: x-координата левого верхнего угла рамы
    :param y: y-координата левого верхнего угла рамы
    :param x_window_r: размер по x рамы
    :param y_window_r: размер по y рамы
    :param x_window_s: размер по x малых(верхних) окон
    :param y_window_s: размер по y малых(верхних) окон
    :param x_window_b: размер по x больших(нижних) окон
    :param y_window_b: размер по y больших(нижних) окон
    :param scale:
    :return:
    """
    # Внешняя рама окна
    rect(screen, big_window_colour,
         (x, y, x_window_r * scale, y_window_r * scale), 0)
    # левое верхнее малое окно
    rect(screen, small_window_colour,
         (x + x_window_r * scale // 20, y + y_window_r // 28,
          x_window_s, y_window_s), 0)
    # правое верхнее малое окно
    rect(screen, small_window_colour,
         (x + x_window_r * scale * 2 // 20 + x_window_s,
          y + y_window_r // 28, x_window_s, y_window_s), 0)
    # левое нижнее малое окно
    rect(screen, small_window_colour,
         (x + x_window_r * scale // 20, y + y_window_r * 3 // 28 + y_window_s,
          x_window_b, y_window_b), 0)
    # правое нижнее малое окно
    rect(screen, small_window_colour,
         (x + x_window_r * scale * 2 // 20 + x_window_s,
          y + y_window_r * 3 // 28 + y_window_s, x_window_b, y_window_b), 0)


def cat_left_tail(x, y, k, cat_colour):
    """
    функция рисует хвост кошки, смотрящей влево
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    ellipse(screen, cat_colour, (x + 250 * k, y + 45 * k, 200 * k, 50 * k))
    ellipse(screen, black, (x + 250 * k, y + 45 * k, 200 * k, 50 * k), 1)


def cat_left_body(x, y, k, cat_colour):
    """
    функция рисует тело кошки, смотрящей влево
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    ellipse(screen, cat_colour, (x, y, int(320 * k), int(160 * k)))
    ellipse(screen, black, (x, y, int(320 * k), int(160 * k)), 1)


def cat_left_back_leg(x, y, k, cat_colour):
    """
    функция рисует заднюю ногу кошки, смотрящей влево
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    circle(screen, cat_colour,
           (int(x + 270 * k), int(y + 130 * k)), int(50 * k), 0)
    circle(screen, black,
           (int(x + 270 * k), int(y + 130 * k)), int(50 * k), 1)
    ellipse(screen, cat_colour,
            (x + 290 * k, y + 130 * k, 50 * k, 100 * k), 0)
    ellipse(screen, black,
            (x + 290 * k, y + 130 * k, 50 * k, 100 * k), 1)


def cat_left_front_leg(x, y, k, cat_colour):
    """
    функция рисует переднюю ногу кошки, смотрящей влево
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    ellipse(screen, cat_colour, (x + 15 * k, y + 135 * k, 100 * k, 40 * k))
    ellipse(screen, black, (x + 15 * k, y + 135 * k, 100 * k, 40 * k), 1)
    ellipse(screen, cat_colour, (x - 30 * k, y + 65 * k, 50 * k, 100 * k))
    ellipse(screen, black, (x - 30 * k, y + 65 * k, 50 * k, 100 * k), 1)


def cat_left_head(x, y, k, cat_colour):
    """
    функция рисует голову кошки, смотрящей влево
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    circle(screen, cat_colour, (int(x + 10 * k), int(y + 75 * k)), int(70 * k))
    circle(screen, black, (int(x + 10 * k), int(y + 75 * k)), int(70 * k), 1)


def cat_left_eyes(x, y, k, eyes_colour):
    """
    функция рисует глаза кошки, смотрящей влево
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param eyes_colour: цвет глаз кошки
    :return:
    """
    circle(screen, eyes_colour,
           (int(x - 20 * k), int(y + 70 * k)), int(18 * k), 0)
    circle(screen, eyes_colour,
           (int(x + 40 * k), int(y + 70 * k)), int(18 * k), 0)
    circle(screen, black,
           (int(x - 20 * k), int(y + 70 * k)), int(18 * k), 1)
    circle(screen, black,
           (int(x + 40 * k), int(y + 70 * k)), int(18 * k), 1)
    ellipse(screen, black, (x - 18 * k, y + 58 * k, 8 * k, 25 * k))
    ellipse(screen, black, (x + 42 * k, y + 58 * k, 8 * k, 25 * k))


def cat_left_right_ear(x, y, k, cat_colour):
    """
    функция рисует правое ухо кошки, смотрящей влево
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    polygon(screen, cat_colour,
            ((int(x + 62 * k), int(y + 2 * k)),
             (int(x + 32 * k), int(y + 23 * k)),
             (int(x + 63 * k), int(y + 43 * k))))
    polygon(screen, black,
            ((int(x + 62 * k), int(y + 2 * k)),
             (int(x + 32 * k), int(y + 23 * k)),
             (int(x + 63 * k), int(y + 43 * k))), 1)
    polygon(screen, pink,
            ((int(x + 58 * k), int(y + 7 * k)),
             (int(x + 37 * k), int(y + 22 * k)),
             (int(x + 60 * k), int(y + 40 * k))))


def cat_left_left_ear(x, y, k, cat_colour):
    """
    функция рисует левое ухо кошки, смотрящей влево
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    polygon(screen, cat_colour,
            ((int(x - 52 * k), int(y + 2 * k)),
             (int(x - 22 * k), int(y + 23 * k)),
             (int(x - 53 * k), int(y + 43 * k))))
    polygon(screen, black,
            ((int(x - 52 * k), int(y + 2 * k)),
             (int(x - 22 * k), int(y + 23 * k)),
             (int(x - 53 * k), int(y + 43 * k))),
            1)
    polygon(screen, pink,
            ((int(x - 48 * k), int(y + 7 * k)),
             (int(x - 27 * k), int(y + 22 * k)),
             (int(x - 50 * k), int(y + 40 * k))))


def cat_left_nose(x, y, k):
    """
    функция рисует нос кошки смотрящей влево
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :return:
    """
    polygon(screen, pink,
            ((int(x + 10 * k), int(y + 100 * k)),
             (int(x + 1 * k), int(y + 95 * k)),
             (int(x + 19 * k), int(y + 95 * k))))
    polygon(screen, black,
            ((int(x + 10 * k), int(y + 100 * k)),
             (int(x + 1 * k), int(y + 95 * k)),
             (int(x + 19 * k), int(y + 95 * k))), 1)


def cat_left_mouth(x, y, k):
    """
    функция рисует нос кошки смотрящей влево
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :return:
    """
    arc(screen, black,
        (x + 10 * k, y + 80 * k, 40 * k, 40 * k), pi, 3 * pi / 2, 1)
    arc(screen, black,
        (x - 30 * k, y + 80 * k, 40 * k, 40 * k), 3 * pi / 2, 2 * pi, 1)


def cat_left_whiskers(x, y, k):
    """
    функция рисующая усы кошки смотрящей влево
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :return:
    """
    arc(screen, black,
        (x - 55 * k, y + 95 * k, 150 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, black,
        (x - 45 * k, y + 98 * k, 130 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, black,
        (x - 35 * k, y + 101 * k, 110 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, black,
        (x - 80 * k, y + 95 * k, 150 * k, 40 * k),  pi / 2, pi - 0.2, 1)
    arc(screen, black,
        (x - 70 * k, y + 98 * k, 130 * k, 40 * k), pi / 2, pi - 0.2, 1)
    arc(screen, black,
        (x - 60 * k, y + 101 * k, 110 * k, 40 * k), pi / 2, pi - 0.2, 1)


def cat_left(x, y, k, cat_colour, eyes_colour):
    """
    функция рисует кошку смотрящую влево на заданной позиции
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :param eyes_colour: цвет глаз кошки
    :return:
    """
    cat_left_tail(x, y, k, cat_colour)
    cat_left_body(x, y, k, cat_colour)
    cat_left_back_leg(x, y, k, cat_colour)
    cat_left_front_leg(x, y, k, cat_colour)
    cat_left_head(x, y, k, cat_colour)
    cat_left_eyes(x, y, k, eyes_colour)
    cat_left_right_ear(x, y, k, cat_colour)
    cat_left_left_ear(x, y, k, cat_colour)
    cat_left_nose(x, y, k)
    cat_left_mouth(x, y, k)
    cat_left_whiskers(x, y, k)


def cat_right_tail(x, y, k, cat_colour):
    """
    функция рисует хвост кошки смотрящей вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    ellipse(screen, cat_colour, (x - 100 * k, y + 45 * k, 200 * k, 50 * k))
    ellipse(screen, black, (x - 100 * k, y + 45 * k, 200 * k, 50 * k), 1)


def cat_right_body(x, y, k, cat_colour):
    """
    функция рисует тело кошки смотрящей вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    ellipse(screen, cat_colour, (x, y, int(320 * k), int(160 * k)))
    ellipse(screen, black, (x, y, int(320 * k), int(160 * k)), 1)


def cat_right_back_leg(x, y, k, cat_colour):
    """
    функция рисует заднюю ногу кошки смотрящей вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    circle(screen, cat_colour,
           (int(x + 50 * k), int(y + 130 * k)), int(50 * k), 0)
    circle(screen, black,
           (int(x + 50 * k), int(y + 130 * k)), int(50 * k), 1)
    ellipse(screen, cat_colour, (x - 10 * k, y + 130 * k, 50 * k, 100 * k), 0)
    ellipse(screen, black, (x - 10 * k, y + 130 * k, 50 * k, 100 * k), 1)


def cat_right_front_leg(x, y, k, cat_colour):
    """
    функция рисует переднюю ногу кошки смотрящей вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    ellipse(screen, cat_colour, (x + 210 * k, y + 135 * k, 100 * k, 40 * k))
    ellipse(screen, black, (x + 210 * k, y + 135 * k, 100 * k, 40 * k), 1)
    ellipse(screen, cat_colour, (x + 310 * k, y + 65 * k, 50 * k, 100 * k))
    ellipse(screen, black, (x + 310 * k, y + 65 * k, 50 * k, 100 * k), 1)


def cat_right_head(x, y, k, cat_colour):
    """
    функция рисует голову кошки смотрящей вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    circle(screen, cat_colour,
           (int(x + 320 * k), int(y + 75 * k)), int(70 * k))
    circle(screen, black,
           (int(x + 320 * k), int(y + 75 * k)), int(70 * k), 1)


def cat_right_eyes(x, y, k, eyes_colour):
    """
    функция рисует глаза кошки смотрящей вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param eyes_colour: цвет глаз кошки
    :return:
    """
    circle(screen, eyes_colour,
           (int(x + 350 * k), int(y + 70 * k)), int(18 * k), 0)
    circle(screen, eyes_colour,
           (int(x + 290 * k), int(y + 70 * k)), int(18 * k), 0)
    circle(screen, black,
           (int(x + 350 * k), int(y + 70 * k)), int(18 * k), 1)
    circle(screen, black,
           (int(x + 290 * k), int(y + 70 * k)), int(18 * k), 1)
    ellipse(screen, black, (x + 352 * k, y + 58 * k, 8 * k, 25 * k))
    ellipse(screen, black, (x + 292 * k, y + 58 * k, 8 * k, 25 * k))


def cat_right_nose(x, y, k):
    """
    функция рисует нос кошки смотрящей вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :return:
    """
    polygon(screen, pink,
            ((int(x + 320 * k), int(y + 100 * k)),
             (int(x + 311 * k), int(y + 95 * k)),
             (int(x + 329 * k), int(y + 95 * k))))
    polygon(screen, black,
            ((int(x + 320 * k), int(y + 100 * k)),
             (int(x + 311 * k), int(y + 95 * k)),
             (int(x + 329 * k), int(y + 95 * k))), 1)


def cat_right_mouth(x, y, k):
    """
    функция рисует рот кошки смотрящей вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :return:
    """
    arc(screen, black,
        (x + 320 * k, y + 80 * k, 40 * k, 40 * k), pi, 3 * pi / 2, 1)
    arc(screen, black,
        (x + 280 * k, y + 80 * k, 40 * k, 40 * k), 3 * pi / 2, 2 * pi, 1)


def cat_right_whiskers(x, y, k):
    """
    функция рисует усы кошки смотрящей вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :return:
    """
    arc(screen, black,
        (x + 255 * k, y + 95 * k, 150 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, black,
        (x + 265 * k, y + 98 * k, 130 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, black,
        (x + 275 * k, y + 101 * k, 110 * k, 40 * k), 0.2, pi / 2, 1)
    arc(screen, black,
        (x + 230 * k, y + 95 * k, 150 * k, 40 * k), pi / 2, pi - 0.2, 1)
    arc(screen, black,
        (x + 240 * k, y + 98 * k, 130 * k, 40 * k), pi / 2, pi - 0.2, 1)
    arc(screen, black,
        (x + 250 * k, y + 101 * k, 110 * k, 40 * k), pi / 2, pi - 0.2, 1)


def cat_right_right_ear(x, y, k, cat_colour):
    """
    функция рисует правое ухо кошки смотрящей вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    polygon(screen, cat_colour,
            ((int(x + 372 * k), int(y + 2 * k)),
             (int(x + 342 * k), int(y + 23 * k)),
             (int(x + 373 * k), int(y + 43 * k))))
    polygon(screen, black,
            ((int(x + 372 * k), int(y + 2 * k)),
             (int(x + 342 * k), int(y + 23 * k)),
             (int(x + 373 * k), int(y + 43 * k))), 1)
    polygon(screen, pink,
            ((int(x + 368 * k), int(y + 7 * k)),
             (int(x + 347 * k), int(y + 22 * k)),
             (int(x + 370 * k), int(y + 40 * k))))


def cat_right_left_ear(x, y, k, cat_colour):
    """
    Функция рисует левое ухо кошки смотрящей вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :return:
    """
    polygon(screen, cat_colour,
            ((int(x + 258 * k), int(y + 2 * k)),
             (int(x + 288 * k), int(y + 23 * k)),
             (int(x + 257 * k), int(y + 43 * k))))
    polygon(screen, black,
            ((int(x + 258 * k), int(y + 2 * k)),
             (int(x + 288 * k), int(y + 23 * k)),
             (int(x + 257 * k), int(y + 43 * k))),
            1)
    polygon(screen, pink,
            ((int(x + 262 * k), int(y + 7 * k)),
             (int(x + 283 * k), int(y + 22 * k)),
             (int(x + 260 * k), int(y + 40 * k))))


def cat_right(x, y, k, cat_colour, eyes_colour):
    """
    функция рисует кошку смотрящую вправо
    :param x: x-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param y: y-координата верхнего левого угла прямоугольника,
    содержащего тело кошки
    :param k: масштаб
    :param cat_colour: цвет кошки
    :param eyes_colour: цвет глаз кошки
    :return:
    """
    cat_right_tail(x, y, k, cat_colour)
    cat_right_body(x, y, k, cat_colour)
    cat_right_back_leg(x, y, k, cat_colour)
    cat_right_front_leg(x, y, k, cat_colour)
    cat_right_head(x, y, k, cat_colour)
    cat_right_eyes(x, y, k, eyes_colour)
    cat_right_nose(x, y, k)
    cat_right_mouth(x, y, k)
    cat_right_whiskers(x, y, k)
    cat_right_right_ear(x, y, k, cat_colour)
    cat_right_left_ear(x, y, k, cat_colour)


def clew_right(x, y, k):
    """
    функция рисует клубок, ориентированный в правую сторону,
    заданного масштаба
    :param x: x-координата центра клубка
    :param y: y-координата центра клубка
    :param k: масштаб
    :return:
    """
    circle(screen, grey,  (x, y), int(50 * k), 0)
    circle(screen, black, (x, y), int(50 * k), 1)
    arc(screen, black,
        (x - 85 * k, y - 30 * k, 120 * k, 100 * k), 0, pi / 2, 1)
    arc(screen, black,
        (x - 80 * k, y - 40 * k, 120 * k, 100 * k), 0, pi / 2, 1)
    arc(screen, black,
        (x - 20 * k, y - 30 * k, 120 * k, 120 * k), 3 * pi / 4,  pi, 1)
    arc(screen, black,
        (x - 10 * k, y - 20 * k, 120 * k, 120 * k), 3 * pi / 4, pi, 1)
    arc(screen, black,
        (x - 5 * k, y - 16 * k, 120 * k, 120 * k), 3 * pi / 4, pi, 1)


def clew_left(x, y, k):
    """
    функция рисует клубок, ориентированный в левую сторону,
    заданного масштаба
    :param x: x-координата центра клубка
    :param y: y-координата центра клубка
    :param k: масштаб
    :return:
    """
    circle(screen, grey,  (x, y), int(50 * k), 0)
    circle(screen, black, (x, y), int(50 * k), 1)
    arc(screen, black,
        (x - 40 * k, y - 30 * k, 120 * k, 100 * k), pi / 2, pi, 1)
    arc(screen, black,
        (x - 40 * k, y - 40 * k, 120 * k, 100 * k), pi / 2, pi,  1)
    arc(screen, black,
        (x - 90 * k, y - 30 * k, 120 * k, 120 * k), 0,  pi / 4, 1)
    arc(screen, black,
        (x - 95 * k, y - 20 * k, 120 * k, 120 * k), 0,  pi / 4, 1)
    arc(screen, black,
        (x - 100 * k, y - 16 * k, 120 * k, 120 * k), 0,  pi / 4, 1)


# Основная программа
background()
window(xw_1, yw_1, x_window_r_0, y_window_r_0, x_window_s_0,
       y_window_s_0, x_window_b_0, y_window_b_0, scale0)
window(xw_2, yw_2, x_window_r_0, y_window_r_0, x_window_s_0,
       y_window_s_0, x_window_b_0, y_window_b_0, scale0)
window(xw_3, yw_3, x_window_r_0, y_window_r_0, x_window_s_0,
       y_window_s_0, x_window_b_0, y_window_b_0, scale0)
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
