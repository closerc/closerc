import sys
import pygame

from flank_bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键

    Args:
        event (_type_): 事件
        ship (_type_): 飞船实例
    """
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开

    Args:
        event (_type_): 事件
        ship (_type_): 飞船实例
    """
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕

    Args:
        ai_settings (class object): 设置实例
        screen (_type_): 屏幕对象
        ship (class object): 飞船实例
    """
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(bullets, ship):
    """更新子弹的位置，并删除已消失的子弹

    Args:
        bullets (_type_): 子弹编组
    """
    # 更新子弹的位置
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.left >= ship.screen_rect.right:
            bullets.remove(bullet)
