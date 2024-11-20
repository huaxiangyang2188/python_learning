#创建一个空的Pygame窗口，使用Pygame游戏基本结构如下：
#alien_invasion.py
import sys
import pygame
#导入两个模块，pygame负责开发游戏的功能，sys负责玩家退出游戏。
def run_game1():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800)) #这个实参明确了创建一个高、宽1200和800像素的游戏窗口
    pygame.display.set_caption("Alien Invasion")
    #设置背景色
    bg_color = (230,230,230)


    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    #让最新绘制的屏幕可见
    screen.fill(bg_color)
    pygame.display.flip()
#run_game()
#12.3.2 设置背景色（Pygame默认是黑色屏幕）
#设置另外一种颜色
    #screen = pygame.display.set_mode((1200,800))
    #pygame.display.set_caption("Alien Invasion")
    #bg_color = (230,230,230)
#开始游戏主循环。
    #while True:
    #监听键盘和鼠标事件
   # ---snip---
   #每次循环时都重绘屏幕
   #screen.fill(bg_color)
#让最近绘制的屏幕可见
    #pygame.display.flip()
#run_game()
#12.3.3 创建设置类，每次增加新功能则引入新设置，统一放入settings模块，包含Settings的类
import pygame

class Settings():
    """存储《外星人入侵》游戏的设置"""
    def __init__(self):
     """初始化游戏的设置"""
    # 屏幕设置
     self.screen_width = 1200
     self.screen_height = 800
     self.bg_color = (230, 230, 230)

from ship import Ship
def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #开始游戏主循环
    ship = Ship(ai_settings,screen)
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()
#run_game()
      
#12.4 添加飞船图像
#从资源库下载图片保存在images文件
#ship.py
import pygame
class Ship():
    def __init__(self,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        """加载飞船图片并获取其外形"""
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """将每艘新飞船放置在屏幕底部中央"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
#重构： 模块game_functions
# 通过创建新模块game_functions.py，将各类游戏将运行的函数移动到其中，从而避免主程序太长。
import sys
import pygame
def check_events():
    """响应键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.tpye == pygame.QUIT:
            sys.exit()
#修改alin_invasion.py,导入game_functions模块，将事件循环替换为函数调用
# alien_invasion.py
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf  # 简化的别名
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    gf.check_events()
    while True:
        #监视键盘和鼠标事件
        gf.check_events()
        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()
# 12.5.2 函数update_screen(),将上述屏幕更新代码移植到update_screen()函数中,同时放入game_functions模块中
import sys
import pygame
def check_events():
    """响应键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.tpye == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()
#修改alien_invasion.py,导入game_functions模块.
# alien_invasion.py
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf  # 简化的别名
         #--snip---  
     #开始游戏主循环
#while True:
        #监视键盘和鼠标事件 
    # gf.check_events()
     #gf.update_screen(ai_settings, screen, ship)


#完成一个天空飞机小作业
import sys
#sys.path.append('C:\\Users\\lenovo\\Desktop\\python_project\\12章武装飞船\\plane.py')

import pygame
from settings import Settings
from plane import Plane



def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Blue Sky")
        # 创建飞机
    plane = Plane(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(settings.bg_color)  # 填充背景颜色
        plane.blitme()  # 绘制飞机
        pygame.display.update()  # 更新屏幕
#run_game()

#12.6 驾驶飞机
# 12.6.1 添加键盘控制,先调整game_functions.py中check_events()函数,后更新alien_invasion.py调用check_events()代码
import sys
import pygame
from pygame.sprite import Group
from ship import Ship
import game_functions as gf  # 简化的别名
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen) #添加实参ai_settings,screen
    bullets = Group()
    gf.check_events(ship)
         #--snip---  
     #开始游戏主循环
    while True:
        #监视键盘和鼠标事件 
        gf.check_events(ai_settings,screen,ship,bullets) # 添加参数ship
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship,bullets)
run_game()