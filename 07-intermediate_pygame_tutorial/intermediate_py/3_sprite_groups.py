import pygame, random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sprite Goups!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


#Define Classes (see https://www.pygame.org/docs/ref/sprite.html)
# inherits from the pygame Sprite class
class Monster(pygame.sprite.Sprite):
    """A simple class to represent a spooky monster"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../intermediate_tutorial_assets/blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 10)

    # update method is mandatory for Sprite.Group calls !
    def update(self):
        """Update and move the monster"""
        self.rect.y += self.velocity


#Create a monster group and add 10 monsters
# Group makes it easier to test, update and
# draw many sprites at once
"""
pygame.sprite.Group.update() and pygame.sprite.Group.draw() are methods which are provided 
by pygame.sprite.Group. The former delegates the to the update method of the contained 
pygame.sprite.Sprites - you have to implement the method.

pygame.sprite.Group.update():
Calls the update() method on all Sprites in the Group.

The later uses the image and rect attributes of the contained pygame.sprite.Sprites to draw 
the objects - you have to ensure that the pygame.sprite.Sprites have the required attributes

pygame.sprite.Group.draw():
Draws the contained Sprites to the Surface argument. This uses the Sprite.image attribute 
for the source surface, and Sprite.rect for the position.
"""
monster_group = pygame.sprite.Group()
for i in range(20):
    monster = Monster(i*64, 10)
    monster_group.add(monster)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the display
    display_surface.fill((0, 0, 0))

    #Update and Draw assets
    monster_group.update()
    monster_group.draw(display_surface)

    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)


#End the game
pygame.quit()