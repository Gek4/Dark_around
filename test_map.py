import pygame
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

Border(25, 25, width - 25, 25)
Border(25, height - 25, width - 25, height - 25)
Border(25, 25, 25, height - 25)
Border(width - 25, 25, width - 25, height - 25)
Border(100, 150, 250, 150)
Border(250, 150, 250, 300)
Border(650, 150, 650, 350)
Border(300, 450, 600, 450)
running = True
while running:
    screen.fill((160, 160, 160))
    rect = pygame.Rect(25, 25, width - 50, height - 50)
    pygame.draw.rect(screen, (200, 200, 200), rect)
    pygame.draw.rect(screen, (100, 150, 250),
                     (23, 23, width - 45, height - 45), 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.draw(screen)
    pygame.display.flip()
