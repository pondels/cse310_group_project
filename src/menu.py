import pygame

from src.downloadVideo import DownloadVideo
from src.wavToCsv import wavToCsv
from src.constants import *
from src.button import Button

class Menu():
    def __init__(self, screen):
        self.screen = screen
        pygame.display.set_caption('Music Visualizer')
        #load button images
        self.start_img = pygame.image.load('src/img/start_btn.png').convert_alpha()
        self.exit_img = pygame.image.load('src/img/exit_btn.png').convert_alpha()
        # basic font for user typed
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = ''
        self.downloadvideo = DownloadVideo()
        self.wavtocsv = wavToCsv()

    def menu(self):
        # create button instances
        start_button = Button(SCREEN_WIDTH / 5, SCREEN_HEIGHT / 1.7, self.start_img, 1, self.screen)
        exit_button = Button(((SCREEN_WIDTH / 5) * 3), SCREEN_HEIGHT / 1.7, self.exit_img, 1, self.screen)

        # create rectangle
        input_rect = pygame.Rect(SCREEN_WIDTH / 5, SCREEN_HEIGHT / 2, (SCREEN_WIDTH / 5) * 3, 32)
            
        # color_active stores color(lightskyblue3) which
        # gets active when input box is clicked by user
        color_active = pygame.Color('lightskyblue3')
        
        # color_passive store color(chartreuse4) which is
        # color of input box.
        color_passive = pygame.Color('chartreuse4')
        color = color_passive

        active = False

        #game loop
        run = True

        while run:
            #event handler
            for event in pygame.event.get():
                #quit game
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False

                if event.type == pygame.KEYDOWN:
    
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:

                        # get text input from 0 to -1 i.e. end.
                        self.user_text = self.user_text[:-1]

                    # Unicode standard is used for string
                    # formation
                    else:
                        self.user_text += event.unicode

            self.screen.fill((202, 228, 241))

            if active:
                color = color_active
            else:
                color = color_passive

            # draw rectangle and argument passed which should
            # be on screen
            pygame.draw.rect(self.screen, color, input_rect)
        
            text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
            
            # render at position stated in arguments
            self.screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            
            # set width of textfield so that text cannot get
            # outside of user's text input
            input_rect.w = max(((SCREEN_WIDTH / 5) * 3) -16, text_surface.get_width() + 10)

            if start_button.draw():
                # does youtube stuff here
                print("Start")
                try:
                    self.downloadvideo.deleteFiles() # Deletes all previous files to avoid problems :>
                    self.downloadvideo.download(self.user_text) # Downloads the video
                    self.downloadvideo.renameFile() # Renames the .wav file
                    wav_file = self.downloadvideo.file # Get's the wav file path
                    csv_file = self.wavtocsv.convertAudio() # Converts wav to csv and gets the csv path
                    # Show on screen in Green text DOWNLOADING VIDEO...
                    return str(wav_file), str(csv_file)
                except: print("INVALID VIDEO URL") # Print in red text ERROR: INVALID VIDEO URL

            if exit_button.draw():
                print("Exit")
                run = False

            pygame.display.flip()
            
        pygame.quit()
