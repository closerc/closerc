import pygame
from pygame.sprite import Group

from star_settings import Settings
import star_functions as sf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Stars")

    # 创建一个星星编组
    stars = Group()

    # 创建星星群
    sf.create_fleet(ai_settings, screen, stars)

    # 开始游戏的主循环
    while True:
        sf.check_events()
        sf.update_screen(ai_settings, screen, stars)


run_game()
