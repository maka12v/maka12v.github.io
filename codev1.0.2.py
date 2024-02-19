from pathlib import Path
import os
import easygui
import urllib.request
from urllib.request import urlretrieve

if wersja != "1.0.2":
    print("Aktualizacja zakończona")
    os.remove("codev" + wersja + ".py")


wersja = "1.0.2"

def logowanie():
    global probhaslo
    global haslo
    testh = 1
    while testh == 1:
        probhaslo = easygui.enterbox("Zaloguj się! Podaj haslo: ")
        plik = open("haslo.txt", "r")
        haslo = plik.read()
        plik.close()
        if probhaslo == haslo:
            del testh
            return 1
        elif str(probhaslo) == "None":
            return 0
        else:
            print(probhaslo)
            easygui.msgbox("Zle haslo!")
def dziel(a, b):
    wynik = a/b
    return wynik

def mno(a, b):
    wynik = a*b
    return wynik

def dod(a, b):
    wynik = a+b
    return wynik

def ode(a, b):
    wynik = a-b
    return wynik

def menu():
    dzialanie = 1
    while dzialanie == 1:
        wybor1 = easygui.choicebox("Witaj w systemie makensonn105. Co chcesz zrobic?", choices = ['kalkulator', 'wyjdz'])
        if wybor1 == "kalkulator":
            wybor2 = easygui.choicebox("Wybierz sposób działania: ", choices  = ['dzielenie', 'mnożenie', 'dodawanie', 'odejmowanie'])
            if wybor2 == "dzielenie":
                try:
                    a = int(easygui.enterbox("Podaj liczbe 1"))
                except TypeError:
                    continue
                except ValueError:
                    continue
                try:
                    b = int(easygui.enterbox("Podaj liczbe 2"))
                except TypeError:
                    continue
                except ValueError:
                    continue
                easygui.msgbox("Wynik: " + str(dziel(a, b)))
            elif wybor2 == "mnożenie":
                try:
                    a = int(easygui.enterbox("Podaj liczbe 1"))
                except TypeError:
                    continue
                except ValueError:
                    continue
                try:
                    b = int(easygui.enterbox("Podaj liczbe 2"))
                except TypeError:
                    continue
                except ValueError:
                    continue
                easygui.msgbox("Wynik: " + str(mno(a, b)))
            elif wybor2 == "dodawanie":
                try:
                    a = int(easygui.enterbox("Podaj liczbe 1"))
                except TypeError:
                    continue
                except ValueError:
                    continue
                try:
                    b = int(easygui.enterbox("Podaj liczbe 2"))
                except TypeError:
                    continue
                except ValueError:
                    continue
                easygui.msgbox("Wynik: " + str(dod(a, b)))
            elif wybor2 == "odejmowanie":
                try:
                    a = int(easygui.enterbox("Podaj liczbe 1"))
                except TypeError:
                    continue
                except ValueError:
                    continue
                try:
                    b = int(easygui.enterbox("Podaj liczbe 2"))
                except TypeError:
                    continue
                except ValueError:
                    continue
                easygui.msgbox("Wynik: " + str(ode(a, b)))

        if wybor1 == "wyjdz":
            del dzialanie
            return 1


aktu = urllib.request.urlopen('https://maka12v.github.io/version')
aktualizacja = str(aktu.read())
aktualizacja = aktualizacja.replace("b", "")
aktualizacja = aktualizacja.replace("'", "")
if str(wersja) == str(aktualizacja):
    plik = Path("haslo.txt")
    if plik.is_file():
        if logowanie() == 1:
            if menu() == 1:
                easygui.msgbox("Dziękujemy za skorzystanie z systemu makenosnn105")
                exit()


    else:
        print("Zarejestruj się!")
        haslo = easygui.enterbox("Zarejestruj się! Podaj haslo do utworzenia")
        plik = open("haslo.txt", "w")
        plik.write(haslo)
        plik.close()
        if menu() == 1:
            easygui.msgbox("Dziękujemy za skorzystanie z systemu makenosnn105")
            exit()
        if menu() == 0:
            exit()
else:
    easygui.msgbox("Twój program wymaga aktualizacji!")
    print("Trwa aktualizowanie....")
    url = "https://maka12v.github.io/codev" + str(aktualizacja) + ".py"
    filename = "codev" + str(aktualizacja) + ".py"
    urlretrieve(url, filename)
    print("Aktualizacja zakończona")
    exit()