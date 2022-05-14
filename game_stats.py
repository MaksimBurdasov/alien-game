class GameStats():

	def __init__(self, ai_game):
		self.settings = ai_game.settings
		self.reset_stats()
		self.game_active = False
		self.score = 0
		self.high_score = 0	
		self.health_points = self.settings.ship_limit


	def reset_stats(self):
		self.score = 0
		self.health_points = self.settings.ship_limit
		self.settings.alien_points = 50
		self.level = 1
		

		