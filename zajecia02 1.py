dane = (2024, 'Python', 3.8) # 6. Mając daną krotkę dane = (2024, 'Python', 3.8), przypisz każdy element krotki do 
rok, jezyk, wersja = dane # odpowiednich zmiennych: rok, jezyk i wersja. Wyświetl te zmienne
print(rok)
print(jezyk)
print(wersja)

oceny = [4, 3, 5, 2, 5, 4] #7. Mając listę oceny = [4, 3, 5, 2, 5, 4], przypisz pierwszą wartość do zmiennej pierwsza, 
pierwsza, *srodek, ostatnia = oceny # ostatnią do ostatnia, a pozostałe do listy srodek. Wykorzystaj * do zgromadzenia 
print(pierwsza)# środkowych wartości. Wyświetl te zmienne.
print(srodek)
print(ostatnia)

info = ('Jan', 'Kowalski', 30, 'Polska', 'programista') #8. Dla krotki info = ('Jan', 'Kowalski', 30, 'Polska', 'programista'), przypisz imię do zmiennej 
imie, nazwisko, _, _, zawod = info #imie, nazwisko do nazwisko, a zawód do zawod, ignorując pozostałe wartości. Do 
#ignorowania wykorzystaj znak _. Wyświetl przypisane zmienne.

dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])#9. Mając zagnieżdżoną strukturę dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')]), przypisz 
rok = dane[0]                                         #rok do zmiennej rok, nazwę języka do jezyk, wersję do wersja i opis wersji do zmiennej opis. 
jezyk = dane[1][0]                                    #Wyświetl te zmienne.
wersja = dane[1][1]
opis = dane[1][2]
print(jezyk)

#10. Stwórz zmienną a oraz b, użyj przypisania z wieloma celami i przypisz im listę [1, 2, 3]: a = b = 
#[1, 2, 3]. Zmodyfikuj pierwszy element listy b przez przypisanie b[0] = 'zmieniono'. Wyświetl 
#obie listy a i b, a następnie wyjaśnij, dlaczego zmiana w b wpłynęła również na a. Czy listy są 
#obiektami mutowalnymi? 
a = b = [1, 2, 3]
b[0] = 'zmieniono'
print(b)

# 11. Korzystając z poprzedniego przykładu, utwórz zmienną c i przypisz jej kopię listy a (możesz 
# użyć metody list() lub składni a[:]). Następnie zmodyfikuj pierwszy element w c i przypisz mu 
# wartość 'nowa wartość'. Wyświetl listy a, b i c, zauważając, że tym razem zmiana w c nie 
# wpłynęła na a ani b. Wyjaśnij, dlaczego kopiowanie listy zapobiegło współdzieleniu 
# referencji. 
c = list(a)
c[0] = "siema"
print(c)

# 12. Utwórz zmienną x oraz y, przypisz im wartość 10 poprzez x = y = 10. Zwiększ wartość y o 1 
# (np. y = y + 1). Wyświetl wartości x i y, a następnie wyjaśnij, dlaczego modyfikacja y nie 
# wpłynęła na wartość x. Czy integery są obiektami mutowalnymi? 
x = y = 10
y= y +1
print(x)

# 13. Wyzwól następujący kod, wyświetl K, L, M i N. Wyjaśnij w jaki sposób konkatenacja 
# zachowuje się inaczej od przypisania rozszerzonego. 
K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]
print(K)
print(L)
print(M)
print(N)

# 4. Mając dwie listy, imiona = ['Anna', 'Jan', 'Ewa'] i oceny = [5, 4, 3], użyj zip do stworzenia 
# pary każdego imienia z odpowiadającą mu oceną. Następnie, iteruj przez te pary, 
# wyświetlając imię wraz z oceną. Co się stanie, jeśli listy będą miały różne długości? 
imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3]
pary = zip(imiona, oceny)
for imie, ocena in pary:
    print(imie)
    print(ocena)

# 15. Mając listę liczby = [1, 2, 3, 4, 5], napisz funkcję kwadrat(x), która zwraca kwadrat liczby x. 
# Użyj map z tą funkcją, aby stworzyć nową listę, w której każdy element jest kwadratem 
# odpowiadającego mu elementu z listy liczby. Wyświetl tą listę. 
liczby = [1, 2, 3, 4, 5]
def kwadrat(x):
    return x ** 2
