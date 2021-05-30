class Question:

    id = 0

    def __init__(self, data):
        self.__data = data
        self.__id = Question.id
        Question.id += 1

    @property
    def getData(self):
        return self.__data

    @property
    def getId(self):
        return self.__id

    def __str__(self):
        return(str(self.getData))

