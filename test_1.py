import pygame
from sys import exit

# print(dir(pygame))
# print(pygame.__version__)
# print(pygame.__path__)



pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Игра!!!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()


