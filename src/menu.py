import pygame
from pygame.image import tostring
import pygame.scrap as scrap

from src.downloadVideo import DownloadVideo
from src.wavToCsv import wavToCsv
from src.constants import *
from src.button import Button
import src.constants as constants
import time
import aubio

scrap.init()
scrap.set_mode(pygame.SCRAP_CLIPBOARD)

class Menu():
    def __init__(self, screen):
        self.screen = screen
        pygame.display.set_caption('Music Visualizer')
        #load button images (Light Mode)
        # start_img = pygame.image.load('src/img/start_btn.png').convert_alpha()
        # exit_img = pygame.image.load('src/img/exit_btn.png').convert_alpha()

        #load button images (Dark Mode)
        start_img = pygame.image.load('src/img/start_btn_dark.png').convert_alpha()
        exit_img = pygame.image.load('src/img/exit_btn_dark.png').convert_alpha()
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

        # Invalid URL Input
        failed = False

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

                keys = pygame.key.get_pressed()

                if event.type == pygame.KEYDOWN:

                    if keys[pygame.K_LCTRL] and keys[pygame.K_v]:
                        for t in scrap.get_types():
                            r = scrap.get(t)
                            self.user_text = r.decode()
    
                    # Check for backspace
                    elif event.key == pygame.K_BACKSPACE:

                        # get text input from 0 to -1 i.e. end.
                        self.user_text = self.user_text[:-1]

                    # Unicode standard is used for string
                    # formation
                    else:
                        self.user_text += event.unicode

            # Light Mode
            # screen.fill((202, 228, 241))

            # Dark Mode
            screen.fill((8, 20, 305))

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

            if failed:
                failed_font = pygame.font.Font(None, 72)
                text = failed_font.render('INVALID URL!', True, (255, 0, 0))
                text_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, 32)
                self.screen.blit(text, (text_rect.x-175, text_rect.y-55))
                pygame.display.flip()
                time.sleep(3)
                failed = False

            if start_button.draw():
                # does youtube stuff here
                print("Start")
                try:
                    print(self.user_text)
                    if "https://" not in self.user_text:
                        self.user_text = "https://" + self.user_text
                    
                    # Creates a loading screen
                    loading_font = pygame.font.Font(None, 72)
                    text = loading_font.render('LOADING...', True, (0, 255, 0))
                    text_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, 32)
                    self.screen.blit(text, (text_rect.x-120, text_rect.y-55))
                    pygame.display.flip()

                    self.downloadvideo.deleteFiles() # Deletes all previous files to avoid problems :>
                    self.downloadvideo.download(self.user_text) # Downloads the video
                    self.downloadvideo.renameFile() # Renames the .wav file
                    wav_file = self.downloadvideo.file # Get's the wav file path
                    s = aubio.source(wav_file)
                    samplerate = s.samplerate

                    win_s = 4096
                    hop_s = 512 

                    tolerance = 0.8

                    pitch_o = aubio.pitch("yin", win_s, hop_s, samplerate)
                    pitch_o.set_unit("midi")
                    pitch_o.set_tolerance(tolerance)

                    pitches = []

                    while True:
                        samples, read = s()
                        pitch = pitch_o(samples)[0]
                        pitches += [pitch]
                        if read < hop_s:
                            break
                    # Show on screen in Green text DOWNLOADING VIDEO...
                    return wav_file, pitches
                except:
                    failed = True

            if exit_button.draw():
                print("Exit")
                run = False

            pygame.display.flip()
            
        pygame.quit()
