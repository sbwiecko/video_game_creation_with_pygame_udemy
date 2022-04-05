# This project is a variation of the preceeding script while:
# * adding sound effect on collision
# * background music
# * some text, e.g., a score panel

import pygame, random

#Initialize Pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 100 + 300 # score panel + game panel
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
VELOCITY = 5

# Initialize the score
SCORE = 0

# font
custom_font = pygame.font.Font('../basic_tutorial_assets/AttackGraffiti.ttf', 40)

#Load images
dragon_image = pygame.image.load("../basic_tutorial_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25 + 100) # below the score panel

coin_image = pygame.image.load("../basic_tutorial_assets/coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# Define the score text
score_text = custom_font.render("Score: 000", True, (255,255,0))
score_text_rect = score_text.get_rect()
score_text_rect.center = (WINDOW_WIDTH//2, 50)

#Load sound effects
sound_1 = pygame.mixer.Sound('../basic_tutorial_assets/sound_1.wav')

#Load background music and playin
pygame.mixer.music.load('../basic_tutorial_assets/music.wav')
pygame.mixer.music.play(-1, 0.0)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_UP] and dragon_rect.top > 100:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY
        
    #Check for collision between two rects
    if dragon_rect.colliderect(coin_rect):

        # play sound instead of printing 'HIT' on the command line
        sound_1.play()

        # add 1 point to the score
        # if displayed now, will disappear with display_surface.fill()
        SCORE += 1


        # put the coin rect in a random position within the surface
        coin_rect.x = random.randint(0, WINDOW_WIDTH - 32)
        coin_rect.y = random.randint(100, WINDOW_HEIGHT - 32)

    #Fill display surface
    display_surface.fill((0, 0, 0))

    #Blit assets
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    # simple line
    # bottom of the line should be on y=100
    pygame.draw.line(display_surface, (255, 255, 255), (0, 98), (WINDOW_WIDTH, 98), 4)

    # score
    score_text = custom_font.render(f"Score: {SCORE:03d}", True, (255,255,255))
    display_surface.blit(score_text, score_text_rect)
    # pygame.draw.rect(display_surface, (0, 255, 0), score_text_rect, 1)

    #Update display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)

#End the game
pygame.mixer.music.stop() # not sure this is really necessary
pygame.quit()