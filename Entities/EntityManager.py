from Entities.PlayerEntity import PlayerEntity


class EntityManager(object):
    def __init__(self):
        self.entities = []
        self.playerEntity = None

    def updateAll(self):
        for entity in self.entities:
            entity.tick()

    def addPlayerEntity(self):
        if self.playerEntity == None:
            self.playerEntity = PlayerEntity()
            self.entities.append(self.playerEntity)
        else:
            raise PlayerAlreadyInstantiatedException()

    def getPlayerEntity(self):
        if self.playerEntity != None:
            return self.playerEntity
        else:
            raise PlayerNotInstantiatedException()


class PlayerNotInstantiatedException(Exception):
    def __init__(self):
        super().__init__()


class PlayerAlreadyInstantiatedException(Exception):
    def __init__(self):
        super().__init__()
