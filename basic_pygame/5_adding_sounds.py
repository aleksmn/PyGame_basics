import pygame

#Initialize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pygame.display.set_caption('Adding Sounds!')

# Load sound effects
sound_1 = pygame.mixer.Sound('sounds/sound_1.wav')
sound_2 = pygame.mixer.Sound('sounds/sound_2.wav')

# Play the sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

# Change volume of a sound effect
sound_2.set_volume(0.1)
sound_2.play()

# Load background music
pygame.mixer.music.load('sounds/music.wav')

# Play and stop background music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(5000)
pygame.mixer.music.stop()


# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Update the display
    pygame.display.update()

# End the game
pygame.quit()