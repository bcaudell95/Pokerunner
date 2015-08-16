import pygame
import display
import player

pygame.init()

clock = pygame.time.Clock()
display = display.Display()
myPlayer = player.Player()

gameExit = False

while not gameExit:
	#Handle Events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				myPlayer.changeMovementState(player.MovementStates.JUMPING)
			elif event.key == pygame.K_DOWN:
				myPlayer.changeMovementState(player.MovementStates.RUNNING)

	myPlayer.stepFrame()
	display.updatePlayerData(myPlayer.getCurrentPlayerState())
	display.updateScreen()
	clock.tick(30)
	
pygame.quit()
quit()
