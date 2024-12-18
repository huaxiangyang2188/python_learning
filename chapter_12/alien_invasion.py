import pygame
from pygame.sprite import Group # type: ignore
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
import game_functions as gf
from button import Button
def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make a game statistics object.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make a group to store aliens in.
    aliens = Group()
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # create a button to start the game
    play_button = Button(ai_settings,screen,"Play")
    

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen,stats,sb,play_button ,ship, aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen, stats,sb,ship,aliens, bullets, play_button)
        

run_game()
   