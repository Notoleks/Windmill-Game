import pygame
from sys import exit


pygame.init()
width, height = 1800,1000
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
time = pygame.time.get_ticks()

class Button:
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False
		
	def draw(self, surface):
		action = False
		pos = pygame.mouse.get_pos()   
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True   
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
			surface.blit(self.image, (self.rect.x, self.rect.y))    
		return action
	
class Board:
	def __init__(self, width, height, screen):
		self.board = pygame.image.load("windmill_board.png")
		self.rect = self.board.get_rect()
		self.screen = screen
		self.rect.center = (width/2, height/2)


	def draw(self):
		self.screen.blit(self.board, self.rect)

windmill_img = pygame.image.load("Windmill1.png")
windmill_button = Button(100, 200, windmill_img, 0.8)
board1 = Board(width, height, screen)

while True:
	time_delta = clock.tick(60)/1000.0
	time = pygame.time.get_ticks()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()


	# print(time)
	board1.draw()
	windmill_button.draw(screen)
	# timer1.draw()

	pygame.display.update()
	# timer.update(time_delta)
		#game code

	pygame.display.update()
	# clock.tick(60)