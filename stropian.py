"""
pip install pyautogui
pip install pynput
pip install opencv-python
pip install opencv-contrib-python  ---> Jeśli z tym wcześniejszym nie bedzie działać
"""

"""
Przyciski "Sterowanie ręczne":

strałkaLG = 110, 100
strałkaŚG = 170, 100
strałkaPG = 230, 100
strałkaLŚ = 110, 160
STOP = 170, 160
strałkaPŚ = 230, 160
strałkaLD = 110, 220
strałkaŚD = 170, 220
strałkaPD = 230, 220

Strzałka poprzednie = 140, 270
Strzałka następne = 200, 270

Checkbox przednia = 157, 307
Checkbox tylna = 180, 307

dYdX = 330, 150
Button Alfa = 330, 285

Temperatura góra = 50, 65
Temperatura dół = 50, 290

Prędokść lewo = 80 ,350
Prędokść prawo = 260 ,350
"""

"""
Przyciski "Wycinanie":

Temperatura góra = 45, 80
Temperatura dół = 45, 250

Wymieniono drut = 470, 210 
Kontynuuj = 350, 240
Wstrzymaj = 470, 240
Parametry materiału = 180, 270
START = 350, 270
STOP = 470, 270

Checkbox Wycinanie wielościenne = 20, 330
Checkbox Obracaj podczas wycinania = 20, 370
"""

"""
Wycinanie zamknij = 520, 10
Sterowanie zamknij = 360, 10

"""


from pynput import keyboard
import pyautogui
from datetime import datetime
import time

# python -m mouseinfo

def sprawdz_obraz(sciezka_obrazu):
    okno = pyautogui.locateOnScreen(sciezka_obrazu, confidence=0.9)
    if okno == None:
        return False
    else:
        return True

def odswiez_sterowanie():
    global okno_sterowanie
    czas_start = time.time()
    okno_sterowanie = pyautogui.locateOnScreen('stropian_sterowanie.png', confidence=0.9)
    czas_stop = time.time()
    print(f'Czas odświeżania: {czas_stop - czas_start}')

def odswiez_wycinanie():
    global okno_wycinanie
    czas_start = time.time()
    okno_wycinanie = pyautogui.locateOnScreen('stropian_wycinanie.png', confidence=0.9)
    czas_stop = time.time()
    print(f'Czas odświeżania: {czas_stop - czas_start}')

def otwarcie_sterowania():
    odswiez_wycinanie()
    if okno_wycinanie:
        # Zamknięcie okna 'wycinanie'
        pyautogui.click(okno_wycinanie.left + 520, okno_wycinanie.top + 10)
        # Otwarcie okna 'sterowanie'
        pyautogui.click(pyautogui.locateOnScreen('ikona_sterowanie.png', confidence=0.9))
        return 0

    odswiez_sterowanie()
    if not okno_sterowanie:
        # Otwarcie okna 'sterowanie'
        pyautogui.click(pyautogui.locateOnScreen('ikona_sterowanie.png', confidence=0.9))

def otwarcie_wycinania():
    odswiez_sterowanie()
    if okno_sterowanie:
        # Zamknięcie okna 'sterowanie'
        pyautogui.click(okno_sterowanie.left + 360, okno_sterowanie.top + 10)
        # Otwarcie okna 'wycinanie'
        pyautogui.click(pyautogui.locateOnScreen('ikona_wycinanie.png', confidence=0.9))
        return 0

    odswiez_wycinanie()
    if not okno_wycinanie:
        # Otwarcie okna 'wycinanie'
        pyautogui.click(pyautogui.locateOnScreen('ikona_wycinanie.png', confidence=0.9))

def kliknij(zdjecie):
    # 'confidence' przyjmuje liczbe od 0-1. Jest to dokładność znajdowanego obrazu. Np. przy 0.6 znajduje nieprawidłowe przyciski.
    czas_start = time.time()
    przycisk = pyautogui.locateOnScreen(zdjecie, confidence=0.8)
    czas_stop = time.time()
    print(f'Przycisk: {przycisk}')
    print(f'Szukanie zdjęcia: {czas_stop - czas_start}')

    if przycisk != None:
        print(' - znalezione zdjęcie')
        czas_start = time.time()
        pyautogui.click(przycisk)
        czas_stop = time.time()
        print(f'Klikniecie zdjęcia: {czas_stop - czas_start}')
    else:
        print(' - nie ma takiego obrazka na ekranie')

    print()

def kliknij_w_oknie(okno, x, y):
    czas_start = time.time()
    try:
        wspolrzedne = okno.left + x, okno.top + y
        pyautogui.click(wspolrzedne)
        print(f'Klik: {wspolrzedne}')
    except AttributeError as error:
        print(f'Błąd: {error}')

    czas_stop = time.time()
    print(f'Czas kliknięcia współrzędnych: {czas_stop - czas_start}')


def akcja(klawisz):
    if klawisz == keyboard.Key.f14:
        odswiez_wycinanie()
        kliknij_w_oknie(okno_wycinanie, 470, 270)
        print(f'Stop - {klawisz}')
        print()

    elif klawisz == keyboard.Key.f13:
        odswiez_wycinanie()
        kliknij_w_oknie(okno_wycinanie, 350, 270)
        print(f'Start - {klawisz}')
        print()

    elif klawisz == keyboard.Key.f13:
        print(f'Start - {klawisz}', end=' ')
        kliknij('start.png')

    elif klawisz == keyboard.Key.f16:
        print(f'Rozpędzanie - {klawisz}', end=' ')
        kliknij('rozpedzanie2.png')

    elif klawisz == keyboard.Key.f17:
        print(f'Panel - {klawisz}', end=' ')
        kliknij('panel.png')

    elif klawisz == keyboard.Key.f18:
        print(f'Zamknięcie programu - {klawisz}')
        return False

    else:
        print('Odpuszczony klawisz: {}'.format(klawisz), end=' ')
        kliknij('CNC sterowanie.png')



# Robi screenshot i zapisuje w folderze
#pyautogui.screenshot('pulpitpy.png')

okno_wycinanie = pyautogui.locateOnScreen('stropian_wycinanie.png', confidence=0.9)
okno_sterowanie = pyautogui.locateOnScreen('stropian_sterowanie.png', confidence=0.9)



# Utworzenie 'nasłuchiwacza'
with keyboard.Listener(on_release=akcja) as listener:
    listener.join()

