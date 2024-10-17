



class Auto:

    def __init__(self):
        super().__init__()
        self.test = "grün"
        self.__farbe = "rot"

    def getFarbe(self):
        return self.__farbe

    def setFarbe(self, value):
        self.__farbe = value




auto = Auto()

print(auto.test)
print(auto.getFarbe())
auto.setFarbe("gelb")
print(auto.getFarbe())