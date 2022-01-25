import pygame
from const import width, height
from models import Border_constructor, Zombie, Player


def start():
    data = [
        ((25, 25), (width - 25, 25)),
        ((25, height - 25), (width - 25, height - 25)),
        ((25, 25), (25, height - 25)),
        ((width - 25, 25), (width - 25, height - 25)),
        ((100, 150), (250, 150)),
        ((250, 150), (250, 300)),
        ((650, 150), (650, 350)),
        ((300, 450), (600, 450))
    ]

    border = Border_constructor(data)
    player = Player(border, 100, 100)
    zombie = Zombie(border.all_sprites, player, 200, 300)
    return border, player, zombie
