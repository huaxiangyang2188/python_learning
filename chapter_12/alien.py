import pygame
from pygame.sprite import Sprite

class Alien(Sprite):   
     """表示单个外星人的类"""
     def __init__(self,ai_settings,screen):
        """初始化外星人并设置其初始位置。"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载外星人图片并设置其rect属性。
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #开始每个新外星人时，将左上角置于屏幕左上角。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #存储外星人的精确位置。
        self.x = float(self.rect.x)
     def blitme(self):
         """在指定位置绘制外星人。"""
         self.screen.blit(self.image,self.rect)
     def check_edges(self):
          """返回True如果外星人到达屏幕边缘。"""
          screen_rect = self.screen.get_rect()
          if self.rect.right >= screen_rect.right:
               return True
          elif self.rect.left <= 0:
               return True
          return False 
     def update(self):
         """向左或右移动外星人。"""
         self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
         self.rect.x = self.x  
