import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 设置窗口标题
pygame.display.set_caption('Simple Pygame Example')

# 定义颜色
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 游戏主循环
running = True
while running:
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景色
    screen.fill(BLACK)

    # 在窗口中绘制一个红色的矩形
    pygame.draw.rect(screen, RED, [100, 100, 200, 100])

    # 更新显示
    pygame.display.flip()

# 退出pygame
pygame.quit()
sys.exit()