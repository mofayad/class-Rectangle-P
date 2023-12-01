class Rectangle :
    _NbrRectangles = 0

    def __init__(self, largeur=0, longueur=0):
        self._largeur = largeur
        self._longueur = longueur
        Rectangle._NbrRectangles += 1

    def getLargeur(self):
        return self._largeur
    
    def setLargeur(self, largeur):
        self._largeur = largeur
    
    def getLongueur(self):
        return self._longueur
    
    def setLongueur(self, longueur):
        self._longueur = longueur

    def getNbrR(self):
        return self._NbrRectangles
    
    def Perimetre(self):
        perimetre = 2 * (self._largeur + self._longueur)
        return perimetre
    
    def Surface(self):
        surface = self._largeur * self._longueur
        return surface
    
    def Equals(self, Rec):
        return self._largeur == Rec.getLargeur() and self._longueur == Rec.getLongueur()
    
    def ToString(self):
        print(f"La largeur est: {self._largeur} \n La longueur est: {self._longueur}" )



Rec1 = Rectangle(3,4)
Rec2 = Rectangle(5,6)
print(Rec1.Equals(Rec2))
print(Rec1.ToString())
print(Rec1.Surface())
print(Rec1.Perimetre())