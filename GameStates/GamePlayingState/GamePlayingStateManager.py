import pygame
from GameStates.GameStates import GameState, StateTransition
from GameStates.GamePlayingState.GamePlayingDisplay import GamePlayingDisplay
from Entities.PlayerEntity import PlayerEntity, MovementStates
from Entities.EntityManager import EntityManager


class GamePlayingStateManager(object):
    SCORE_DELTA = 10

    def __init__(self, screen):
        self.display = GamePlayingDisplay(screen)
        self.entityManager = EntityManager()
        self.entityManager.addPlayerEntity()
        self.player = self.entityManager.getPlayerEntity()
        self.score = 0

    def tick(self):
        self.entityManager.updateAll()
        self.incrementScore()
        self.display.setScore(self.getScore())
        self.display.updatePlayerData(self.player.getCurrentPlayerState())
        self.display.updateScreen()

    def handleEvent(self, event):
        if self.isEventKeyDown(event):
            self.handleKeyEvent(event)

    def isEventKeyDown(self, event):
        return event.type == pygame.KEYDOWN

    def handleKeyEvent(self, event):
        if event.key == pygame.K_UP:
            self.player.changeMovementState(MovementStates.JUMPING)
        elif event.key == pygame.K_p:
            transitionToPaused()

    def reset(self):
        pass

    def incrementScore(self):
        self.score += GamePlayingStateManager.SCORE_DELTA

    def getScore(self):
        return self.score


def transitionToPaused():
    raise StateTransition(GameState.PAUSED)
