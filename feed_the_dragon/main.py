import pygame

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the dragon")

FPS = 60
clock = pygame.time.Clock()

# GAME CONSTANTS
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

# COLORS
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font("fonts/AttackGraffiti.ttf")

score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Feed the Dragon", True, GREEN, DARKGREEN)
title_rect = title_text.get_rect()
title_rect.midtop = (WINDOW_WIDTH//2, 10)

lives_text = font.render("Lives: " + str(lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAME OVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("GAME OVER", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32)

# SOUNDS
# coin_sound = pygame.mixer.Sound("sounds/coin_sound.wav")
# miss_sound = pygame.mixer.Sound("sounds/miss_sound.wav")
# miss_sound.set_volume(0.1)
# pygame.mixer.music.load("sounds/music.wav")


# IMAGES
player_image = pygame.image.load("images/dragon_right.png")
player_rect = player_image.get_rect()

# MAIN LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
