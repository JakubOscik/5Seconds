class Player:

    id = 0

    def __init__(self, name):
        self.__points = 0
        self.__name = name
        self.__id = Player.id
        Player.id += 1

    @property
    def getName(self):
        return self.__name

    @property
    def getPoints(self):
        return self.__points

    @property
    def getId(self):
        return self.__id

    def addPoints(self, points):
        self.__points += points

    def __str__(self):
        return "{}, Punkty: {}".format(self.getName, self.getPoints)

    def __eq__(self, other):
        return self.__name == other.__name
