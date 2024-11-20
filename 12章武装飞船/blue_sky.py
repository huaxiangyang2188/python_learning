import sys
#sys.path.append('C:\\Users\\lenovo\\Desktop\\python_project\\12章武装飞船\\plane.py')

import pygame
from settings import Settings
from plane import Plane
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Blue Sky")
        # 创建飞机
    plane = Plane(ai_settings,screen)

    gf.check_events(plane)
          #开始游戏主循环


    while True:         
        gf.check_events(plane) # 添加参数plane
        plane.update()
        gf.update_screen(ai_settings, screen, plane)
        #添加退出游戏条件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
run_game()
       