import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """表示单个星星的类"""
    def __init__(self, ai_settings, screen):
        """初始化星星并设置其起始位置"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载星星人图像，并设置其rect属性
        self.image = pygame.image.load(
            r'Learning\Python_Crash_Course\alien_invasion\images\water_32.bmp')
        self.rect = self.image.get_rect()

        # 每个星星最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储星星人的准确位置
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果星星消失于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True
