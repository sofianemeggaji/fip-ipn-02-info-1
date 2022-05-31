from enum import Enum


class Ingredients(Enum):
    Mango = "Mango"
    Orange = "Orange"
    Guajana = "Guajana"
    Apple = "Apple"
    Ginger = "Ginger"
    Lemon = "Lemon"
    Guava = "Guava"
    Pineapple = "Pineapple"
    Banana = "Banana"
    Carrot = "Carrot"
    Celery_Stick = "Celery stick"
    Beetroot = "Beetroot"


class Taille(Enum):
    Small = 0
    Medium = 1
    Large = 2

    def choixtaille(self,s):
        if(s == "Small"):
            return Taille.Small
        if(s == "Medium"):
            return Taille.Medium
        if(s == "Large"):
            return Taille.Large

class Jus:
    _name = ""
    _price = 0
    _sizeFactor = 0
    _listeIngredients = []
    _listeQuantite = []

    def __init__(self, name, price, taille, listeIngredients, listeQuantite, debug=False):
        self._name = name
        self._price = price + (0.5 * taille.value)
        self._listeIngredients = listeIngredients
        self._listeQuantite = listeQuantite
        if debug:
            print(self._name)
            print(self._listeIngredients)
            print(self._listeQuantite)
            print(self._price)

    @property
    def getName(self):
        return self._name
    @property
    def getPrice(self):
        return self._price
    @property
    def getListeIngredients(self):
        return self._listeIngredients
    @property
    def getListeQuantite(self):
        return self._listeQuantite

class Commande :
    _totalPrice = 0
    _jusListe = []

    def __init__(self,debug=False):
        self._jusListe = []
        self._totalPrice = 0
        if debug :
            print(self._jusListe)
            print(self._totalPrice)

    def choixproduit(self,j,debug=False):
        taille = Taille.choixtaille(None,input("taille : "))
        if debug :
            print(taille)
        self._jusListe.append( Juice(j.getName,j.getPrice,taille,j.getListeIngredient,j.getListeQuantite,debug) )
        self._totalPrice += self._jusliste[-1].getPrice


    def afficherpanier(self):
        for i in self._jusListe:
            print("\"" + i.getName + "\"-" + str(i.getPrice) + "$|")

    @property
    def pricetotal(self):
        return self._totalPrice

class Barmaid() :
    _Commande = None
    _jusDispo = None
    def __init__(self):
        self._Commande = None
        self._jusDispo = [
            Juice("The Boost", 5, Taille.Small, [Ingredient.Mango, Ingredient.Orange, Ingredient.Guajana], [0.5, 2, 1]),
            Juice("The Fresh", 4, Taille.Small, [Ingredient.Apple, Ingredient.Ginger, Ingredient.Lemon], [3, 1, 1]),
            Juice("The Fusion", 5, Taille.Small, [Ingredient.Guava, Ingredient.Pineapple, Ingredient.Banana], [1, 0.25, 0.5]),
            Juice("The Detox", 3.5, Taille.Small, [Ingredient.Carrot, Ingredient.Celery_Stick, Ingredient.Beetroot], [3, 1, 1])
        ]
    def createOrder(self,debug=False):
        self._Commande = Commande(debug)
    def addToOrder(self,debug=False):
        userChoice = input("Jus : ")
        while( userChoice != "annuler" and userChoice != "fin") :
            for i in self._jusDispo:
                if userChoice == i.getName:
                    jusToAdd = i
                    if debug :
                        print("jus existe")
                    break
            self._Commande.choixproduit(jusToAdd,debug)
            self._Commande.afficherpanier()

            userChoice = input("Jus : ")
        if userChoice == "annuler" :
            self._Commande = None
            print("commande annuler")
        if userChoice == "fin":
            print("commande finaliser")
            print("Le montant est de : " + str(self._Commande.getTotalPrice ) + "$" )

    def affichercommande(self):
        print(self._Commande)

if __name__ == '__main__':
    DEBUG = True
    b = Barmaid()
    b.createOrder()
    b.addToOrder()