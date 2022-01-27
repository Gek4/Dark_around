import pygame

__all__ = (
    'width',
    'height',
    'screen',
    'clock',
    'background',
    'wall',
    'character_stay',
    'character_walk_right',
    'character_walk_left',
    'character_walk_front',
    'character_walk_back',
    'character_walk',
    'character_walk_new',
    'image_player',
    'zombie_stay',
    'zombie_walk_right',
    'zombie_walk_left',
    'zombie_walk_front',
    'zombie_walk_back',
    'zombie_walk',
    'zombie_walk_new',
    'image_zombie'
)

width, height = 1920, 1080
size = width, height
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load('data/background2.jpg'), (1920, 1080))
wall = pygame.transform.scale(pygame.image.load('data/beton2.jpg'), (1920, 1080))

# load character images for animation
character_stay = pygame.image.load('data/main_character/player_stay.png')
character_stay = pygame.transform.scale(character_stay, (35, 65))
character_stay.set_colorkey([255, 255, 255])

character_walk_front = [
    pygame.image.load('data/main_character/walk_front/walk_front1.png'),
    pygame.image.load('data/main_character/walk_front/walk_front2.png'),
    pygame.image.load('data/main_character/walk_front/walk_front3.png'),
    pygame.image.load('data/main_character/walk_front/walk_front4.png'),
    pygame.image.load('data/main_character/walk_front/walk_front5.png'),
    pygame.image.load('data/main_character/walk_front/walk_front6.png'),
    pygame.image.load('data/main_character/walk_front/walk_front7.png'),
    pygame.image.load('data/main_character/walk_front/walk_front8.png'),
    pygame.image.load('data/main_character/walk_front/walk_front9.png')
]

character_walk_left = [
    pygame.image.load('data/main_character/walk_left/walk_left1.png'),
    pygame.image.load('data/main_character/walk_left/walk_left2.png'),
    pygame.image.load('data/main_character/walk_left/walk_left3.png'),
    pygame.image.load('data/main_character/walk_left/walk_left4.png'),
    pygame.image.load('data/main_character/walk_left/walk_left5.png'),
    pygame.image.load('data/main_character/walk_left/walk_left6.png'),
    pygame.image.load('data/main_character/walk_left/walk_left7.png'),
    pygame.image.load('data/main_character/walk_left/walk_left8.png'),
    pygame.image.load('data/main_character/walk_left/walk_left9.png')
]

character_walk_back = [
    pygame.image.load('data/main_character/walk_back/walk_back1.png'),
    pygame.image.load('data/main_character/walk_back/walk_back2.png'),
    pygame.image.load('data/main_character/walk_back/walk_back3.png'),
    pygame.image.load('data/main_character/walk_back/walk_back4.png'),
    pygame.image.load('data/main_character/walk_back/walk_back5.png'),
    pygame.image.load('data/main_character/walk_back/walk_back6.png'),
    pygame.image.load('data/main_character/walk_back/walk_back7.png'),
    pygame.image.load('data/main_character/walk_back/walk_back8.png'),
    pygame.image.load('data/main_character/walk_back/walk_back9.png')
]

character_walk_right = [
    pygame.image.load('data/main_character/walk_right/walk_right1.png'),
    pygame.image.load('data/main_character/walk_right/walk_right2.png'),
    pygame.image.load('data/main_character/walk_right/walk_right3.png'),
    pygame.image.load('data/main_character/walk_right/walk_right4.png'),
    pygame.image.load('data/main_character/walk_right/walk_right5.png'),
    pygame.image.load('data/main_character/walk_right/walk_right6.png'),
    pygame.image.load('data/main_character/walk_right/walk_right7.png'),
    pygame.image.load('data/main_character/walk_right/walk_right8.png'),
    pygame.image.load('data/main_character/walk_right/walk_right9.png')
]
character_walk = [character_walk_front, character_walk_back, character_walk_left, character_walk_right]
character_walk_new = [[], [], [], []]
for i in range(4):
    for j in range(9):
        image_player = character_walk[i][j]
        image_player = pygame.transform.scale(image_player, (35, 65))
        image_player.set_colorkey([255, 255, 255])
        character_walk_new[i].append(image_player)
character_walk_front, character_walk_back, character_walk_left, character_walk_right = character_walk_new

# load images for animation zombie

zombie_stay = pygame.image.load('data/zombus/zombie_stay.png')
zombie_stay = pygame.transform.scale(zombie_stay, (35, 65))
zombie_stay.set_colorkey([255, 255, 255])

zombie_walk_front = [
    pygame.image.load('data/zombus/walk_front/walk_front1.png'),
    pygame.image.load('data/zombus/walk_front/walk_front2.png'),
    pygame.image.load('data/zombus/walk_front/walk_front3.png'),
    pygame.image.load('data/zombus/walk_front/walk_front4.png'),
    pygame.image.load('data/zombus/walk_front/walk_front5.png'),
    pygame.image.load('data/zombus/walk_front/walk_front6.png'),
    pygame.image.load('data/zombus/walk_front/walk_front7.png')
]

zombie_walk_back = [
    pygame.image.load('data/zombus/walk_back/walk_back1.png'),
    pygame.image.load('data/zombus/walk_back/walk_back2.png'),
    pygame.image.load('data/zombus/walk_back/walk_back3.png'),
    pygame.image.load('data/zombus/walk_back/walk_back4.png'),
    pygame.image.load('data/zombus/walk_back/walk_back5.png'),
    pygame.image.load('data/zombus/walk_back/walk_back6.png'),
    pygame.image.load('data/zombus/walk_back/walk_back7.png'),
]

zombie_walk_left = [
    pygame.image.load('data/zombus/walk_left/walk_left1.png'),
    pygame.image.load('data/zombus/walk_left/walk_left2.png'),
    pygame.image.load('data/zombus/walk_left/walk_left3.png'),
    pygame.image.load('data/zombus/walk_left/walk_left4.png'),
    pygame.image.load('data/zombus/walk_left/walk_left5.png'),
    pygame.image.load('data/zombus/walk_left/walk_left6.png'),
    pygame.image.load('data/zombus/walk_left/walk_left7.png')
]

zombie_walk_right = [
    pygame.image.load('data/zombus/walk_right/walk_right1.png'),
    pygame.image.load('data/zombus/walk_right/walk_right2.png'),
    pygame.image.load('data/zombus/walk_right/walk_right3.png'),
    pygame.image.load('data/zombus/walk_right/walk_right4.png'),
    pygame.image.load('data/zombus/walk_right/walk_right5.png'),
    pygame.image.load('data/zombus/walk_right/walk_right6.png'),
    pygame.image.load('data/zombus/walk_right/walk_right7.png')
]
zombie_walk = [zombie_walk_front, zombie_walk_back, zombie_walk_left, zombie_walk_right]
zombie_walk_new = [[], [], [], []]
for i in range(4):
    for j in range(7):
        image_zombie = zombie_walk[i][j]
        image_zombie = pygame.transform.scale(image_zombie, (35, 65))
        image_zombie.set_colorkey([255, 255, 255])
        character_walk_new[i].append(image_zombie)
zombie_walk_front, zombie_walk_back, zombie_walk_left, zombie_walk_right = zombie_walk_new
