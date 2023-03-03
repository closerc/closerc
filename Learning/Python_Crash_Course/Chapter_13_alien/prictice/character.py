import pygame


class Character():
    """模拟游戏角色的类"""
    def __init__(self, cb_settings, screen):
        """初始化角色并设置其初始位置"""
        self.screen = screen
        self.cb_settings = cb_settings

        # 加载角色图像并获得其外接矩形
        self.image = pygame.image.load(
            r'Learning\Python_Crash_Course\alien_invasion\images\yes_32px.bmp'
        )
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个新角色放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在角色的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整角色的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.cb_settings.character_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.cb_settings.character_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_character(self):
        """让角色在屏幕上居中"""
        self.center = self.screen_rect.centerx
