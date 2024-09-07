import pygame
from sys import exit
import pygame_gui


pygame.init()
width, height = 1800,1000
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
time = pygame.time.get_ticks()
manager = pygame_gui.UIManager((width, height))

windmill = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 100), (150, 150)), text ='', manager=manager)
windmill1 = pygame.image.load("Windmill1.png")
windmill.set_image(windmill1)

# timer = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((200, 200), (100,100)), text = f"{time}", manager = manager)
# clock = pygame.time.Clock()
# class Timer:
#     def __init__(self, width, height, screen, ):

class Timer:
    def __init__(self, x, y, width, height, text , screen):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.screen = screen
    
    def draw(self):
        # pygame.draw.rect(screen, self.rect)
        self.screen.blit(self.surface, self.rect)

class Board:
    def __init__(self, width, height, screen):
        self.board = pygame.image.load("windmill_board.png")
        self.rect = self.board.get_rect()
        self.screen = screen
        # self.board = pygame.transform.scale(self.board,(600, 600))
        self.rect.center = (width/2, height/2)


    def draw(self):
        surf = self.
        self.screen.blit(self.board, self.rect)


board1 = Board(width, height, screen)
timer1 = Timer(200, 200, width, height, f"{time}", screen)
while True:
    time_delta = clock.tick(60)/1000.0
    time = pygame.time.get_ticks()
    # print(time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == windmill:
                print('Windmill placed')
        manager.process_events(event)
    manager.update(time_delta)
    manager.update(time)
    print(time)
    board1.draw()
    timer1.draw()
    manager.draw_ui(screen)
    # manager.draw_ui(timer)
    pygame.display.update()
    # timer.update(time_delta)
        #game code

    pygame.display.update()
    # clock.tick(60)