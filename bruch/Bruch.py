"""
Created on 18.09.2017

@author: Michael Borko <mborko@tgm.ac.at>
@version: 20170918

@description: Implementierung einiger Operationen, um das Rechnen mit Bruechen zu ermoeglichen
"""

class Bruch(object):
    """
    Konstruktor
    :type zaehler: Zaehler des Bruchs
    :type nenner: Nenner des Bruchs
    """
    def __init__(self, zaehler=None, nenner=None):
        # Klassenaufruf: Bruch(2,4)
        if isinstance(zaehler, int) and isinstance(nenner, int):
            # --> Division durch 0 ueberpruefen
            if nenner != 0:
                self.zaehler = zaehler
                self.nenner = nenner
            elif zaehler < 0 and nenner < 0:
                self.zaehler = abs(zaehler)
                self.nenner = abs(nenner)
            else:
                raise ZeroDivisionError("Division durch 0 nicht definiert!")

        # Klassenaufruf: self.b2 = Bruch(self.b)
        # --> Zuweisen von Zaehler und Nenner aus dem Bruchobjekt
        elif isinstance(zaehler, Bruch):
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner

        # Klassenaufruf: Bruch(4)
        # --> ohne Nenner, daher Deklarierung von Nenner = 1
        elif isinstance(zaehler, int) and not isinstance(nenner, float):
            self.zaehler = zaehler
            self.nenner = 1

        else:
            raise TypeError("Zaehler und/oder Nenner nicht zulaessig!")


    ## Unit_Allgemein
    def __float__(self):
        erg = float(self.zaehler) / float(self.nenner)
        return erg

    def __int__(self):
        erg = int(self.zaehler) / int(self.nenner)
        return erg

    def __complex__(self):
        erg = complex(self.zaehler) / complex(self.nenner)
        return erg

    def __invert__(self):
        z1 = self.zaehler
        n1 = self.nenner
        z2 = n1
        n2 = z1
        return Bruch(z2,n2)

    def __pow__(self, power):
        tempz = self.zaehler**power
        tempn = self.nenner**power
        return Bruch(tempz,tempn)

    def __abs__(self):
        tempz = abs(self.zaehler)
        tempn = abs(self.nenner)
        return Bruch(tempz, tempn)

    def __neg__(self):
        tempz = abs(self.zaehler)
        tempn = abs(self.nenner)
        return Bruch(tempz, tempn)

    def _Bruch__makeBruch(cls, value):
        if type(value) is str:
            raise TypeError
        return Bruch(value)

    ## Unit_Addition
    def __add__(self, other):
        if type(other) is float:
            raise TypeError
        else:
            erg = float(self) + float(other)
        return erg

    def __radd__(self, other):
        erg = float(self) + float(other)
        return erg

    def __iadd__(self, other):
        if type(other) is str:
            raise TypeError
        else:
            temp = float(self) + float(other)
            temp1 = int(temp*self.nenner)
        return Bruch(temp1, self.nenner)


    ## Unit_Division
    def __div__(self, other):
        if type(other) is float:
            raise TypeError
        return float(self) / float(other)

    def __rtruediv__(self, other):
        if self.zaehler is 0:
            raise ZeroDivisionError
        if type(other) is float:
            raise TypeError
        return float(self) / float(other)

    def __itruediv__(self, other):
        if type(other) is str:
            raise TypeError
        return self/other

    ## Unit_Multiplikation
    def __mul__(self, other):
        if type(other) is float:
            raise TypeError
        else:
            return float(self) * float(other)

    def __imul__(self, other):
        if type(other) is str:
            raise TypeError
        else:
            return float(self) * float(other)

    def __rmul__(self, other):
        return float(self) * float(other)

    ## Unit_String
    def __str__(self):
        tempz = str(abs(self.zaehler))
        tempn = str(abs(self.nenner))
        return "("+tempz+"/"+tempn+")"

    ## Unit_Subtraktion
    def __sub__(self, other):
        return float(self) - float(other)

    def __rsub__(self, other):
        if type(other) is float:
            raise TypeError
        return float(other) - float(self)

    def __isub__(self, other):
        if type(other) is str:
            raise TypeError
        else:
            temp = float(self) - float(other)
            temp1 = int(temp*self.nenner)
        return Bruch(temp1, self.nenner)

    ## Unit__Vergleich
    def __eq__(self, other):
        if float(self) == float(other):
            return True
        else:
            return False


    def __ge__(self, other):
        if float(self) >= float(other):
            return True
        else:
            return False

    def __le__(self, other):
        if float(self) <= float(other):
            return True
        else:
            return False

    def __lt__(self, other):
        if float(self) < float(other):
            return True
        else:
            return False

    def __gt__(self, other):
        if float(self) > float(other):
            return True
        else:
            return False

    ## Unit_Zusatz
