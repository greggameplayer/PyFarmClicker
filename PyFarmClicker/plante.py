import random


class Legume:
    def __init__(self, Nom, PrixAchat, PrixVente, ProbaVente):
        self.__Nom = Nom
        self.__PrixAchat = PrixAchat
        self.__PrixVente = PrixVente
        self.__ProbaVente = ProbaVente

    def getNom(self):
        return self.__Nom

    def getPrixAchat(self):
        return float(self.__PrixAchat)

    def vendre(self):
        rd = random.randint(0, 100)

        if rd <= self.__ProbaVente * 100:
            return self.__PrixVente
        else:
            return 0


class Fleur(Legume):
    def __init__(self, Nom, PrixAchat, PrixVente, ProbaVente, Couleur):
        Legume.__init__(self, Nom, PrixAchat, PrixVente, ProbaVente)
        self.__couleur = Couleur

    def getCouleur(self):
        return self.__couleur


Legumes = [
    Legume("courgette", 0.5, 2, 0.75),
    Legume("tomate", 0.4, 3, 0.5),
    Legume("patate", 0.9, 1.5, 0.9),
]
Fleurs = [
    Fleur("tulipe", 2, 4, 0.80, "rose"),
    Fleur("rose", 3, 7, 0.5, "rouge"),
    Fleur("muguet", 1, 2, 0.9, "blanc"),
]


def getLegumesNames():
    legumeNamesArray = []
    for legume in Legumes:
        legumeNamesArray.append(legume.getNom())
    return legumeNamesArray


def getFlowersNames():
    flowersNamesArray = []
    for fleur in Fleurs:
        flowersNamesArray.append(fleur.getNom())
    return flowersNamesArray


def getFlowerColors():
    flowerColorsArray = []
    for flower in Fleurs:
        flowerColorsArray.append(flower.getCouleur())
    return flowerColorsArray


def getFashionFlowerColor():
    return random.choice(getFlowerColors())


def getPlantes():
    plantes = []
    plantes.extend(Legumes)
    plantes.extend(Fleurs)
    return plantes
