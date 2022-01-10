import pygame
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
zombie_player = pygame.sprite.Group()
swat_player = pygame.sprite.Group()
swat_zombie = pygame.sprite.Group()
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, zombie_player, swat_player)
        radius = 5
        self.vx = 0
        self.vy = 0
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)

    def update(self, t):
        if pygame.key.get_pressed()[pygame.K_w]:
            self.vy = -1
            self.vx = 0
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.vy = 1
            self.vx = 0
        elif pygame.key.get_pressed()[pygame.K_a]:
            self.vx = -1
            self.vy = 0
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.vx = 1
            self.vy = 0
        else:
            self.vx = 0
            self.vy = 0
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = 0
            self.rect = self.rect.move(0, -1)
            if pygame.sprite.spritecollideany(self, horizontal_borders):
                self.rect = self.rect.move(0, 2)
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = 0
            self.rect = self.rect.move(-1, 0)
            if pygame.sprite.spritecollideany(self, vertical_borders):
                self.rect = self.rect.move(2, 0)
        self.rect = self.rect.move(self.vx, self.vy)


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites, zombie_player)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([3, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 3])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


Border(25, 25, width - 25, 25)
Border(25, height - 25, width - 25, height - 25)
Border(25, 25, 25, height - 25)
Border(width - 25, 25, width - 25, height - 25)
Border(100, 150, 250, 150)
Border(250, 150, 250, 300)
Border(650, 150, 650, 350)
Border(300, 450, 600, 450)
Player(100, 100)
running = True
t = 0
while running:

    screen.fill((160, 160, 160))
    rect = pygame.Rect(25, 25, width - 50, height - 50)
    pygame.draw.rect(screen, (200, 200, 200), rect)
    pygame.draw.rect(screen, (100, 150, 250),
                     (23, 23, width - 45, height - 45), 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t += clock.tick()
    if t >= 4:
        all_sprites.draw(screen)
        all_sprites.update(t)
        pygame.display.flip()
        t = 0
