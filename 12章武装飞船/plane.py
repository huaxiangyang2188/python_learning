import pygame
class Plane():
    def __init__(self,ai_settings,screen):
        """初始化飞机并设定初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞机图片
        self.image = pygame.image.load('plane.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #将飞机放在屏幕中央
        self.rect.center = self.screen_rect.center
         #在飞机的属性center中存储小数值
        self.center = float(self.rect.centerx) #float类型可以储存小数
        #移动标志
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """更新飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.plane_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.plane_factor
        #根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞机"""
        self.screen.blit(self.image, self.rect)

        