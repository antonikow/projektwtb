"""
Modul zawierajacy klase metody poszukiwania ekstremum funkcji.
"""
from PackageNewton.functions import diff1, diff2
from random import randint
from math import copysign

from AbstractClass import FindExtremumMethod

class Newton(FindExtremumMethod):
    """
    Klasa dziedziczaca po klasie abstrakcyjnej FindExtremumMethod, posiada przydatne metody np.: gettery, settery  i inne do obslugi klasy,
    oraz wlasciwa metode obliczajaca ekstremum i liczbe iteracji do jego znalezienia.
    """
    def __init__(self, f: "funkcja dla ktorej poszukiwane jest ekstremum", a: ("lewy kraniec przedzialu", float), \
                 b: ("prawy kraniec przedzialu", float), eps: ("dokladnosc poszukiwania ekstremum", float)) -> None:
        """
        Konstruktor inicjalizujacy atrybuty przechowujace wynik funkcji znajdujacej ekstremum.
        """
        self.__objectID = randint(0,1000000)
        self.__numerical_method = "metoda newtona"
        self.__ekstremum, self.__it = self.find_extremum(f, a, b, eps)
        self.outcome()     #   przykladowe wykorzystanie dzialania mmetod odziedziczonych po bazowej klasie abstrakcyjnej
        self.whoami()      #   

    @property
    def ekstremum(self) -> float:
        """
        Dekorator wlasciwosci zwracajacy ekstremum.
        """
        return self.__ekstremum
    @property
    def it(self) -> int:
        """
        Dekorator wlasciwosci zwracajacy liczbe iteracji.
        """
        return self.__it

    def my_extremum(self) -> float:
        """
        Metoda zwracajaca atrybut ekstremum. 
        """
        return self.__ekstremum

    def my_iterations(self) -> int:
        """
        Metoda zwracajaca atrybut liczbe iteracji.
        """
        return self.__it

    def my_type(self) -> str:
        """
        Metoda zwracajaca atrybut informujace o nazwie metody.
        """
        return self.__numerical_method

    def outcome(self) -> None:
        """
        Metoda, wywolujaca metode bazowej klasy abstrakcyjnej FindExtremumMethod,
        w swoim dzialaniu wykorzystuje mechanizm polimorfizmu i wypisuje na konsole wyniki dzialania metody poszukiwania ekstremum.
        """
        super().outcome()

    def whoami(self) -> None:
        """
        Metoda, wywolujaca metode bazowej klasy abstrakcyjnej FindExtremumMethod,
        w swoim dzialaniu wykorzystuje mechanizm polimorfizmu i wypisuje na konsole nazwe metody poszukiwania ekstremum.
        """
        super().whoami()    # przeciazenie metody klasy bazowej nie zmienia dzialania,
                            # ale dla innego typu jest wywolywana inna funkcja - polimorfizm (w Pythonie wymuszony, bez przeciazenie program by nie dzial )

    def find_extremum(self, f: "funkcja dla ktorej poszukiwane jest ekstremum", a: ("lewy kraniec przedzialu", float), \
        b: ("prawy kraniec przedzialu", float), eps: ("dokladnosc poszukiwania ekstremum", float)) -> None:
        """
        Metoda na podstawie podanych atrybutow zwraca wartosc ekstremum i liczbe iteracji do jego znalezienia.
        """
        h = 10 ** (-5)
        sign = lambda x : copysign(1, x)
        if sign(f(a)) == sign(diff2(f, h, a)):
            x0 = a
        else:
            x0 = b
        xm = x0 - (diff1(f, h, x0)/diff2(f, h, x0))
        it = 0
        if( (a < xm and xm < b) and f(xm) < f(a) and f(xm) < f(b)):
            pass
        else:
            return "brak ekstremum", it 
        while True:
            it += 1
            xm=x0-(diff1(f, h, x0)/diff2(f, h, x0)) 
            if abs(diff1(f, h, xm)) < eps:
                break
            x0 = xm
        return xm, it 

    def __hash__(self) -> int:
        """
        Metoda zwraca wartosc hash obiektu.
        """
        return  self.__objectID

    def __str__(self) -> str:
        """
        Metoda zwraca nieoficjalna reprezentacje obiektu o typie str.
        """
        return "ID={}".format(self.__objectID)

    def __repr__(self) -> str:
        """
        Metoda zwraca oficjalna reprezentacje obiektu o typie str.
        """
        return "ID={}".format(self.__objectID)
    
