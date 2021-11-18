import pygame

from src.constants import *

class Menu:
    pass

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Music Visualizer')

#load button images
start_img = pygame.image.load('src/img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('src/img/exit_btn.png').convert_alpha()

# button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

# create button instances
start_button = Button(250, 300, start_img, 1)
exit_button = Button(700, 300, exit_img, 1)


#game loop
run = True
while run:

    screen.fill((202, 228, 241))

    if start_button.draw():
        print("Start")
    if exit_button.draw():
        print("Exit")
        run = False

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()

pygame.quit()