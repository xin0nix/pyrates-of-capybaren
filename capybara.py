import pygame

from lib import Player, Enemy

# https://realpython.com/pygame-a-primer/#sprites

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()

screen = pygame.display.set_mode(WINDOW)

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)

player = Player(WINDOW)
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy(WINDOW)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()

    # #3498db
    screen.fill((0x34, 0x98, 0xDB))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        for entity in all_sprites:
            entity.kill()
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