nowa_lista = list(map(kwadrat, liczby))
print(nowa_lista)

# 16. Napisz funkcję zmien_wartosc(arg), która przyjmuje jeden argument i próbuje 
# zmodyfikować ten argument w różny sposób w zależności od tego, czy jest on niemutowalny 
# (w tym przypadku integerem) czy mutowalny (w tym przypadku listą). 
# a. Jeśli jest listą, wykonaj arg[0] = 'kalafior '. 
# b. Jeśli jest integerem, wykonaj arg = 65482652. 

def zmien_wartosc(x):
    if isinstance(x, list):
        x[0] = 'kalafior'
    elif isinstance(x, int):
        x = 65482652
    return x
print(x)

# 17. Napisz funkcję zamowienie_produktu, która przyjmuje jeden obowiązkowy argument 
# pozycyjny nazwa_produktu i dwa obowiązkowe argumenty nazwane: cena i ilosc. Funkcja 
# powinna zwracać tekst podsumowujący zamówienie, zawierające nazwę produktu, łączną 
# cenę (cena * ilość) oraz ilość zamówionego produktu. 
# a. Stwórz pustą listę, do której wstawisz wartości zwracane przez funkcję dla 3 różnych 
# produktów. 
# b. Przeiteruj po wypełnionej liście, wyświetl teksty. 
# c. Zmodyfikuj funkcję tak, żeby oprócz tekstu podsumowującego zwracała także 
# wartość zamówienia. 
# d. Na koniec wyświetl sumaryczną wartość zamówień (sumę z każdego zamówionego 
# produktu). 
# e. Dodaj wartość domyślną dla argumentu ilosc równą 1.

def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    wartosc = cena * ilosc
    tekst_podsumowanie = f"Zamówienie: {nazwa_produktu}, Cena: {cena}, Ilość: {ilosc}, Łączna cena: {wartosc}"
    return tekst_podsumowanie, wartosc
zamowienia = []
zamowienia.append(zamowienie_produktu("Kawa", cena=10, ilosc=2))
zamowienia.append(zamowienie_produktu("Herbata", cena=5, ilosc=3))
zamowienia.append(zamowienie_produktu("Chleb", cena=3))
for tekst_podsumowanie, wartosc in zamowienia:
    print(tekst_podsumowanie)
suma_zamowien = sum(wartosc for _, wartosc in zamowienia)
print("Suma wartości zamówień:", suma_zamowien)

# 19. Napisz funkcję fabrykującą stworz_funkcje_potegujaca(wykladnik), która przyjmuje jeden 
# argument: wykładnik potęgi. Zwracana przez nią funkcja zagnieżdżona poteguj(podstawa) 
# powinna również przyjmować jeden argument – podstawę potęgi – i zwracać wynik 
# podniesienia tej podstawy do potęgi określonej przez wykładnik przekazany do funkcji 
# zewnętrznej. 
def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj

potega_2 = stworz_funkcje_potegujaca(2)
print(potega_2(5))

# 20. Napisz funkcję licznik(), która za każdym razem, gdy jest wywoływana, zwiększa swoje 
# wewnętrzne liczenie o jeden (licznik stanu). Zaimplementuj cztery wersje tej funkcji, 
# wykorzystując: 
# a. Zmienną nonlocal w zagnieżdżonej funkcji. 
# b. Zmienną global. 
# c. Klasę z atrybutem instancji. # Wskazówka: zaimplementowanie w klasie funkcji 
# __init__ oraz __call__  
# d. Atrybut funkcji. # Funkcja, jak każdy inny obiekt, może mieć swoje atrybuty 

#ad.a
from typing import Callable
def licznik() -> Callable[[], int]:
    licznik_stan: int = 2
    def zwieksz_licznik() -> int:
        nonlocal licznik_stan
        licznik_stan += 1
        return licznik_stan
    return zwieksz_licznik
licznik1 = licznik()
print(licznik1())  

#ad. b
licznik_stan2 = 2
def licznik2():
    global licznik_stan2
    licznik_stan2 =+ 1
    return licznik_stan2
