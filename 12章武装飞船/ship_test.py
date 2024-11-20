import sys
import pygame
from ship import Ship
import game_functions as gf  # 简化的别名
from settings import Settings
from bullet import Bullet
from pygame.sprite import Sprite
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen) #添加实参ai_settings,screen
    gf.check_events()
         #--snip---  
     #开始游戏主循环
pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Alien Invasion")
ship = Ship(ai_settings,screen) #添加实参ai_settings,screen

# 创建子弹组
bullets = pygame.sprite.Group()

#Sprite()
while True:
    #监视键盘和鼠标事件 
    gf.check_events(ai_settings,screen,ship, bullets) # 添加参数ship
    ship.update()
    gf.update_bullets(bullets) 
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))    # 打印子弹数量,但会降低游戏运行速度
    gf.update_screen(ai_settings, screen, ship,bullets)