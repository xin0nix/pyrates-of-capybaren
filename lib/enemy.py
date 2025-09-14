import random

import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, window: tuple[int, int]):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(
            "pirate-pack/PNG/Default size/Ship parts/cannonBall.png"
        ).convert_alpha()
        self.window = window
        self.rect = self.surf.get_rect(
            center=(
                random.randint(window[0] + 10, window[0] + 100),
                random.randint(0, window[1] - 5),
            )
        )
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
