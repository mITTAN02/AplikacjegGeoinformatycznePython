import math
import random
wartosc = 100 #2. Stwórz zmienną wartosc o wartości 100

dodawanie = wartosc + 123.15 #3. Do zmiennej dodawanie przypisz wartość dodania do zmiennej wartosc liczby 123.15
print(dodawanie)

potega = dodawanie**12 #4. Stwórz zmienną potega i przypisz do niej zmienną dodawanie podniesioną do potęgi 12345.
print(potega)

tekst = str(potega) #5. 5. Do zmiennej tekst przypisz rzutowanie wartości zmiennej potega na typ string.
print(tekst)

wartosc_pi = math.pi #6. Do zmiennej wartosc_pi przypisz wartość pi.
print(wartosc_pi)

lista = [1,2,3,4,5]
losowa = random.choice(lista)#7. Do zmiennej losowa przypisz losową wartość z listy [1,2,3,4,5].
lista.append(losowa)
print(lista)

#-------------------------------------------------------

tekst = f"Wartosc: {tekst}" #8. Nadpisz zmienną tekst następującym wyrażeniem: tekst = f"Wartosc: {tekst}"
print(tekst)

print(len(tekst)) #9. Wyświetl długość tekstu w zmiennej tekst i później wykorzystując wycinki wyświetl część zmiennej tekst o wartości „art”.

print(tekst[tekst.find('art'):]) #10. Później wykorzystując wycinki wyświetl część zmiennej tekst o wartości „art”.

print(dir(tekst)) #11. Wypisanie wartości funkcji dir(tekst)

tekst = tekst.upper()
print(tekst) #11. Zamiana całego łańcucha znaków w zmiennej 'tekst' na wielkie litery i wypisanie

nowy_tekst = tekst[:2] + 'p' + tekst[3:]
print(nowy_tekst) #12. Spróbuj zamienić znak na pozycji 2 w łańcuchu w zmiennej tekst na znak p.

#-------------------------------------------------------

#13
lista = list(tekst) # Stwórz zmienną o nazwie lista, przypisz do niej rzutowanie na listę zmiennej tekst.
print(lista)

lista = lista[lista.index('W'):lista.index(' ')]# Wykorzystując wycinki zrób tak, żeby lista zawierała jedynie litery słowa WARTOSC i później dwukropek.
print(lista)

lista += [[1, 2, 3, 4, 5]]# Do listy dodaj kolejny wyraz, niech będzie to kolejna lista [1,2,3,4,5]
print(lista)

lista.remove(':') #Z listy usuń wyraz, który jest dwukropkiem.
print(lista) #Wypisz zmienną lista.


#-------------------------------------------------------

#14

lista2 = [1,2,3,"banan",100] #Stwórz zmienną jak tutaj: lista2 = [1,2,3,"banan",100]
print(lista2)

lista3 = [x**2 for x in lista2 if x != "banan"] #Jako zmienna lista3, wykorzystaj składnię listy składanej, przeiteruj po każdym
#wyrazie z listy, do nowej listy zapisz wartość podniesioną do potęgi 2, jeśli wartość
#jest równa "banan" to ją pomiń

lista4 = list(range(2, 17, 2)) #Stwórz lista4, wykorzystaj funkcję range(), ma ona zawierać co drugą liczbę od 2 do 16.

# Wypisanie zmiennych lista2, lista3 i lista4
print("lista2:", lista2)
print("lista3:", lista3)
print("lista4:", lista4)

#---------------------------------------------
# 15. Stworzenie pustego słownika o nazwie 'ja'
ja = {}

# 16. Niech będzie to reprezentacja Twojej osoby, dodaj do niego klucze imie, nazwisko, wiek,
# rodzice (rodzice mają być reprezentowani przez listę z 2 zagnieżdżonymi słownikami o 2
# kluczach: imie i wiek).
ja['imie'] = 'Mateusz'
ja['nazwisko'] = 'Mitan'
ja['wiek'] = 22
ja['rodzice'] = [{'imie': 'Renata', 'wiek': 56}, {'imie': 'Maciej', 'wiek': 60}]

# 17. Wypisanie wartości klucza rodzice.
print(ja['rodzice'])

# 18. Wypisanie jedynie imienia pierwszego z rodziców.
print(ja['rodzice'][0]['imie'])

# 19. Wypisanie wszystkich kluczy naszego słownika.
print(ja.keys())

# 20. Sprawdzenie czy nasz słownik posiada klucz rodzenstwo, wypisanie zmiennej typu boolean.
czy_ma_rodzenstwo = 'rodzenstwo' in ja
print(czy_ma_rodzenstwo)

