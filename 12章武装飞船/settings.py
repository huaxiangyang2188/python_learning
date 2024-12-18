class Settings():
    """存储《外星人入侵》游戏的设置"""
    def __init__(self):
     """初始化游戏的设置"""
    # 屏幕设置
     self.screen_width = 1200
     self.screen_height = 800
     self.bg_color = (230, 230, 230)
     self.bullet_allowed = 3
     self.ship_factor = 1
     #飞船速度设置
     self.ship_speed = 1.5
     #子弹设置
     self.bullet_speed_factor =  1
     self.bullet_width = 3
     self.bullet_height = 15
     self.bullet_color = 60, 60, 60 #设置了宽3像素、高15像素、颜色为灰色子弹
     self.bullets_allowed = 3 # 最多允许3个子弹，新增
     self.bullet_speed_factor = 1.5 # 子弹速度， 新增