import pygame

__all__ = (
    'width',
    'height',
    'screen',
    'clock'
)

width, height = 800, 600
size = width, height
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
