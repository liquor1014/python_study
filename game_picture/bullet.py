import pygame
import os
from game_picture.common import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        bullet_img=pygame.image.load(os.path.join(os.path.join(os.getcwd()), 'image', "6.png")).convert()
        pygame.sprite.Sprite.__init__(self)
        self.image=bullet_img
        # self.image=pygame.Surface((2,10))
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
