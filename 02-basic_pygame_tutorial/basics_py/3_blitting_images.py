import pygame

#Initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images!")

"""
Pygame has a display Surface. This is basically an image that is visible on the screen,
and the image is made up of pixels. The main way you change these pixels is by calling
the blit() function. This copies the pixels from one image onto another.

This is the first thing to understand. When you blit an image onto the screen, you are
simply changing the color of the pixels on the screen. Pixels aren't added or moved,
we just change the colors of the pixels already on the screen. These images you blit
to the screen are also Surfaces in pygame, but they are in no way connected to the
display Surface. When they are blitted to the screen they are copied into the display,
but you still have a unique copy of the original.
"""

#Create images...returns a SURFACE OBJECT with the image drawon on it.
#We can then get the RECT of the surface and use the rect to position the image.
# icon downloaded from IconArchive with the format 64x64
dragon_left_image = pygame.image.load("../basic_tutorial_assets/dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()

dragon_right_image = pygame.image.load("../basic_tutorial_assets/dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
print(f"initial dragon_right_rect:{dragon_right_rect}")

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit (copy) a surface object at the given coordinates to our display surface
    # multiple ways to position an image rect
    dragon_left_rect.topleft = (0,0)
    dragon_right_rect.topright = (WINDOW_WIDTH, 0)

    # blit stands for "Block Transfer", or the copy of the content of one surface
    # to another surface at a defined position
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    # simple line
    pygame.draw.line(display_surface, (255, 255, 255), (0, 75), (WINDOW_WIDTH, 75), 4)

    #Update the display
    pygame.display.update()

print(f"final dragon_right_rect:{dragon_right_rect}")

#End the game
pygame.quit()