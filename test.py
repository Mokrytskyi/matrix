import pygame as pg
import random

class MatrixLetters:
	def __init__(self , app):
		self.app = app 
		self.letters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
		self.font_size = 50
		self.font = pg.font.SysFont('arial' , self.font_size , bold = True)
		self.columns = app.WIDTH // self.font_size
		self.drops = [1 for i in range(0 , self.columns)]

	def draw(self):
		for i in range(0 ,len(self.drops)):
			char = random.choice(self.letters)
			char_render = self.font.render(char , False , (0,148,87))
			pos = i * (self.font_size + 3) , (self.drops[i] - 1) * self.font_size
			self.app.surface.blit(char_render,pos)

			if self.drops[i] * self.font_size > app.HEIGHT and random.uniform(0 , 1) > 0.975:
				self.drops[i] = 0
			self.drops[i] = self.drops[i] + 1

	def run(self):
		self.draw()

class MatrixApp:

	def __init__(self): # INITIALISATION APP

		self.RES = self.WIDTH , self.HEIGHT = 1000 , 1000
		pg.init()
		self.screen = pg.display.set_mode(self.RES)   #displayed screen 
		self.surface = pg.Surface(self.RES, pg.SRCALPHA)           #render surface
		self.clock = pg.time.Clock() 				  #for tracking time
		self.matrixletters = MatrixLetters(self)	  #class instance off letters

	def draw(self):# fill screen and work ground
		self.surface.fill((0,0,0,10))
		self.matrixletters.run()
		self.screen.blit(self.surface, (0,0))

	def run(self): #IMPORTANT PROGRAMM LOOP
		while True:
			self.draw() 							  #screen drawing
			[exit() for i in pg.event.get() if i.type == pg.QUIT]
			pg.display.flip() 						  #updating screen
			self.clock.tick(30) 		  			  # FPS

if __name__ == "__main__":
	app = MatrixApp()
	app.run()