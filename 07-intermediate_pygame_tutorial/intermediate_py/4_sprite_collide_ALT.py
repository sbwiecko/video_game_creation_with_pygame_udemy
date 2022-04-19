"""
An alternative version of the 4_sprite_collide.py file
where the Player object, unique in that case, is not
added into a group, to test whether it is mandatory to
create a group for an unique Sprite object.
"""
import pygame, random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sprite Goups!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


#Define Classes
class Player(pygame.sprite.Sprite):
    """A simple class to represent a player who fights monsters"""
    def __init__(self, x, y, monster_group):
        super().__init__()
        self.image = pygame.image.load("../intermediate_tutorial_assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = 5

        # not necessarily need to give the `monster_group` as attribute
        # but easier to control/follow
        self.monster_group = monster_group

    # called at each frame
    def update(self):
        """Update the player"""
        self.move()
        self.check_collisions()

    def move(self):
        """Move the player continoulsy"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity

    def check_collisions(self):
        """Check for collisions between player (self) and the monster group"""
        # if `do_kill` arg set True, all sprite collided are removed
        if pygame.sprite.spritecollide(self, self.monster_group, True):
            print(len(self.monster_group))

    
class Monster(pygame.sprite.Sprite):
    """A simple class to represent a spooky monster"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../intermediate_tutorial_assets/blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 10)

    def update(self):
        """Update and move the monster"""
        self.rect.y += self.velocity


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
#Create a monster group and add 10 monsters
my_monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i*64, 10)
    my_monster_group.add(monster)

#Create a player group
# player_group = pygame.sprite.Group()
player = Player(500, 500, my_monster_group)
# player_group.add(player)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the display
    display_surface.fill((0, 0, 0))

    #Update and Draw assets
    # player_group.update()
    # player_group.draw(display_surface)
    player.update()
    display_surface.blit(player.image, player.rect)
    # it works perfectly well with one player outside of a group ;-)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()