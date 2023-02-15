import pygame
from pygame.sprite import Group

from ship_settings import Settings
from ship_1 import Ship
import ship_functions as sf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invation")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        sf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        sf.update_bullet(bullets, ship)
        sf.update_screen(ai_settings, screen, ship, bullets)


run_game()
