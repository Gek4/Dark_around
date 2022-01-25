import pygame
import first_level
from const import *

pygame.init()

border, player, zombie = first_level.start()  # border, player, zombie
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
