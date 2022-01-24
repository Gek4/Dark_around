import pygame
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
zombie = pygame.sprite.Group()
player = pygame.sprite.Group()
zombie_player = pygame.sprite.Group()


class ZombieLook(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, zombie_player)
        radius = 30
        self.look = False
        self.parent = None
        self.player = None
        self.track = False
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)

    def update(self):
        self.look = self.track or self.look
        self.track = pygame.sprite.spritecollideany(self, player) and not self.look
        self.follow()
        if self.track:
            self.player = pygame.sprite.spritecollide(self, player, False)[0]
            coord = pygame.sprite.spritecollide(self, player, False)[0].being_tracked()
            self.parent = pygame.sprite.spritecollide(self, zombie, False)[0]
            pygame.sprite.spritecollide(self, zombie, False)[0].being_tracked()
            pygame.sprite.spritecollide(self, zombie, False)[0].get_coord(coord)

    def follow(self):
        if self.look:
            coord = self.player.being_tracked()
            self.parent.get_coord(coord)


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, zombie)
        radius = 5
        self.vision = ZombieLook(x - 10, y - 10)
        self.coord = []
        self.index = "undefined"
        self.x = x
        self.y = y
        self.tracked = False
        self.vx = 0
        self.vy = 0
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("green"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)

    def update(self):
        self.vision.update()
        if self.tracked:
            x, y = self.coord[self.index]
            if self.x != x or self.y != y:
                self.rect = self.rect.move(x - self.x, y - self.y)
            else:
                while self.x == x and self.y == y:
                    self.index += 1
                    if not self.index >= len(self.coord):
                        x, y = self.coord[self.index]
                    else:
                        break
                self.rect = self.rect.move(x - self.x, y - self.y)
            self.x = x
            self.y = y

    def being_tracked(self):
        self.tracked = True

    def get_coord(self, coord):
        self.coord = coord
        if self.index == "undefined":
            self.index = len(self.coord) - 1
        else:
            self.index += 1


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, player, zombie_player)
        radius = 5
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.tracked = False
        self.record = []
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)

    def update(self, vx, xy):
        self.vx = vx
        self.vy = vy
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = 0
            self.rect = self.rect.move(0, -4)
            if pygame.sprite.spritecollideany(self, horizontal_borders):
                self.rect = self.rect.move(0, 8)
            self.vy = 0
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = 0
            self.rect = self.rect.move(-4, 0)
            if pygame.sprite.spritecollideany(self, vertical_borders):
                self.rect = self.rect.move(8, 0)
            self.vx = 0
        self.x = self.rect.x
        self.y = self.rect.y
        if self.tracked:
            self.record.append((self.x, self.y))
        self.rect = self.rect.move(self.vx, self.vy)

    def being_tracked(self):
        self.tracked = True
        if not self.record:
            self.record = [(self.x, self.y)]
        return self.record


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([10, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 10, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 10])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 10)


Border(25, 25, width - 25, 25)
Border(25, height - 25, width - 25, height - 25)
Border(25, 25, 25, height - 25)
Border(width - 25, 25, width - 25, height - 25)
Border(100, 150, 250, 150)
Border(250, 150, 250, 300)
Border(650, 150, 650, 350)
Border(300, 450, 600, 450)
main_character = Player(100, 100)
Zombie(200, 300)
running = True
t = 0
zombie_go = True
death_per_tick = []
while running:
    if not all(death_per_tick) or len(death_per_tick) == 0:
        screen.fill((160, 160, 160))
        rect = pygame.Rect(25, 25, width - 50, height - 50)
        pygame.draw.rect(screen, (200, 200, 200), rect)
        pygame.draw.rect(screen, (100, 150, 250),
                         (23, 23, width - 45, height - 45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        t += clock.tick()

        if t >= 16:
            vx = 0
            vy = 0
            if pygame.key.get_pressed()[pygame.K_w]:
                vy = -4
            if pygame.key.get_pressed()[pygame.K_s]:
                vy = 4
            if pygame.key.get_pressed()[pygame.K_a]:
                vx = -4
            if pygame.key.get_pressed()[pygame.K_d]:
                vx = 4
            death_per_tick.append(pygame.sprite.spritecollideany(main_character, zombie) != None)
            zombie_go = not zombie_go
            all_sprites.draw(screen)
            player.update(vx, vy)
            if zombie_go:
                zombie.update()
            pygame.display.flip()
            if len(death_per_tick) > 4:
                death_per_tick = death_per_tick[-5:]
            print(death_per_tick)
            t = 0
    else:
        running = False
        pygame.display.flip()
