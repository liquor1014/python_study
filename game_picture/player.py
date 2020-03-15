from game_picture.bullet import *
from game_picture.spirit import *
import os

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # player_img = pygame.image.load(os.path.join(os.getcwd(), "image", "p1_jump.png"))
        self.shoot_sound = pygame.mixer.Sound(os.path.join(os.path.join(os.getcwd()), 'snd', 'pew.wav'))
        self.expl_sounds=pygame.mixer.Sound(os.path.join(os.path.join(os.getcwd()), 'snd','expl3.wav'))
        # self.exp3_sounds = pygame.mixer.Sound(os.path.join(os.path.join(os.getcwd()), 'snd', 'expl4.wav'))
        # self.exp4_sounds = pygame.mixer.Sound(os.path.join(os.path.join(os.getcwd()), 'snd', 'expl5.wav'))
        self.exp2_sounds = pygame.mixer.Sound(os.path.join(os.path.join(os.getcwd()), 'snd', 'expl6.wav'))
        player_img = pygame.image.load(os.path.join(os.path.join(os.getcwd()), 'image', "fly1.jpg")).convert()
        self.player_mini_img = pygame.transform.scale(player_img, (25, 19))
        self.player_mini_img.set_colorkey(BLACK)
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        # self.image = pygame.transform.scale(player_img, (85,60))
        self.image.set_colorkey(BLACK)
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HEIGHT-10
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()


    def update(self):  #控制飞机的运动轨迹
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx=-8
        if keystate[pygame.K_RIGHT]:
            self.speedx=8
        if keystate[pygame.K_UP]:
            self.speedy=-5
        if keystate[pygame.K_DOWN]:
            self.speedy=5
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right =WIDTH
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>HEIGHT:
            self.rect.bottom=HEIGHT

        # unhide if hidden

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                self.shoot_sound.play()
            if self.power >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                self.shoot_sound.play()

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()