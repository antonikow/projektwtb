"""
Modul zawierajacy klase zapewniajaca GUI i glowne dzialanie programu.
"""

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QDialog, QWidget, QLabel, QLineEdit
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT, FigureCanvasQTAgg
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from PackageNewton.NewtonClass import Newton 



class MainWindow(QWidget):
    """
    Klasa tworzaca glowne okno GUI, zapewniajaca calosc dzialania programu.
    """
    def __init__(self) -> None:
        """
        Konstruktor wywolujacy metody zapewniajace oczekiwana funkcjonalnosc calego programu.
        """
        super().__init__()
        self.__objectID = randint(0,1000000)
        self.set_window_size()
        self.setWindowTitle("Ekstremum funkcji jednej zmiennej - Metoda Newtona(stycznych)")
        self.gui()
        
    def set_window_size(self) -> None:
        """
        Metoda ustawiajaca rozmiar okna.
        """
        self.__width = 1100
        self.__height = 700
        self.setFixedSize(self.__width, self.__height) 
        
    def gui(self) -> None:
        """
        Metoda przygotowujaca GUI.
        """
        self.__fig = plt.figure()
        self.__canvas = FigureCanvasQTAgg(self.__fig)
        self.__toolbar = NavigationToolbar2QT(self.__canvas, self)
        self.__pathtext = QLabel("Sciezka: ")
        self.__pathline = QLineEdit()
        self.__komunikat = QLabel()
        self.__draw_button = QPushButton("rysuj")
        self.__draw_button.clicked.connect(self.glowna_akcja)
        uklad = QVBoxLayout()
        uklad.addWidget(self.__toolbar)
        uklad.addWidget(self.__canvas)
        uklad.addWidget(self.__pathtext)
        uklad.addWidget(self.__pathline)
        uklad.addWidget(self.__komunikat)
        uklad.addWidget(self.__draw_button)
        self.setLayout(uklad)

    def plot_function(self) -> None:
        """
        Metoda rysujaca wykres funkcji bez ekstremum.
        """
        self.__fig.clf()
        ax = self.__fig.add_subplot(1,1,1)
        t = np.arange(self.__a, self.__b, 0.01)
        ax.plot(t,self.__f(t), label = self.__nazwa_funkcji)
        plt.legend(loc = "upper right")
        ax.grid()
        self.__canvas.draw()

    def plot_function_with_extremum(self, ekstr: ("ekstremum do zaznaczenia na wykresie", float)) -> None:
        """
        Metoda rysujaca wykres funkcji z ekstremum
        """
        self.__fig.clf()
        ax = self.__fig.add_subplot(1,1,1)
        t = np.arange(self.__a, self.__b, 0.01)
        ax.plot(t,self.__f(t), label = self.__nazwa_funkcji)
        plt.legend(loc = "upper right")
        ax.grid()
        plt.plot(ekstr,self.__f(ekstr),"r.", markersize = 12)
        self.__canvas.draw()

    def plot_wyczysc(self) -> None:
        """
        Metoda czyszczaca wykres.
        """
        self.__fig.clf()
        ax = self.__fig.add_subplot(1,1,1)
        self.__canvas.draw()

    def use_newton(self) -> None:   
        """
        Metoda tworzaca obiekt klasy Newton, ktory dokonuje niezbedne obliczenia 
        poszukiwania ekstremum, metoda ta zwraca ekstremum i liczbe iteracji wykonanych do jego znalezienia.
        """
        newton = Newton(self.__f, self.__a, self.__b, self.__eps)     
        return newton.my_extremum(), newton.my_iterations()
  
    def glowna_akcja(self) -> None:
        """
        Glowna metoda, metoda wczytujaca dane na podstawie podanej sciezki do tworzonych przez siebie atrybutow, ktore potem stanowią argumenty w metodzie Newtona.
        Metoda wywoluje metode Newtona, w roznego rodzaju wyjatkach przerywa dzialanie sygnalizujac w GUI rodzaj bledu, w zaleznosci od wyniku dzialania tej metody
        metoda wywoluje odpowiedni rodzaj metody rysujacej wykres.
        """
        try:
            sciezka = r"{}".format(self.__pathline.text())  
            loaded_f = np.loadtxt(sciezka, delimiter=";", usecols=0, dtype=str)
            loaded_f = str(loaded_f)
            loaded_f = loaded_f.replace(" ", "")
        except:
            self.__komunikat.setText("Nieprawidlowa sciezka")
            self.plot_wyczysc()
            return
        try:
            self.__nazwa_funkcji = loaded_f
            self.__f = lambda x : eval(loaded_f)
            loaded_a = np.loadtxt(sciezka, delimiter=";", usecols=1, dtype=str)
            loaded_b = np.loadtxt(sciezka, delimiter=";", usecols=2, dtype=str)
            loaded_eps = np.loadtxt(sciezka, delimiter=";", usecols=3, dtype=str)
            self.__a = eval(str(loaded_a))
            self.__b = eval(str(loaded_b))     
            self.__eps = eval(str(loaded_eps))
            ekstr, it = self.use_newton()
        except:
            self.__komunikat.setText("Nieprawidlowe dane w pliku")
            self.plot_wyczysc()
            return
        if ekstr != "brak ekstremum":
            self.plot_function_with_extremum(ekstr)
            self.__komunikat.setText("Ekstremum: " + str(ekstr) + " Iteracje: " + str(it))        
        else:
            self.plot_function()
            self.__komunikat.setText("Brak Ekstremum")

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