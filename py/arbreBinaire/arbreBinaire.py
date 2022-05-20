class arbreBinaire:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.parent = None
        self.droite = None
        self.gauche = None

    def GetData(self):
        return self.data

    def addElement(self, dataAdd):
        if dataAdd < self.data:
            if self.gauche == None:
                self.gauche = arbreBinaire(dataAdd)
                self.gauche.parent = self
            else:
                self.gauche.addElement(dataAdd)
        elif dataAdd > self.data:
            if self.droite == None:
                self.droite = arbreBinaire(dataAdd)
                self.droite.parent = self
            else:
                self.droite.addElement(dataAdd)

    def getAllFormTable(self):
        print(self.data)
        if self.gauche != None:
            self.gauche.getAllFormTable()
        if self.droite != None:
            self.droite.getAllFormTable()


# fonction find(A,e)
#         Si A = .
#             retourner Faux
#         Sinon A = (x,FilsGauche,FilsDroit)
#             Si x = e
#                 retourner Vrai
#             Sinon si e < x
#                 retourner Recherche(FilsGauche,e)
#             Sinon
#                 retourner Recherche(FilsDroit,e)

arbre = arbreBinaire(25)
arbre.addElement(44)
arbre.addElement(23)
arbre.addElement(26)
arbre.addElement(22)
arbre.addElement(24)
arbre.getAllFormTable()