print(licznik2())

#ad.c
class Licznik:
    def __init__(self):
        self.licznik_stan = 5
    def __call__(self):
        self.licznik_stan += 1
        return self.licznik_stan
licznik1 = Licznik()
print(licznik1())  

#ad.d
def licznik4():
    if not hasattr(licznik4, 'licznik_stan'):
        licznik4.licznik_stan = 7
    licznik4.licznik_stan += 1
    return licznik4.licznik_stan
print(licznik4())  # 1

# 22. Masz daną listę słowników reprezentujących informacje o książkach w bibliotece. Każdy 
# słownik zawiera klucze: 'tytul', 'autor' oraz 'rok_wydania'. Twoim zadaniem jest napisanie 
# kodu, który wykonuje następujące operacje przy użyciu funkcji lambda: 
# a. Sortowanie książek według roku wydania: Posortuj listę książek w kolejności 
# rosnącej według roku ich wydania. 
# b. Filtracja książek wydanych po 2000 roku: Utwórz nową listę zawierającą tylko te 
# książki, które zostały wydane po roku 2000. 
# c. Transformacja listy do listy tytułów: Przekształć oryginalną listę książek w listę 
# zawierającą tylko tytuły książek. 
# Wykorzystaj funkcje sorted(), filter() oraz map() w połączeniu z funkcjami lambda do realizacji 
# zadania. 

biblioteka = [
    {'tytul': 'Wesele', 'autor': 'Stanisław Wyspiański', 'rok_wydania': 1901},
    {'tytul': 'Pan Tadeusz', 'autor': 'Adam Mickiewicz', 'rok_wydania': 1834},
    {'tytul': 'Lalka', 'autor': 'Bolesław Prus', 'rok_wydania': 1890}
]
#a
posortowane_ksiazki = sorted(biblioteka, key=lambda x: x['rok_wydania'])
print("Sortowanie książek według roku wydania:")
for ksiazka in posortowane_ksiazki:
    print(ksiazka)
#b
ksiazki_po_2000 = list(filter(lambda x: x['rok_wydania'] > 1900, biblioteka))
print("\nFiltracja książek wydanych po 2000 roku:")
for ksiazka in ksiazki_po_2000:
    print(ksiazka)
#c
tytuly_ksiazek = list(map(lambda x: x['tytul'], biblioteka))
print("\nTransformacja listy do listy tytułów:")
print(tytuly_ksiazek)

# 23. Napisz generator, który iteracyjnie zwraca nazwy dni tygodnia: od poniedziałku do niedzieli. 
# Następnie, użyj tego generatora w pętli, aby wyświetlić każdy dzień tygodnia. Dodatkowo, 
# zademonstruj, jak można użyć tego generatora do pobrania tylko pierwszych trzech dni 
# tygodnia bez konieczności iterowania przez cały tydzień. 
# To zadanie można wykonać zarówno funkcją jak i wyrażeniem.

def dni_tygodnia():
    dzien = 0
    while dzien < 7:
        if dzien == 0:
            yield "Poniedziałek"
        elif dzien == 1:
            yield "Wtorek"
        elif dzien == 2:
            yield "Środa"
        elif dzien == 3:
            yield "Czwartek"
        elif dzien == 4:
            yield "Piątek"
        elif dzien == 5:
            yield "Sobota"
        elif dzien == 6:
            yield "Niedziela"
        dzien += 1
print("Każdy dzień tygodnia:")
for dzien in dni_tygodnia():
    print(dzien)
print("\nPierwsze trzy dni tygodnia:")
generator = dni_tygodnia()
for _ in range(3):
    print(next(generator))

# 24. Rozbij całość napisanego do tej pory kodu na jeden główny skrypt w folderze ./scripts/run.py 
# (który odpowiedzialny będzie za samo wywołanie funkcji) oraz na pakiet (stworzony w 
# folderze ./zajecia02), który będzie zawierał osobne moduły oraz subpakiet (stworzony w 
# folderze ./zajecia02/liczniki_stanu) w którym w osobnych modułach zapisane będą różne 
# wersje funkcji z zadania 20. Pakiety i subpakiety mają wykorzystywać listę __all__.

