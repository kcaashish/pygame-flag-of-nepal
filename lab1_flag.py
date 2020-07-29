# importing required libraries
import math
import pygame
from pygame import event
from pygame.locals import *

# initializing pygame
pygame.init()

display_info = pygame.display.Info()
width = display_info.current_w
height = display_info.current_h
print("------------------------------------------")
print("The screen resolution is {}p X {}p.".format(width, height))
print("------------------------------------------")

# starting a new window
window = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Lab 1 - Flag")

RED = Color("#C8102E")
CRIMSON = Color("#DC143C")
DARK_BLUE = Color("#003893")
BLUE = Color("#003087")
WHITE = Color("#FFFFFF")
BLACK = Color("#000000")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        # close when [X] is pressed
        if event.type == pygame.QUIT:
            running = False
        # close when ESC is pressed
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # fill the window with a colour, here white
    window.fill(WHITE)

    """
    Following  Constitution of Nepal:
    Schedule-1 National Flag of Nepal
    C (100, 100)
    D (100, 200)
    F (100, 300)    E (200, 300)    G(400, 300)

    A (100, 500)                    B (400, 500)
    """

    bod = 12

    # upper outer triangle
    pygame.draw.polygon(
        window,
        DARK_BLUE,
        [
            (100 - bod, 100 - 2 * bod),
            (100 - bod, 300 + bod),
            (400 + 3 * bod, 300 + bod),
        ],
    )

    # lower outer triangle
    pygame.draw.polygon(
        window,
        DARK_BLUE,
        [
            (100 - bod, 200 - 2 * bod - 5),
            (100 - bod, 500 + bod),
            (400 + 2 * bod + 5, 500 + bod),
        ],
    )

    # upper inner triangle
    pygame.draw.polygon(window, CRIMSON, [(100, 100), (100, 300), (400, 300)])

    # lower inner triangle
    pygame.draw.polygon(window, CRIMSON, [(100, 200), (100, 500), (400, 500)])

    # drawing the sun
    num_points = 12
    point_list = []
    center_x = 175
    center_y = 400
    for i in range(num_points * 2):
        radius = 60
        if i % 2 != 0:
            radius = radius // 1.5
        ang = i * 3.14159 / num_points
        x = center_x + int(math.cos(ang) * radius)
        y = center_y + int(math.sin(ang) * radius)
        point_list.append((x, y))

    pygame.draw.polygon(window, WHITE, point_list)

    """
    L (175, 200)
    M (175, 220)
    N (175, 260)
    """
    # drawing the moon
    pygame.draw.circle(window, WHITE, (175, 234), 60)
    pygame.draw.circle(window, CRIMSON, (175, 220), 58)
    num_points = 16
    point_list = []
    center_x = 175
    center_y = 260
    for i in range(num_points * 2):
        radius = 40
        if i % 2 == 0:
            radius = radius // 1.3
        ang = i * 3.14159 / num_points
        x = center_x + int(math.cos(ang) * radius)
        y = center_y + int(math.sin(ang) * radius)
        point_list.append((x, y))

    del point_list[5:13]
    pygame.draw.polygon(window, WHITE, point_list)

    font = pygame.font.SysFont("arial", 28)
    font_2 = pygame.font.SysFont("helvetiva", 18)
    text = font.render("National Flag of Nepal", True, BLACK)
    name = font_2.render("Aashish KC", True, BLACK)
    window.blit(text, (90, 520))
    window.blit(name, (420, 580))
    pygame.display.update()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
