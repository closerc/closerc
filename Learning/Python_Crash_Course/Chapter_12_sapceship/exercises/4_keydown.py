import sys
import pygame


def run_game():
    # 创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Keydown")

    # 背景颜色
    bg_color = (255, 255, 255)

    # 开始主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.type)

        screen.fill(bg_color)

        pygame.display.flip()


run_game()
