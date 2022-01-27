from const import width, height
from models import Border_constructor, Zombie, Player, Swat


def start():
    data = [
        ((10, 10), (width - 20, 10)),
        ((10, height - 20), (width - 20, height - 20)),
        ((10, 10), (10, height - 20)),
        ((width - 20, 10), (width - 20, height - 10)),
        ((700, 280), (1200, 280)),
        ((700, 280), (700, 780)),
        ((700, 780), (1200, 780)),
        ((1200, 280), (1200, 790)),
        ((1500, 530), (1900, 530)),
        ((1500, 730), (1500, 1060)),
        ((1500, 10), (1500, 340)),
        ((10, 530), (410, 530)),
        ((410, 730), (410, 1060)),
        ((410, 10), (410, 340)),
    ]
    coord_to_zombie = [
        (1450, 520),
        (420, 520),
        (425, 730),
        (1450, 730),
        (425, 310),
        (1450, 310),
        (760, 795),
        (920, 795),
        (1080, 795),
        (760, 200),
        (920, 200),
        (1080, 200)

    ]
    border = Border_constructor(data)
    player = Player(border, 1700, 880)
    swat = [Swat(border.horizontal_borders, border.vertical_borders, border.all_sprites, player, 1760, 50,
                 [(1760, 50), (1760, 450), (1350, 450), (1350, 930), (550, 930), (550, 130), (1350, 130), (1350, 400),
                  (1650, 400), (1650, 50)]),
            Swat(border.horizontal_borders, border.vertical_borders, border.all_sprites, player, 150, 960,
                 [(150, 960), (150, 600), (550, 600), (550, 130), (1350, 130), (1350, 930), (550, 930), (550, 650),
                  (300, 650), (300, 960)])]
    zombie_list = []
    for i in range(len(coord_to_zombie)):
        zombie_list.append(Zombie(border.all_sprites, player, coord_to_zombie[i][0], coord_to_zombie[i][1]))
    return border, player, zombie_list, swat
