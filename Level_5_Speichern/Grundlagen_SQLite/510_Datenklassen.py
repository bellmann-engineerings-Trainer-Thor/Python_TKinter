

###############################################################################################
#                                        Datenklasse
# der einzige Zweck einer Datenklasse ist es Daten zu halten.
# Es ist ein ganz normales Objekt ohne besonderheiten
###############################################################################################
class Datenklasse:
    def __init__(self, id, name, adresse):
        self.id = id
        self.name = name
        self.adresse = adresse

    def __str__(self):
        return f'Datenklasse(id={self.id}, name={self.name}, adresse={self.adresse})'

data = Datenklasse(1,"peter", "adresse")
print(data)


###############################################################################################
#                                        Kurzform
# weil Datenklassen so oft gebraucht werden hatten die Python-Entwickler dieses Geschenk für uns.
###############################################################################################

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    lebensalter: int
    beruf: str

object = Person(name= "Peter", lebensalter=12, beruf="Schüler")
print(object)