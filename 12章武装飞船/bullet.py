from typing import Any
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """一个队飞船发射的子弹的管理类"""
    def __init__(self,ai_settings,screen,ship):
        """初始化子弹，并设置初始位置"""
        super().__init__()
        self.screen = screen
        # 创建子弹对象，并设置其初始位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor # 子弹移动速度,有修改
    def update(self):
        """移动子弹，并更新其位置"""
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)