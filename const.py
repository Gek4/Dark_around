import pygame

__all__ = (
    'width',
    'height',
    'screen',
    'clock',
    'background'
)

width, height = 1920, 1080
size = width, height
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load('data/background2.jpg'), (1920, 1080))
last_picture = 0
