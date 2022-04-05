import pygame

#Initiailze pygame
pygame.init()

#Create a display surface and set its caption
# set constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello World!")

#The main game loop
running = True
while running:
    #Loop through a list of Event objects that have occured
    # in pygame, a click or a key stroke is an event, as well as mouse movement or
    # QUIT, ACTIVEEVENT, KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONUP, VIDEORESIZE, USEREVENT, etc.
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

#End the game
pygame.quit()