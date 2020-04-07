class Animal:
    def __init__(self, nom, prixAchat, cri, gain, gainmin, gainmax, age):
        self.__age = age
        self.__nom = nom
        self.__prixAchat = prixAchat
        self.__cri = cri
        self.__gain = gain
        self.__gainmin = gainmin
        self.__gainmax = gainmax
        self.__saisonDebut = 1
        self.__selled = False

    def getNom(self):
        return self.__nom

    def getSelled(self):
        return self.__selled

    def setSelled(self, state):
        self.__selled = state

    def getGain(self):
        return self.__gain

    def getProduction(self, saison):
        if self.__gainmin <= self.__age < self.__gainmax and (saison - self.__saisonDebut) % 4 == 0:
            return self.__gain
        else:
            return 0

    def getPrixAchat(self):
        return float(self.__prixAchat)

    def setSaisonDebut(self, saison):
        if saison == 1:
            self.__saisonDebut = 0
        else:
            self.__saisonDebut = saison

    def setAge(self, saison):
        if ((saison - self.__saisonDebut) % 4) == 0:
            self.__age += 1

    def vendre(self):
        if self.__nom == "Vache":
            if self.__gainmin <= self.__age < self.__gainmax:
                return 120
            else:
                return 50
        elif self.__nom == "Poule":
            if self.__age < 3:
                return 5
            elif self.__age <= 8:
                return 20
            else:
                return 0
        else:
            if self.__age < 3:
                return 15
            elif self.__age <= 5:
                return 50
            else:
                return 20


def getAnimaux():
    animaux = [Animal("Vache", 100, "meuuuuh", 10, 3, 10, 0),
               Animal("Poule", 10, "cotcot", 30, 2, 8, 0),
               Animal("Oie", 15, "kwac", 0, 0, 0, 0)]
    return animaux


def getAnimauxNames():
    animalNamesArray = []
    for animal in getAnimaux():
        animalNamesArray.append(animal.getNom())
    return animalNamesArray
