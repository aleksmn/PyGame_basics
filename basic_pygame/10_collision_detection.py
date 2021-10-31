import pygame
import random

#Initialize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pygame.display.set_caption('Collision Detection!')


# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load sound effects
sound_1 = pygame.mixer.Sound('sounds/sound_1.wav')
sound_1.set_volume(0.1)

# Load background music
pygame.mixer.music.load('sounds/music.wav')


# Play background music
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0.0)



# Set game values
VELOCITY = 5

# Load images
dragon_image = pygame.image.load("images/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

coin_image = pygame.image.load("images/coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH//2, WINDOW_HIGHT//2)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False

    # Get a list of all keys pressed down
    keys = pygame.key.get_pressed()

    # Move the dragon continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WINDOW_HIGHT:
        dragon_rect.y += VELOCITY

    # Check for collision between two rects
    if dragon_rect.colliderect(coin_rect):
        # print("Collision!!!")
        sound_1.play()
        coin_rect.left = random.randint(0, WINDOW_WIDTH - coin_rect.w)
        coin_rect.top = random.randint(0, WINDOW_HIGHT - coin_rect.h)

        
    # Fill display to cover old images
    display_surface.fill((BLACK))

    # Draw rectangles
    # pygame.draw.rect(display_surface, RED, dragon_rect, 1)
    # pygame.draw.rect(display_surface, RED, coin_rect, 1)

    # Blit image
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)
 
    # Update the display
    pygame.display.update()

    # Tick the clock 
    clock.tick(FPS)

# End the game
pygame.quit()