from pathlib import Path
import os
import easygui
import urllib.request

wersja = "b'1.0.0'"

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
        else:
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
            a = int(easygui.enterbox("Podaj liczbe 1"))
            b = int(easygui.enterbox("Podaj liczbe 2"))
            if wybor2 == "dzielenie":
                easygui.msgbox("Wynik: " + str(dziel(a, b)))
            if wybor2 == "mnożenie":
                easygui.msgbox("Wynik: " + str(mno(a, b)))
            if wybor2 == "dodawanie":
                easygui.msgbox("Wynik: " + str(dod(a, b)))
            if wybor2 == "odejmowanie":
                easygui.msgbox("Wynik: " + str(ode(a, b)))
        else:
            del dzialanie
            return 1

aktu = urllib.request.urlopen('https://maka12v.github.io/version')
aktualizacja = aktu.read()
if str(wersja) == str(aktualizacja):
    plik = Path("haslo.txt")
    if plik.is_file():
        if logowanie() == 1:
            if menu() == 1:
                easygui.msgbox("Dziękujemy za skorzystanie z systemu makenosnn105")


    else:
        print("Zarejestruj się!")
        haslo = easygui.enterbox("Zarejestruj się! Podaj haslo do utworzenia")
        plik = open("haslo.txt", "w")
        plik.write(haslo)
        plik.close()
        if menu() == 1:
            easygui.msgbox("Dziękujemy za skorzystanie z systemu makenosnn105")
else:
    easygui.msgbox("Twój program wymaga aktualizacji!")