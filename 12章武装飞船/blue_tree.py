import sys
import pygame
from settings import Settings
from sun import Sun
def run_geme():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.screen_width,ai_settings.screen_height)
    pygame.display.set_caption("bule sky and white sun")
    #设置背景色
    bg_color = (0,0,230)
    #创建一个太阳
    sun = Sun(screen)

    #开始游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #每次循环时都重绘屏幕
        screen.fill(ai_settings,bg_color)
        sun.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()
    run_game()
