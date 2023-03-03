import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from character import Character
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    cb_settings = Settings()
    screen = pygame.display.set_mode(
        (cb_settings.screen_width, cb_settings.screen_height)
    )
    pygame.display.set_caption("Catch The Ball")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(cb_settings)

    # 创建一个角色，一个球编组
    character = Character(cb_settings, screen)
    balls = Group()

    # 创建一个位置随机的球
    gf.create_ball(cb_settings, screen, balls)

    # 开始游戏的主循环
    while True:
        gf.check_events(cb_settings, screen, character)
        if stats.game_active:
            character.update()
            gf.update_ball(cb_settings, stats, screen, character, balls)
        gf.update_screen(cb_settings, screen, character, balls)


run_game()
