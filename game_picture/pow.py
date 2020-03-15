import pygame
import random
import os
from game_picture.common import *



powerup_images = {}


class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        # self.exp3_sounds = pygame.mixer.Sound(os.path.join(os.path.join(os.getcwd()), 'snd', 'expl4.wav'))
        powerup_images['shield'] = pygame.image.load(
            os.path.join(os.path.join(os.getcwd()), 'image', 'shield_gold.png')).convert()
        # self.exp4_sounds = pygame.mixer.Sound(os.path.join(os.path.join(os.getcwd()), 'snd', 'expl5.wav'))
        powerup_images['gun'] = pygame.image.load(
            os.path.join(os.path.join(os.getcwd()), 'image', 'bolt_gold.png')).convert()
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the bottom of the screen
        if self.rect.top > HEIGHT:
            self.kill()