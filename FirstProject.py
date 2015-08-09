import pygame
import display

pygame.init()

clock = pygame.time.Clock()
display = display.Display()

gameExit = False

while not gameExit:
    #Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    display.update()
    clock.tick(30)
    
pygame.quit()
quit()
