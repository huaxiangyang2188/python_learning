import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        """加载飞船图片并获取其外形"""
        self.image = pygame.image.load('.\\picture\\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """将每艘新飞船放置在屏幕底部中央"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx) #float类型可以储存小数
        #移动标志
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """更新飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_factor
        #根据self.center更新rect对象
        self.rect.centerx = self.center
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        """居中飞船"""
        self.center = self.screen_rect.centerx