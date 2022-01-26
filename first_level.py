from const import width, height
from models import Border_constructor, Zombie, Player


def start():
    data = [
        ((10, 10), (width - 20, 10)),
        ((10, height - 20), (width - 20, height - 20)),
        ((10, 10), (10, height - 20)),
        ((width - 20, 10), (width - 20, height - 10)),
        ((1380, 20), (1380, 330)),
        ((1380, 580), (1380, 880)),
        ((20, 580), (1380, 580)),
        ((210, 320), (1380, 320)),
        ((210, 20), (210, 330))
        #((,), (,)),
    ]
    coord_to_zombie = [
        (1000, 340),
        (1000, 500)

    ]
    border = Border_constructor(data)
    player = Player(border, 1460, 760)
    zombie_list = []
    for i in range(len(coord_to_zombie)):
        zombie_list.append(Zombie(border.all_sprites, player, coord_to_zombie[i][0], coord_to_zombie[i][1]))
    return border, player, zombie_list