#-------------------------------------------------------

#21. Do zmiennej krotka1 przypisz wartość (1,2,"3",4,2,5).
krotka1 = (1,2,"3",4,2,5)
print(krotka1)

#22. Wypisz długość zmiennej i pierwszy wyraz.
print("Długość zmiennej krotka1:", len(krotka1))
print("Pierwszy wyraz zmiennej krotka1:", krotka1[0])

#23. Sprawdź, ile razy występuje wartość 2 i wypisz.
print(krotka1.count(2))

#24. Spróbuj zmienić pierwszy wyraz na wartość 2.
#krotka1[0] = 2

#---------------------------------------

#25. Stwórz dwa zbiory o nazwach X i Y, nadaj im wartości odpowiednio: set("kalarepa") oraz set("lepy").
X = set("kalarepa")
Y = set("lepy")
print(X)
print(Y)

#26. Wyświetl część wspólną obu zbiorów - można na nich wykonywać podobne operacje jak na zbiorach matematycznych.
print(X & Y)

#------------------------------------------------------------------
#Instrukcje
#1. Napisz program, który iteruje przez listę imion używając pętli for oraz funkcji enumerate(),
#aby wyświetlić indeks każdego imienia wraz z samym imieniem
lista_imion = ["ozai", "sozin", "toph", "aang", "katara", "sokka", "zuko", "iroh"]
for i in enumerate(lista_imion):
    print(i)

#a) Gdzie wystąpią dwa warunki - napisz program sprawdzający czy dana liczba jest
#dodatnia i parzysta. Jeśli tak, program powinien wydrukować "Liczba jest dodatnia i
#parzysta"
liczba = 4
if liczba > 0 and liczba % 2 == 0:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta lub niedodatnia")

#b) Gdzie wykorzystane zostanie zaprzeczenie not lub =! - napisz program, który
#sprawdza, czy wprowadzona przez użytkownika liczba nie jest równa zero. Jeśli nie
#jest, wydrukuj "Liczba jest różna od zera".
if liczba != 0:
    print("Liczba jest różna od zera")

#c) Gdzie wykorzystane będzie słowo in - napisz program, który sprawdza, czy
#wprowadzony przez użytkownika owoc znajduje się na liście dostępnych owoców
#(np. ['jabłko', 'banan', 'pomarańcza']). Jeśli tak, program powinien wydrukować
#"Owoc jest dostępny".
lista_owocow = ["jabłko", "kiwi", "awokado"," pomarańcza", "wiśnia", "klementynka"]
owoc = "jabłko"
if owoc == "aaaa" in lista_owocow:
    print("Owoc jest dostępny")
else:
    print("Owoc nie jest dostępny")

# #3. Stwórz przykład z pętlą while - Stwórz program, który będzie ciągle prosił użytkownika o
# wprowadzenie liczby. Program powinien sumować wprowadzone liczby i kończyć działanie,
# gdy suma przekroczy 100. Po zakończeniu pętli, program powinien wydrukować sumę
# wprowadzonych liczb.

suma = 0
licznik = 0
# while suma <= 100:
#     liczba = float(input("Podaj liczbę: "))
#     suma += liczba
#     licznik += 1
print(suma)

#-----------------------------------------------------------------

# “Dziwactwa”
# <w tych przypadkach, zapoznaj się z kodem, wyzwól go i zastanów się co się dzieje>
# 1. Przypisanie tworzy referencje, a nie kopie
L = [1,2,3,4]
M = [1,2,3,L,4]
print(f"Wartość zmiennej M przed zmianą L: {M}")
L[1] = "woooow"
print(f"Wartość zmiennej M po zmianie L: {M}")

# 2. Powtórzenie dodaje jeden poziom zagłębienia
L = [4,5,6]
X = L * 4
Y = [L] * 4
print(f"X: {X}, Y: {Y}")
L[1] = "wow"
print(f"X: {X}, Y: {Y}")

L = [4,5,6]
Y = [list(L)] * 4
L[1] = "wow"
print(f"Y: {Y}")
Y[0][1] = "wow"
print(f"Y: {Y}")


#--------------------------------------------------------------------------

# Praca z plikami
# <przy pracy z plikami warto stosować managery kontekstu (za pomocą słowa with), które dbają o
# poprawne otwarcie i zamknięcie zasobów>

# with open('example.txt', 'r') as file:
#  content = file.read()

#   ------------------------------------------------------------------------

with open('teksty.json', 'r') as file:
 content = file.read()

content.upper()
print(content)


