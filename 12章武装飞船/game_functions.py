import sys
import pygame
from bullet import Bullet


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应键盘和鼠标事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #创建一一颗子弹，并将它加入到飞船的子弹列表中
        # new_bullet = Bullet(ai_settings,screen,ship)
        # bullets.add(new_bullet)
        fire_bullet(ai_settings=ai_settings,screen=screen,ship=ship,bullets=bullets)

def check_keyup_events(event,ship):
    """响应松开键盘的键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
            
def check_events(ai_settings,screen,ship,bullets):
                #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen,ship,bullets)            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)           
                                
def update_screen(ai_settings,screen,ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除消失的子弹(新增)"""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """开火发射子弹(新增)"""
    # Create a new bullet, add to bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)