import pygame
from sys import exit


pygame.init()
width, height = 1800,1000
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
time = pygame.time.get_ticks()
mouse_pos = pygame.mouse.get_pos()
font = pygame.font.Font('free-sans-bold.ttf', 20)

def display_time():
	time_surf = font.render(f"{time}", False, (255, 0, 0))
	time_rect = time_surf.get_rect(center = (200, 500))
	screen.blit(time_surf, time_rect)
	# print(time)

class Button:
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False
		
	def draw(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))    

	def mouse_pressed(self):
		
		mouse_pos = pygame.mouse.get_pos()   
		if self.rect.collidepoint(mouse_pos):
			if pygame.mouse.get_pressed()[0] == 1:
				print("windmill")
	

	
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
	windmill_button.mouse_pressed()
	# timer1.draw()
	display_time()
	pygame.display.update()
	# timer.update(time_delta)
		#game code

	pygame.display.update()
	# clock.tick(60)