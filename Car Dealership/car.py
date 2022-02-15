# Dhruv Patel
# Dec 20th, 2021
# Car Class

class Car:

    def __init__(self, name, price, horsepower, engineType, bodyType, carType):

        self.__name = name
        self.__price = price
        self.__horsepower = int(horsepower)
        self.__engineType = engineType
        self.__bodyType = bodyType
        self.__carType = carType

    # getters and setters.
    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getHorsepower(self):
        return self.__horsepower

    def getEngineType(self):
        return self.__engineType

    def getBodyType(self):
        return self.__bodyType

    def getCarType(self):
        return self.__carType

    def setName(self, name):
        self.__name = name

    def setPrice(self, price):
        self.__price = price

    def setHorsepower(self, horsepower):
        self.__horsepower = horsepower

    def setEngineType(self, type):
        self.__engineType = type

    def setBodyType(self, type):
        self.__bodyType = type

    def setCarType(self, type):
        self.__carType = type

    def toString(self):
        # to string.
        return """
        Name: {}
        Price: ${}
        Horsepower: {}
        Engine Type: {}
        Body Type: {}
        Car Type: {}""".format(self.__name, self.__price, self.__horsepower, self.__engineType, self.__bodyType, self.__carType)
