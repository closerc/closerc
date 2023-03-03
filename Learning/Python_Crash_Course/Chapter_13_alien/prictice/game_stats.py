class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, cb_settings):
        """初始化统计信息"""
        self.cb_settings = cb_settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.characters_left = self.cb_settings.character_limit

        # 游戏刚启动时处于活动状态
        self.game_active = True
