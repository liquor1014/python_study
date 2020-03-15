from game_picture.player import *
from game_picture.mob import Mob
from game_picture.explosion import Explosion
from game_picture.pow import Pow
import pygame
import os
import random
'''
初始化格式
'''

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("飞机大战11.0")
clock = pygame.time.Clock()

background = pygame.image.load(os.path.join(os.path.join(os.getcwd()),'image','main_photo.jpg')).convert()
background_rect = background.get_rect()
pygame.mixer.music.load(os.path.join(os.path.join(os.getcwd()),'snd', 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.4)

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def hide(self):
    # hide the player temporarily
    self.hidden = True
    self.hide_timer = pygame.time.get_ticks()
    self.rect.center = (WIDTH / 2, HEIGHT + 200)

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "START!!!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Arrow keys move, Space to fire", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Pass Keywoed To Begin Game", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
# screen.fill(BLACK)
# screen.blit(background, background_rect)
# all_sprites.draw(screen)

# player = Player()
# all_sprites.add(player)
# for i in range(18):
#     newmob()
'''
游戏开始循环体
'''
score = 0
pygame.mixer.music.play(loops=-1)
game_over = True
running = True

while running:
    if game_over:
        show_go_screen()
        game_over = False
        # all_sprites = pygame.sprite.Group()
        # mobs = pygame.sprite.Group()
        # bullets = pygame.sprite.Group()
        # powerups = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            newmob()
        score = 0
    clock.tick(FPS)
    pygame.display.flip()
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:   #空格---发射子弹
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)   #碰撞检测
    for hit in hits:
        score += 50 - hit.radius
        player.shoot_sound.play()
        player.expl_sounds.play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob()

    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.exp2_sounds.play()
        player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0:
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.shield = 100

    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            # player.exp3_sounds.play()
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'gun':
            # player.exp4_sounds.play()
            player.powerup()
            # power_sound.play()

        # if the player died and the explosion has finished playing
        if player.lives == 0 and not death_explosion.alive():
            running = False
            game_over = True



    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen,"score:",18,WIDTH/2-40,10)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)
    draw_lives(screen, WIDTH - 100, 5, player.lives,player.player_mini_img)
    pygame.display.flip()

pygame.quit()

