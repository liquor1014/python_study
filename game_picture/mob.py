import pygame
import random
import os
from game_picture.common import *


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        mob_img = pygame.image.load(os.path.join(os.path.join(os.getcwd()), 'image', "boss.png")).convert()
        pygame.sprite.Sprite.__init__(self)
        self.image=mob_img
        # self.image=pygame.Surface((20,30))
        m=random.choice(range(10,70))
        self.image = pygame.transform.scale(mob_img, (m,m))
        self.image.set_colorkey(BLACK)
        # self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x=random.randrange(WIDTH - self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.recty=random.randrange(1,8)
        self.rectx=random.randrange(-3,3)

    def update(self):
        self.rect.x += self.rectx
        self.rect.y += self.recty
        if self.rect.top>HEIGHT + 10 or self.rect.left< -25 or self.rect.right>WIDTH+20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
