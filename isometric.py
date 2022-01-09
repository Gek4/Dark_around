import pygame
import sys
import time
from pygame.locals import *

pygame.init()
pygame.display.set_caption('probable map')
screen = pygame.display.set_mode((900, 900), 0, 32)
display = pygame.Surface((300, 300))

floor_img = pygame.image.load('grass.png').convert()
floor_img.set_colorkey((0, 0, 0))

top_wall_img = pygame.image.load('front_wall.png').convert()
top_wall_img.set_colorkey((0, 0, 0))

left_wall_img = pygame.image.load('left_wall.png').convert()
left_wall_img.set_colorkey((0, 0, 0))

topleft_wall_img = pygame.image.load('frontleft_wall.png').convert()
topleft_wall_img.set_colorkey((0, 0, 0))

wall_23_img = pygame.image.load('experemental_wall.png').convert()
wall_23_img.set_colorkey((0, 0, 0))

wall_32_img = pygame.image.load('experemental_wall_2.png').convert()
wall_32_img.set_colorkey((0, 0, 0))

f = open('map1.txt')
map_data = [[int(i) for i in row] for row in f.read().split('\n')]
f.close()

while True:
    display.fill((0, 0, 0))

    for y, row in enumerate(map_data):
        print(y, row)
        for x, tile in enumerate(row):
            print(x, tile)
            if tile == 1:
                display.blit(floor_img, (80 + x * 10 - y * 10, 100 + x * 5 + y * 5))
            elif tile == 2:
                display.blit(top_wall_img, (80 + x * 10 - y * 10, 86 + x * 5 + y * 5))
            elif tile == 3:
                display.blit(left_wall_img, (80 + x * 10 - y * 10, 86 + x * 5 + y * 5))
            elif tile == 4:
                display.blit(topleft_wall_img, (80 + x * 10 - y * 10, 86 + x * 5 + y * 5))
            elif tile == 5:
                display.blit(wall_23_img, (80 + x * 10 - y * 10, 86 + x * 5 + y * 5))
            elif tile == 6:
                display.blit(wall_32_img, (80 + x * 10 - y * 10, 86 + x * 5 + y * 5))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    time.sleep(5)
