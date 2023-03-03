class Settings():
    """存储《抓球》所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # 人物设置
        self.character_speed_factor = 1.5
        self.character_limit = 3

        # 球设置
        self.ball_speed_factor = 1
