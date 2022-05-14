import sys
from time import sleep

import pygame

from pygame.sprite import Sprite
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from scoreboard import Scoreboard
from ship_grey import Ship_grey
from background import Around


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""
    
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        self.bg_image = pygame.image.load("images/background.jpg")
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bg_objects = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "Play")

       
    def run_game(self):
        while True:
            self._check_events() #перерисовка экрана

            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()
                self.bg_objects.update()

            self._update_screen()


    def _update_screen(self):
        self.screen.blit(self.bg_image, (0, 0))
        for obj in self.bg_objects:
            obj.blitme()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


    def _check_events(self): #Обработка нажатия мыши & клавиатуры 
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True   
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True #Проверка нажата ли кнопка вверх
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True #Проверка нажата ли кнопка вниз
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            self.start_game()
 

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False            
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False #проверка отжата ли кнопка
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False #проверка отжата ли кнопка


    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()

            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()



    def start_game(self):
        pygame.mouse.set_visible(False)

        self.stats.reset_stats()
        self.stats.game_active = True

        self.aliens.empty()
        self.bullets.empty()
        self.bg_objects.empty()

        self._creat_bg_objects()
        self._create_fleet()
        self.ship.center_ship()        


    def _creat_bg_objects(self):
        for _ in range(3):
            self.bg_objects.add(Around(self))


    def _fire_bullet(self): #self указатель на не созданный объект
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, False)
        # print(type(collisions.values()), collisions.values())
        #{<Bullet Sprite(in 337 groups)>: [<Alien Sprite(in 0 groups)>, <Alien Sprite(in 0 groups)>, 
        #<Alien Sprite(in 0 groups)>, <Alien Sprite(in 0 groups)>, <Alien Sprite(in 0 groups)>]}
        kills = len(collisions)
        self.stats.score += kills
        # if self.stats.score > 9:
         #  self.stats.game_active = False
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

        if collisions:
            for aliens in collisions.values():
                for alien in aliens:
                    alien.hp -= 1 # Уменьшение жизни
                    if not alien.hp:
                        alien.kill()
                        self.stats.score += self.settings.alien_points
                    alien.carrent_costume = (alien.carrent_costume + 1) % 3                  
                    alien.image = alien.alien_costumes[alien.carrent_costume]
            self.sb.prep_score()
            self.sb.check_high_score() #

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        # alien_height = alien.rect.height
        number_rows = 3
        number_aliens = 5
        gap = int((self.settings.screen_width - (number_aliens + 2) * alien_width) / (number_aliens - 1))
        # ship_height = self.ship.rect.height

        for row in range(number_rows):
            for alien_number in range(number_aliens):
               self._create_alien(row, alien_number, gap)
    
 
    def _create_alien(self, alien_row, alien_number, gap):
    # """Создание пришельца и размещение его в ряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (gap + alien_width) * alien_number
        alien.rect.x = alien.x
        alien.y = alien.rect.height // 10 + 1.5 * alien.rect.height  * alien_row # доли пиксилей
        alien.rect.y = alien.y # значение alien.rect  содержит целое количество пиксилей
        self.aliens.add(alien)



    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break



    def _ship_hit(self):
        if self.stats.health_points > 0:
            self.stats.health_points -= 1
            self.sb.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)



    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens:
            alien.y += self.settings.fleet_drop_speed
            alien.rect.y = alien.y        
        self.settings.fleet_direction *= -1 
        

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()




