#print("Hello World")
#help(print)
from os import getcwd #1. Z pakietu os zaimportuj jedną funkcję o nazwie getcwd.

current_path = getcwd() #2. Wywołaj funkcję getcwd i jej wynik przypisz do zmiennej current_path.
print(current_path)

import czas #6. Zaimportuj moduł czas w skrypcie skrypt1.py.
print(czas.aktualny_czas) #7. Wypisz wartość zmiennej aktualny_czas.

import time #8. Zaimportuj pakiet time
time.sleep(5) #9. Jako kolejną funkcję w skrypcie użyj time.sleep(20).
print(czas.aktualny_czas) #10. Ponownie wypisz wartość zmiennej aktualny_czas.

from importlib import reload #11. Przeładuj moduł czas.
reload(czas)
print(czas.aktualny_czas) #12. Po raz trzeci wypisz wartość zmiennej aktualny_czas.



