import pygame

#Initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Continuous Movement!")

#Set FPS and clock
# slow down the main while loop + ensure it runs same speed on every computer
FPS = 60
# Creates a new Clock object that can be used to track an amount of time.
# The clock also provides several functions to help control a game's framerate.
clock = pygame.time.Clock()

#Set game values
VELOCITY = 5

#Load images
dragon_image = pygame.image.load("../basic_tutorial_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()
    # gives a tuple of 0 and 1 for each key position
    # so that we know each iteration if a key is pressed.
    # Using pressed will be true as long as the key is pressed,
    # in contrast, pygame.KEYDOWN events are only fired when the key is first pressed.
    print(keys)
    

    #Move the dragon continuously
    # pressing continuously a key is not a native event!
    if keys[pygame.K_LEFT]:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT]:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_UP]:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_DOWN]:
        dragon_rect.y += VELOCITY
    
    #Fill the display
    display_surface.fill((0, 0, 0))

    #Blit assets
    display_surface.blit(dragon_image, dragon_rect)

    #Update the display
    pygame.display.update()

    #Tick the clock
    # This method should be called once per frame.
    # It will compute how many milliseconds have passed since the previous call.
    # If you pass the optional framerate argument the function will delay
    # to keep the game running slower than the given ticks per second.
    clock.tick(FPS)

#End the game
pygame.quit()