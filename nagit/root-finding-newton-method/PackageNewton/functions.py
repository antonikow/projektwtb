"""
Modul zawierajacy funkcje ktore nie wchodza w sklad zadnej z obecnych w projekcie klas. 
"""
def diff1(f: "funkcja f, uzyta funkcja", h: ("wspolczynnik h"), x: ("argument funkcji f", float)) -> ("pierwsza pochodna w punkcie", float):  
    """
    Funkcja zwracajaca wartosc pierwszej pochodnej w punkcie dla argumentow  obliczana funkcja, wielkosc h i wartosci argumentu wczesniej podanej funkcji.
    """
    return (f(x+h)-f(x-h) )/(2*h)

def diff2(f: "funkcja f, uzyta funkcja", h: ("wspolczynnik h"), x: ("argument funkcji f", float)) -> ("druga pochodna w punkcie", float):  
    """
    Funkcja zwracajaca wartosc drugiej pochodnej w punkcie dla argumentow  obliczana funkcja, wielkosc h i wartosci argumentu wczesniej podanej funkcji.
    """
    return (f(x+h)-2*f(x)+f(x-h))/h**2
