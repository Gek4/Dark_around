import pygame
from const import screen

__all__ = (
    'ZombieLook',
    'Zombie',
    'Player',
    'Border_constructor',
    'Border',
    'graphics_zombie',
    '_timer'
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


class Swat(pygame.sprite.Sprite):
    def __init__(self, h_borders, v_borders, all_sprites, player, x, y, coords):
        super().__init__(all_sprites, pygame.sprite.Group())
        radius = 5
        self.w = 50
        self.h = 50
        self.l = 200
        # переменные сверху отвечают за длину и ширину бойца
        self.vision = SwatLook(h_borders, v_borders, self, player)
        self.coords = coords
        self.index = 0
        self.rotate = 2
        self.death = True
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("blue"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 50, 50)

    def update(self):
        self.death = self.vision.update()
        self.vx = self.vy = 0
        if self.x == self.coords[(self.index + 1) % len(self.coords)][0] and self.y == \
                self.coords[(self.index + 1) % len(self.coords)][1]:
            self.index += 1
        if self.coords[self.index % len(self.coords)][0] > self.coords[(self.index + 1) % len(self.coords)][0]:
            self.vx = -1
            self.rotate = 3
        elif self.coords[self.index % len(self.coords)][0] < self.coords[(self.index + 1) % len(self.coords)][0]:
            self.vx = 1
            self.rotate = 1
        elif self.coords[self.index % len(self.coords)][1] < self.coords[(self.index + 1) % len(self.coords)][1]:
            self.vy = 1
            self.rotate = 0
        else:
            self.vy = -1
            self.rotate = 2
        self.x += self.vx
        self.y += self.vy
        self.rect = self.rect.move(self.vx, self.vy)

    @property
    def get_group(self):
        return self.groups()[1]

    @property
    def get_rotate(self):
        return self.rotate

    @property
    def alive(self):
        return self.death

    @property
    def get_vision(self):
        return self.vision

    @property
    def get_size(self):
        return self.w, self.h, self.l

    @property
    def get_cords(self):
        return self.x, self.y


class SwatLook(pygame.sprite.Sprite):
    def __init__(self, h_borders, v_borders, parent, player):
        super().__init__()
        self.h_borders = h_borders
        self.v_borders = v_borders
        self.parent = parent
        self.player = player

    def update(self):
        x1, y1 = self.parent.get_cords
        x2, y2 = self.player.get_cords
        w, h, l = self.parent.get_size
        if self.parent.get_rotate == 0:
            self.rect = pygame.Rect(x1, y1, w, l)

            if x1 <= x2 <= x1 + w and y1 <= y2 <= y1 + l and pygame.Rect.collidelist(self.rect, [i.rect for i in
                                                                                                 self.h_borders]) == -1:
                return False
            elif pygame.Rect.collidelist(self.rect, [i.rect for i in self.h_borders]) != -1:
                if x1 <= x2 <= x1 + w and y1 <= y2 <= y1 + l and y2 < self.h_borders[pygame.Rect.collidelist(self.rect, [i.rect for i in self.h_borders])].get_cords_h:
                    return False
        elif self.parent.get_rotate == 2:
            self.rect = pygame.Rect(x1, y1 - l, w, l)
            if x1 <= x2 <= x1 + w and y1 - l <= y2 <= y1 and pygame.Rect.collidelist(self.rect, [i.rect for i in self.h_borders]) == -1:
                return False
            elif pygame.Rect.collidelist(self.rect, [i.rect for i in self.h_borders]) != -1:
                if x1 <= x2 <= x1 + w and y1 - l <= y2 <= y1 and y2 < self.h_borders[pygame.Rect.collidelist(self.rect, [i.rect for i in self.h_borders])].get_cords_h:
                    return False

        elif self.parent.get_rotate == 1:
            self.rect = pygame.Rect(x1, y1, l, h)
            if x1 <= x2 <= x1 + l and y1 <= y2 <= y1 + h:
                return False

        else:
            self.rect = pygame.Rect(x1 - l, y1, l, h)
            if x1 - l <= x2 <= x1 and y1 <= y2 <= y1 + h:
                return False
        return True

    @property
    def _get_group(self):
        return self.groups()[1]


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
        self.rect = pygame.Rect(x, y, 32, 65)

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
            self.x = x1
        else:
            self.add(parent.horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 10])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 10)
            self.y = y1

    @property
    def get_cords_h(self):
        return self.y

    @property
    def get_cords_v(self):
        return self.x


def graphics_zombie():
    _sprite_sheet = pygame.image.load('data/zombus.png')
    image_zombie = _sprite_sheet.subsurface([13, 4, 22, 43])
    image_zombie = pygame.transform.scale(image_zombie, (35, 65))
    image_zombie.set_colorkey([255, 255, 255])
    return image_zombie


def _timer(timer_seconds):
    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    timer_seconds /= 62.5
    timer_seconds = int(timer_seconds)
    if timer_seconds < 60:
        label = myfont.render(f"Time : {timer_seconds}", True, (255, 0, 0))
    else:
        minutes = timer_seconds // 60
        minutes = int(minutes)
        timer_seconds -= minutes * 60
        timer_seconds = int(timer_seconds)
        label = myfont.render(f"Time : {minutes}:{timer_seconds}", True, (255, 0, 0))
    screen.blit(label, (10, 10))
