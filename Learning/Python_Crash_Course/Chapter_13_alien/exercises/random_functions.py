import sys
import pygame
from random import randint

from star import Star


def check_keydown_events(event):
    """响应按键

    Args:
        event (_type_): 事件
        ship (_type_): 飞船实例
    """
    if event.key == pygame.K_q:
        sys.exit()


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)


def update_screen(ai_settings, screen, stars):
    """更新屏幕上的图像，并切换到新屏幕

    Args:
        ai_settings (class object): 设置实例
        screen (_type_): 屏幕对象
    """
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    stars.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def get_number_alines_x(ai_settings, star_width):
    """计算每行可容纳多少个星星"""
    available_space_x = ai_settings.screen_width - 2 * star_width
    number_aliens_x = int(available_space_x / (2 * star_width))

    return number_aliens_x


def get_number_rows(ai_settings, star_height):
    """计算屏幕可容纳多少行星星"""
    available_space_y = ai_settings.screen_height - 3 * star_height
    number_rows = int(available_space_y / (2 * star_height))

    return number_rows


def create_star(ai_settings, screen, stars, star_number, row_number):
    """创建一个星星并将其放在当前行"""
    star = Star(ai_settings, screen)
    star.x = randint(0, star_number)
    star.rect.x = star.x
    star.rect.y = randint(0, row_number)
    stars.add(star)


def create_fleet(ai_settings, screen, stars):
    """创建星星群"""
    # 创建一个星星，并计算一行可容纳多少个星星
    star = Star(ai_settings, screen)
    number_stars_x = get_number_alines_x(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, star.rect.height)

    # 创建随机星星
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars, ai_settings.screen_width, ai_settings.screen_height)
