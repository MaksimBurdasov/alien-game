class Settings(): # обстрактное описание
	def __init__(self): #конструктор
		self.screen_width = 1200
		self.screen_height = 800 
		self.bg_color = (255, 0, 255)
		
		self.bg_image_speed = 0.2

		self.bullet_speed = 20
		self.bullet_width = 5
		self.bullet_height = 20
		self.bullet_color = (255, 255, 255)
		self.bullets_allowed = 1

		self.alien_speed = 0.6
		self.fleet_drop_speed = 20
		# fleet_direction = 1 обозначает движение вправо; а -1 - влево.
		self.fleet_direction = 1
		self.alien_points = 50

		self.ship_speed = 1.5
		self.ship_limit = 2


		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.start_health_alien = 3 #

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):	
		self.bg_image_speed_factor = 1.2

		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 2.5
		self.alien_speed_factor = 0.1

		self.fleet_direction = 1


	def increase_speed(self):
		self.bg_image_speed_factor *= self.speedup_scale

		self.ship_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
			

