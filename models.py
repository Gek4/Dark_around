import pygame

__all__ = (
    'ZombieLook',
    'Zombie',
    'Player',
    'Border_constructor',
    'Border',
    'graphics'
)


class ZombieLook(pygame.sprite.Sprite):
    def __init__(self, all_sprites, parent, player, x, y):
        super().__init__(all_sprites)
        radius = 30
        self.look = False
        self.parent = parent
        self.player = player
        self.track = False
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)

    def update(self):
        self.look = self.track or self.look
        self.track = pygame.sprite.spritecollideany(self, self.player.get_group) and not self.look
        self.follow()
        if self.track:
            coord = self.player.being_tracked()
            self.parent.being_tracked()
            self.parent.get_coord(coord)

    def follow(self):
        if self.look:
            coord = self.player.being_tracked()
            self.parent.get_coord(coord)

    @property
    def _get_group(self):
        return self.groups()[1]


class Zombie(pygame.sprite.Sprite):
    def __init__(self, all_sprites, player, x, y):
        super().__init__(all_sprites, pygame.sprite.Group())
        radius = 5
        self.vision = ZombieLook(all_sprites, self, player, x - 10, y - 10)
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
        self.rect = pygame.Rect(x, y, 35, 65)

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

    @property
    def get_group(self):
        return self.groups()[1]

    @property
    def get_cords(self):
        return self.x, self.y


class Player(pygame.sprite.Sprite):
    def __init__(self, border, x, y):
        super().__init__(border.all_sprites, pygame.sprite.Group())
        radius = 5
        self.border = border
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
        self.rect = pygame.Rect(x, y, 35, 65)

    def update(self, vx, vy):
        self.vx = vx
        self.vy = vy
        if pygame.sprite.spritecollideany(self, self.border.horizontal_borders):
            self.vy = 0
            self.rect = self.rect.move(0, -4)
            if pygame.sprite.spritecollideany(self, self.border.horizontal_borders):
                self.rect = self.rect.move(0, 8)
            self.vy = 0
        if pygame.sprite.spritecollideany(self, self.border.vertical_borders):
            self.vx = 0
            self.rect = self.rect.move(-4, 0)
            if pygame.sprite.spritecollideany(self, self.border.vertical_borders):
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

    @property
    def get_group(self):
        return self.groups()[1]

    @property
    def get_cords(self):
        return self.x, self.y


class Border_constructor(pygame.sprite.Sprite):
    def __init__(self, data):
        # all_sprites, vertical_borders, horizontal_borders
        super().__init__(pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group())
        for p in data:
            p1, p2 = p
            x1, y1 = p1
            x2, y2 = p2
            Border(x1, y1, x2, y2, self)
            self.image = pygame.Surface([1, 1])
            self.rect = pygame.Rect(1, 1, 1, 1)

    @property
    def all_sprites(self):
        return self.groups()[0]

    @property
    def vertical_borders(self):
        return self.groups()[1]

    @property
    def horizontal_borders(self):
        return self.groups()[2]


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, parent):
        super().__init__(parent.all_sprites)
        if x1 == x2:
            self.add(parent.vertical_borders)
            self.image = pygame.Surface([10, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 10, y2 - y1)
        else:
            self.add(parent.horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 10])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 10)


def graphics_character():
    _sprite_sheet = pygame.image.load('../Dark_around/data/1_1.png')
    image_player = _sprite_sheet.subsurface([12, 3, 23, 43])
    image_player = pygame.transform.scale(image_player, (35, 65))
    image_player.set_colorkey([255, 255, 255])
    return image_player


def graphics_zombie():
    _sprite_sheet = pygame.image.load('../Dark_around/data/zombus.png')
    image_zombie = _sprite_sheet.subsurface([13, 4, 22, 43])
    image_zombie = pygame.transform.scale(image_zombie, (35, 65))
    image_zombie.set_colorkey([255, 255, 255])
    return image_zombie
