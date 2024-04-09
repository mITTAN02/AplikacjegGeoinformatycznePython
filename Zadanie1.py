import json
# Wczytaj jako słownik plik z rozszerzeniem JSON 
with open('teksty.json', 'r') as file:
 content = file.read()
# Zamień wszystkie duże litery na małe
male = content.lower()
print(male)
# Podziel go na wyrazy - będzie to najprawdopodobniej lista
wyrazy = male.split()
print(wyrazy) 
# Usuń znaki interpunkcyjne – w tekście występują jedynie kropki i przecinki,
interpunkt = [wyraz.replace(',', '').replace('.', '') for wyraz in wyrazy]
print(interpunkt)
# Zmodyfikuj tak każdy wyraz, żeby w każdym ostatni znak był w formacie dużej litery np.
# wyraz KozA
koza = [x[:-1] + x[-1].upper() for x in interpunkt]
print(koza)
# Z listy usuń wyrazy, które nie posiadają w sobie znaku a lub A - można wykorzystać składnię
# list składanych
a = [word for word in koza if 'a' in word or 'A' in word]
print(a)
# Swórz zmienną, które będzie przechowywać wszystkie unikatowe wyrazy - można
zbior = set(a)
print(zbior)
#Stwórz zmienną, która będzie przetrzymywać ilość wystąpień dla każdego ze słów
# występujących w tekście - można wykorzystać słowniki.
slownik = {}
for i in a:
    slownik[i] = a.count(i)

print(slownik)

with open('slownik.json', 'w') as file:
    json.dump(slownik, file, indent=4)