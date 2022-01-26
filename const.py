import pygame

__all__ = (
    'width',
    'height',
    'screen',
    'clock',
    'background'
)

width, height = 1600, 900
size = width, height
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load('data/background2.jpg'), (1600, 900))
last_picture = 0