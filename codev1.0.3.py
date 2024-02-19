from pathlib import Path
import os
import easygui
import urllib.request
from urllib.request import urlretrieve
global wersja
import pygame, sys, random

narciarz_rysunki = ["skier_down.png", "skier_right1.png", "skier_right2.png", "skier_left2.png", "skier_left1.png"]

class KlasaNarciarz(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.nachylenie = 0

    def obroc(self, kierunek):
        self.nachylenie = self.nachylenie + kierunek
        if self.nachylenie < -2: self.nachylenie = -2
        if self.nachylenie > 2: self.nachylenie = 2
        srodek = self.rect.center
        self.image = pygame.image.load(narciarz_rysunki[self.nachylenie])
        self.rect = self.image.get_rect()
        self.rect.center = srodek
        predkosc = [self.nachylenie, 6 - abs(self.nachylenie) * 2]
        return predkosc
    
    def przesun(self, predkosc):
        self.rect.centerx = self.rect.centerx + predkosc[0]
        if self.rect.centerx < 20: self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620

class KlasaPrzeszkoda(pygame.sprite.Sprite):
    def __init__(self, plik_graficzny, pole, rodzaj):
        pygame.sprite.Sprite.__init__(self)
        self.plik_graficzny = plik_graficzny
        self.image = pygame.image.load(plik_graficzny)
        self.rect = self.image.get_rect()
        self.rect.center = pole
        self.rodzaj = rodzaj
        self.zaliczona = False
    def update(self):
        global predkosc
        self.rect.centery -= predkosc[1]
        if self.rect.centery < -32:
            self.kill()

def utworz_mape():
    zajete_pola = []
    for i in range(10):
        wiersz = random.randint(0, 9)
        kolumna = random.randint(0, 9)
        pole = [kolumna * 64 + 20, wiersz * 64 + 20 + 640]
        if not (pole in zajete_pola):
            zajete_pola.append(pole)
            rodzaj = random.choice(["drzewko", "flaga"])
            if rodzaj == "drzewko": rysunek = "skier_tree.png"
            elif rodzaj == "flaga": rysunek = "skier_flag.png"
            przeszkoda = KlasaPrzeszkoda(rysunek, pole, rodzaj)
            przeszkody.add(przeszkoda)

def animuj():
    ekran.fill([255, 255, 255])
    przeszkody.draw(ekran)
    ekran.blit(narciarz.image, narciarz.rect)
    ekran.blit(wynik_tekst, [10, 10])
    pygame.display.flip()

try:
    if wersja != "1.0.3":
        os.remove("codev" + wersja + ".py")
        easygui.msgbox("Aktualizacja zakonczona!")
        easygui.msgbox("W folderze w ktorym miales poprzednia wersje programu powinienes spotkać nowa!")
        exit()
except NameError:
    print("")


wersja = "1.0.3"

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
        wybor1 = easygui.choicebox("Witaj w systemie makensonn105. Co chcesz zrobic?", choices = ['kalkulator', 'narciarz(gra)', 'wyjdz'])
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
            
        elif wybor1 == "narciarz(gra)":
            global punkty
            global ekran
            global zegar
            global narciarz
            global przeszkody
            global predkosc
            global wynik_tekst
            pygame.init()
            ekran = pygame.display.set_mode([640, 640])
            zegar = pygame.time.Clock()
            narciarz = KlasaNarciarz()
            predkosc = [0, 6]
            przeszkody = pygame.sprite.Group()
            pozycja_mapy = 0
            punkty = 0
            utworz_mape()
            czcionka = pygame.font.Font(None, 50)
            uruchomiona = True
            while uruchomiona:
                zegar.tick(30)
                for zdarzenie in pygame.event.get():
                    if zdarzenie.type == pygame.QUIT:
                        uruchomiona = False
                    if zdarzenie.type == pygame.KEYDOWN:
                        if zdarzenie.key == pygame.K_LEFT:
                            predkosc = narciarz.obroc(-1)
                        elif zdarzenie.key == pygame.K_RIGHT:
                            predkosc = narciarz.obroc(1)
                
                narciarz.przesun(predkosc)

                pozycja_mapy += predkosc[1]

                if pozycja_mapy >= 640:
                    utworz_mape()
                    pozycja_mapy = 0

                kolizja = pygame.sprite.spritecollide(narciarz, przeszkody, False)
                if kolizja:
                    if kolizja[0].rodzaj == "drzewko" and not kolizja[0].zaliczona:
                        punkty = punkty - 100
                        narciarz.image= pygame.image.load("skier_crash.png")
                        animuj()
                        pygame.time.delay(1000)
                        narciarz.image = pygame.image.load("skier_down.png")
                        narciarz.nachylenie = 0
                        predkosc = [0, 6]
                        kolizja[0].zaliczona = True
                    elif kolizja[0].rodzaj == "flaga" and not kolizja[0].zaliczona:
                        punkty += 10
                        kolizja[0].kill()

                przeszkody.update()
                wynik_tekst = czcionka.render("Wynik: " + str(punkty), 1, (0, 0, 0))
                animuj()
            pygame.quit()

        elif wybor1 == "wyjdz":
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
    url = "https://maka12v.github.io/codev" + aktualizacja + ".py"
    filename = "codev" + aktualizacja + ".py"
    urlretrieve(url, filename)
    exec(open("codev" + aktualizacja + ".py").read())