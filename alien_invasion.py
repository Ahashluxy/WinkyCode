import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet 
from alien import Alien

class AlienInvasion:
	"""管理游戏资源和行为的类"""
	
	def __init__(self):
		"""初始化游戏并创建游戏资源"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Ivnasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()
        
        #设置背景色
		#self.bg_color = (230, 230, 230)

	def run_game(self):
		"""开始游戏的主循环"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()		
            
            # 每次循环时都重绘屏幕
			"""self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

			# 让最近绘制的屏幕可见
			pygame.display.flip()"""
			# print(len(self.bullets))
			
			self._update_screen()		

	def _check_events(self):
		"""响应按键和鼠标事件"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit();
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)				
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self,event):
		# 响应按键
		if  event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()	
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()	

	def _check_keyup_events(self,event):
		# 响应松开
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		#创建一颗子弹，并将其加入到编组中
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
	def _create_fleet(self):
		"""创建外星人群"""

		#创建一个外星人
		alien = Alien(self)
		# self.aliens.add(alien)
		alien_width = alien.rect.x
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# 创建一行外星人
		for alien_number in range(number_aliens_x):
			# 创建一个外星人加入当前行
			self._create_alien(alien_number)
			"""alien = Alien(self)
			alien.x = alien_width + 2 *alien_width*alien_number
			alien.rect.x = alien.x
			self.aliens.add(alien)"""

	def _create_alien(self,alien_number):
		"""创建一个外星人并将其放在当前行"""
		alien = Alien(self)
		alien_width = alien.rect.width
		alien.x = alien_width + 2 *alien_width*alien_number
		alien.rect.x = alien.x
		self.aliens.add(alien)				

 

	def _update_screen(self):
		"""Update images on the sc reen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)	

		pygame.display.flip()
	"""def _update_screen(self)

		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		pygame.display.flip()"""

	def _update_bullets(self):
		# 更新子弹的位置并删除消失的子弹
		# 更新子弹的位置
		self.bullets.update()

		# 删除消失的子弹
		for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)

				




if __name__ == '__main__':
   
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()					