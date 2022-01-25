import pygame

__all__ = (
    'width',
    'height',
    'screen',
    'clock'
)

width, height = 1600, 900
size = width, height
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
