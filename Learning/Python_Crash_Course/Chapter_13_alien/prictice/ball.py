import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """表示单个球的类"""
    def __init__(self, cb_settings, screen):
        """初始化球并设置其起始位置"""
        super().__init__()
        self.cb_settings = cb_settings
        self.screen = screen

        # 加载球图像，并设置其rect属性
        self.image = pygame.image.load(
            r'Learning\Python_Crash_Course\alien_invasion\images\ball_32.bmp'
        )
        self.rect = self.image.get_rect()

        # 每个球最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储球的准确位置
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制球"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果球位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        """向下移动球"""
        self.y += self.cb_settings.ball_speed_factor
        self.rect.y = self.y
