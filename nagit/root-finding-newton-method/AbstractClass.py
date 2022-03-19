"""
Modul zawierajacy klase abstrakcyjna, po ktorej moga dziedziczyc
dowolne metody poszukiwania ekstremum funkcji jednej lub wielu zmiennych.
"""

from abc import ABC, abstractmethod

class FindExtremumMethod(ABC):
    """
    Abstrakcyjna klasa zawierajaca metody umozliwajace wglad w wyniki dzialania danej metody poszukiwania ekstremum funkcji. Zapewnia metody mozliwe do wykorzystania przez
    dowolne instancje metod poszukiwania ekstremum funkcji dowolnej liczby zmiennych.
    """
    @abstractmethod
    def my_extremum(self) -> None:
        """
        Metoda klasy abstrakcyjnej stanowiaca "wzorzec" do wykorzystania przez klasy potomne w ktorych jest wywolywana, informuje o wartosc ekstremum.
        """
        pass

    @abstractmethod
    def my_iterations(self) -> None:
        """
        Metoda klasy abstrakcyjnej stanowiaca "wzorzec" do wykorzystania przez klasy potomne w ktorych jest wywolywana, informuje o liczbie iteracji.
        """
        pass

    @abstractmethod
    def my_type(self) -> None:
        """
        Metoda klasy abstrakcyjnej stanowiaca "wzorzec" do wykorzystania przez klasy potomne w ktorych jest wywolywana,
        informuje o nazwie metody poszukiwania ekstremum funkcji.
        """
        pass

    @abstractmethod
    def outcome(self) -> None:
        """
        Metoda klasy abstrakcyjnej stanowiaca "wzorzec" do wykorzystania przez klasy potomne w ktorych jest wywolywana, 
        wypisuje na ekran konsoli znalezione ekstremum i liczbe iteracji.
        """
        print("Ekstremum: ", self.my_extremum() , " Iteracje: ", self.my_iterations())

    @abstractmethod
    def whoami(self) -> None:
        """
        Metoda klasy abstrakcyjnej stanowiaca "wzorzec" do wykorzystania przez klasy potomne w ktorych jest wywolywana,
        wypisuje na ekran konsoli nazwe metody poszukiwania ekstremum funkcji.
        """
        print("Metoda: ", self.my_type())
