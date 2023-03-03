import sys
from random import randint
from time import sleep
import pygame

from ball import Ball


def check_keydown_events(event, cb_settings, screen, charater):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        charater.moving_right = True
    elif event.key == pygame.K_LEFT:
        charater.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, character):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        character.moving_right = False
    elif event.key == pygame.K_LEFT:
        character.moving_left = False


def check_events(cb_settings, screen, character):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, cb_settings, screen, character)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, character)


def update_screen(cb_settings, screen, character, balls):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(cb_settings.bg_color)

    character.blitme()
    balls.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def create_ball(cb_settings, screen, balls):
    """创建一个球并将其放在当前行的随机位置"""
    screen_rect = screen.get_rect()

    ball = Ball(cb_settings, screen)
    ball.x = randint(0, screen_rect.right)
    ball.rect.x = ball.x
    ball.rect.y = ball.rect.height
    balls.add(ball)


def charcter_hit(cb_settings, screen, character, balls):
    """响应抓到球"""
    # 清空球列表
    balls.empty()

    # 创建一个新的球，并将角色放到屏幕底端中央
    create_ball(cb_settings, screen, balls)
    character.center_character()

    # 暂停
    sleep(0.5)


def check_aliens_bottom(cb_settings, stats, screen, character, balls):
    """检查是否有球到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for ball in balls.sprites():
        if ball.rect.bottom >= screen_rect.bottom:
            # 像抓住球一样处理
            if stats.characters_left > 0:
                stats.characters_left -= 1
                charcter_hit(cb_settings, screen, character, balls)
            else:
                stats.game_active = False
            break


def update_ball(cb_settings, stats, screen, character, balls):
    """更新球的位置"""
    balls.update()

    # 检测球和飞船
    if pygame.sprite.spritecollideany(character, balls):
        charcter_hit(cb_settings, screen, character, balls)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(cb_settings, stats, screen, character, balls)
