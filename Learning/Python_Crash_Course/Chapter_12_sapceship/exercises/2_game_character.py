import sys
import pygame


class Yes():
    def __init__(self, screen):
        """初始化人物并设置其初始位置

        Args:
            screen (str): 屏幕对象
        """
        self.screen = screen
        # 加载人物图像并获取其外接矩形
        self.image = pygame.image.load(
            r'Learning\Python_Crash_Course\alien_invasion\images\yes_32px.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将人物放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制人物"""
        self.screen.blit(self.image, self.rect)


def run_game():
    # 初始化并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Game Character")

    bg_color = (255, 255, 255)

    # 创建人物
    character = Yes(screen)

    # 开始主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕
        screen.fill(bg_color)
        character.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
