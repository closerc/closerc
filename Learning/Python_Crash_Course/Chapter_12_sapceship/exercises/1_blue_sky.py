# 创建一个背景为蓝色的Pygame窗口
import sys
import pygame


def blue_sky():
    # 初始化并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")

    bg_color = (162, 238, 255)
    # 开始主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕
        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


blue_sky()
