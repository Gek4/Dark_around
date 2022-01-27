from const import width, height
from models import Border_constructor, Zombie, Player, Swat


def start():
    data = [
        ((10, 10), (width - 20, 10)),
        ((10, height - 20), (width - 20, height - 20)),
        ((0, 60), (10, 60)),
        ((0, 185), (10, 185)),
        ((10, 10), (10, 70)),
        ((10, 185), (10, height - 20)),
        ((width - 20, 10), (width - 20, height - 10)),
        ((390, 450), (1910, 450)),
        ((390, 450), (390, 810)),
        ((1530, 700), (1530, 1060)),
        ((1150, 450), (1150, 810)),
        ((770, 700), (770, 1060)),
        ((10, 235), (1530, 235))
        # ((,), (,)),
    ]
    coord_to_zombie = [
        (1150, 830),
        (1480, 985),
        (1320, 900),
        (830, 710),
        (430, 790),
        (335, 450),
        (840, 270),
        (1215, 385),
        (365, 120),
        (1570, 235)
    ]

    border = Border_constructor(data)
    player = Player(border, 1700, 880)
    swat = [Swat(border.horizontal_borders, border.vertical_borders, border.all_sprites, player, 100, 350,
                [(100, 350), (1800, 350)])]
    zombie_list = []
    for i in range(len(coord_to_zombie)):
        zombie_list.append(Zombie(border.all_sprites, player, coord_to_zombie[i][0], coord_to_zombie[i][1]))
    return border, player, zombie_list, swat
