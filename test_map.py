import pygame


def start_game():
    import first_level
    import const
    import models

    pygame.init()

    # load level information
    border, player, zombie_list, swat = first_level.start()  # border, player, zombie
    last_pic = const.last_picture
    _image_character_front, _image_character_back, \
    _image_character_left, _image_character_right = models.graphics_character()
    _image_zombie = models.graphics_zombie()
    _images_character = [
        _image_character_front,
        _image_character_back,
        _image_character_left,
        _image_character_right
    ]

    running = True
    t = 0
    time = 0
    zombie_go = True
    death_per_tick = []
    while running:
        if (not all(death_per_tick) or len(death_per_tick) == 0) and swat.alive:
            const.screen.blit(const.background, (0, 0))
            # screen.blit(_image_character, player.get_cords)
            # pygame.draw.rect(screen, (41, 41, 41), (20, 20, 1560, 860))
            # pygame.draw.rect(screen, (0, 0, 0), (210, 20, 1170, 310))
            # pygame.draw.rect(screen, (0, 0, 0), (20, 580, 1360, 300))
            # pygame.draw.rect(screen, (100, 150, 250),
            #                  (23, 23, width - 45, height - 45), 5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False

            t += const.clock.tick()
            if t >= 16:
                time += 1
                vx = 0
                vy = 0
                if pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_a]:
                    vy = -3
                    vx = -3
                    const.screen.blit(_images_character[1], player.get_cords)
                    last_pic = 1
                elif pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_d]:
                    vy = -3
                    vx = 3
                    const.screen.blit(_images_character[1], player.get_cords)
                    last_pic = 1
                elif pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_a]:
                    vy = 3
                    vx = -3
                    const.screen.blit(_images_character[0], player.get_cords)
                    last_pic = 0
                elif pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_d]:
                    vy = 3
                    vx = 3
                    const.screen.blit(_images_character[0], player.get_cords)
                    last_pic = 0
                elif pygame.key.get_pressed()[pygame.K_w]:
                    vy = -4
                    const.screen.blit(_images_character[1], player.get_cords)
                    last_pic = 1
                elif pygame.key.get_pressed()[pygame.K_s]:
                    vy = 4
                    const.screen.blit(_images_character[0], player.get_cords)
                    last_pic = 0
                elif pygame.key.get_pressed()[pygame.K_a]:
                    vx = -4
                    const.screen.blit(_images_character[2], player.get_cords)
                    last_pic = 2
                elif pygame.key.get_pressed()[pygame.K_d]:
                    vx = 4
                    const.screen.blit(_images_character[3], player.get_cords)
                    last_pic = 3
                else:
                    const.screen.blit(_images_character[last_pic], player.get_cords)
                death_z = False
                for zombie in zombie_list:
                    const.screen.blit(_image_zombie, zombie.get_cords)
                    death_z = death_z or pygame.sprite.spritecollideany(player, zombie.get_group) is not None
                death_per_tick.append(death_z)
                zombie_go = not zombie_go
                border.all_sprites.draw(const.screen)
                player.update(vx, vy)
                swat.update()
                if zombie_go:
                    for zombie in zombie_list:
                        zombie.update()
                pygame.display.flip()
                if len(death_per_tick) > 21:
                    death_per_tick = death_per_tick[-22:]
                t = 0

        else:
            running = False
            pygame.display.flip()
