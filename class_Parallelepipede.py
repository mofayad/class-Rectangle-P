from class_Rectangle import Rectangle 
class Parallelepipede(Rectangle) :
    _NbrParallelepipedes = 0
    
    def __init__(self, largeur=0, longueur=0, hauteur=0):
        super().__init__()
        self.__hauteur = hauteur
        Parallelepipede._NbrParallelepipedes += 1

    def getHauteur(self):
        return self.__hauteur
    
    def setHauteur(self, hauteur):
        self.__hauteur = hauteur

    def getNbrP(self):
        return self._NbrParallelepipedes
    
    def Equals(self, Rec):
        return self.getLargeur() == Rec.getLargeur() and self.getLongueur() == Rec.getLongueur() and self.__hauteur == Rec.getHauteur()
    
    def Surface(self):
        return (self.getLargeur() + self.getLongueur() + self.__hauteur)*2
    
    def ToString(self):
                return f"La largeur est: {self.getLargeur()} \n La longueur est: {self.getLongueur()} \n La hauteur est: {self.__hauteur}" 

    def Volume(self):
         pass
    


Rec3 = Parallelepipede(7,8,9)
Rec4 = Parallelepipede(10,11,12)
print(Rec3.Equals(Rec4))
print(Rec3.ToString())
print(Rec3.Surface())
print(Rec3.Volume())