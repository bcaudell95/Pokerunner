import pygame

# Game Elements
backdropFiles = ['assets/images/backdrop.png', 'assets/images/backdrop1.png']
backdrops = [pygame.image.load(file) for file in backdropFiles]

scoreBorderImage = pygame.image.load('assets/images/ScoreBorder.png')
basicObstacle = pygame.image.load('assets/images/basicObstacle.png')
heartImage = pygame.image.load('assets/images/heart.png')

# Pause Screen Elements
pauseScreenOverlay = pygame.image.load('assets/images/Pause.png')

# Main Menu Elements
mainMenuBackdropImage = pygame.image.load('assets/images/MainMenu.png')
START_BUTTON_IMAGES_FILES = ['assets/images/Start_on.png', 'assets/images/Start_off.png']

# Credits Elements
creditsBackdropImage = pygame.image.load('assets/images/GameOver.png')