import pygame

from rocket_settings import Settings
from rocket import Ship
import rocket_functions as rf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invation")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        rf.check_events(ship)
        ship.update()
        rf.update_screen(ai_settings, screen, ship)


run_game()
