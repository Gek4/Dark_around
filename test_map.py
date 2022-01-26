import pygame
import first_level
from const import *
from models import graphics_character, graphics_zombie

pygame.init()

border, player, zombie_list = first_level.start()  # border, player, zombie
running = True
t = 0
zombie_go = True
death_per_tick = []
_image_character = graphics_character()
_image_zombie = graphics_zombie()
while running:
    if not all(death_per_tick) or len(death_per_tick) == 0:
        screen.blit(background, (0, 0))
        screen.blit(_image_character, player.get_cords)
        # pygame.draw.rect(screen, (41, 41, 41), (20, 20, 1560, 860))
        # pygame.draw.rect(screen, (0, 0, 0), (210, 20, 1170, 310))
        # pygame.draw.rect(screen, (0, 0, 0), (20, 580, 1360, 300))
        # pygame.draw.rect(screen, (100, 150, 250),
        #                  (23, 23, width - 45, height - 45), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        t += clock.tick()

        if t >= 16:
            vx = 0
            vy = 0
            if pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_a]:
                vy = -3
                vx = -3
            elif pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_d]:
                vy = -3
                vx = 3
            elif pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_a]:
                vy = 3
                vx = -3
            elif pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_d]:
                vy = 3
                vx = 3
            elif pygame.key.get_pressed()[pygame.K_w]:
                vy = -4
            elif pygame.key.get_pressed()[pygame.K_s]:
                vy = 4
            elif pygame.key.get_pressed()[pygame.K_a]:
                vx = -4
            elif pygame.key.get_pressed()[pygame.K_d]:
                vx = 4
            death_z = False
            for zombie in zombie_list:
                screen.blit(_image_zombie, zombie.get_cords)
                death_z = death_z or pygame.sprite.spritecollideany(player, zombie.get_group) is not None
            death_per_tick.append(death_z)
            zombie_go = not zombie_go
            border.all_sprites.draw(screen)
            player.update(vx, vy)
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
