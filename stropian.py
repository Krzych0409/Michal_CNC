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
    global aktywne_okno
    odswiez_wycinanie()
    if okno_wycinanie:
        # Zamknięcie okna 'wycinanie'
        pyautogui.click(okno_wycinanie.left + 520, okno_wycinanie.top + 10)
        # Otwarcie okna 'sterowanie'
        pyautogui.click(pyautogui.locateOnScreen('ikona_sterowanie.png', confidence=0.9))
        time.sleep(3)
        odswiez_sterowanie()
        aktywne_okno = okno_sterowanie
        return 0

    odswiez_sterowanie()
    if not okno_sterowanie:
        # Otwarcie okna 'sterowanie'
        pyautogui.click(pyautogui.locateOnScreen('ikona_sterowanie.png', confidence=0.9))
        odswiez_sterowanie()

    aktywne_okno = okno_sterowanie

def otwarcie_wycinania():
    global aktywne_okno
    odswiez_sterowanie()
    if okno_sterowanie:
        # Zamknięcie okna 'sterowanie'
        pyautogui.click(okno_sterowanie.left + 360, okno_sterowanie.top + 10)
        # Otwarcie okna 'wycinanie'
        pyautogui.click(pyautogui.locateOnScreen('ikona_wycinanie.png', confidence=0.9))
        time.sleep(3)
        odswiez_wycinanie()
        aktywne_okno = okno_wycinanie
        return 0

    odswiez_wycinanie()
    if not okno_wycinanie:
        # Otwarcie okna 'wycinanie'
        pyautogui.click(pyautogui.locateOnScreen('ikona_wycinanie.png', confidence=0.9))
        time.sleep(5)
        odswiez_wycinanie()

    aktywne_okno = okno_wycinanie

def plan_klikniecia_wycinanie(wspolrzedne):
    odswiez_wycinanie()
    if okno_wycinanie:
        kliknij_w_oknie(okno_wycinanie, wspolrzedne)
        print(f'Klik - {wspolrzedne}\n')
    else:
        otwarcie_wycinania()
        kliknij_w_oknie(okno_wycinanie, wspolrzedne)
        print(f'Klik - {wspolrzedne}\n')

def plan_klikniecia_sterowanie(wspolrzedne):
    odswiez_sterowanie()
    if okno_sterowanie:
        kliknij_w_oknie(okno_sterowanie, wspolrzedne)
        print(f'Klik - {wspolrzedne}\n')
    else:
        otwarcie_sterowania()
        kliknij_w_oknie(okno_sterowanie, wspolrzedne)
        print(f'Klik - {wspolrzedne}\n')

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

def kliknij_w_oknie(okno, przycisk):
    czas_start = time.time()
    try:
        wspolrzedne = okno.left + przycisk[0], okno.top + przycisk[1]
        pyautogui.click(wspolrzedne)
        print(f'Klik: {wspolrzedne}')
    except AttributeError as error:
        print(f'Błąd: {error}')

    czas_stop = time.time()
    print(f'Czas kliknięcia współrzędnych: {czas_stop - czas_start}')

def akcja(klawisz):
    if klawisz == keyboard.Key.f13:
        plan_klikniecia_wycinanie(w_START)
    elif klawisz == keyboard.Key.f14:
        plan_klikniecia_wycinanie(w_STOP)
    elif klawisz == keyboard.Key.f15:
        plan_klikniecia_wycinanie(w_temp_dol)
    elif klawisz == keyboard.Key.f16:
        plan_klikniecia_wycinanie(w_temp_gora)

    elif klawisz == keyboard.Key.esc:
        print(f'Zamknięcie programu - {klawisz}')
        return False

    elif klawisz == keyboard.Key.f17:
        plan_klikniecia_sterowanie(s_temp_dol)
    elif klawisz == keyboard.Key.f18:
        plan_klikniecia_sterowanie(s_temp_gora)
    elif klawisz == keyboard.Key.f19:
        plan_klikniecia_sterowanie(s_STOP)
    elif klawisz == keyboard.Key.f21:
        plan_klikniecia_sterowanie(s_strzalka_LS)
    elif klawisz == keyboard.Key.f22:
        plan_klikniecia_sterowanie(s_strzalka_PS)
    elif klawisz == keyboard.Key.f23:
        plan_klikniecia_sterowanie(s_strzalka_SG)
    elif klawisz == keyboard.Key.f24:
        plan_klikniecia_sterowanie(s_strzalka_SD)


    '''else:
        print('Odpuszczony klawisz: {}'.format(klawisz), end=' ')
        kliknij('CNC sterowanie.png')'''


# Robi screenshot i zapisuje w folderze
#pyautogui.screenshot('pulpitpy.png')

# Przyciski panelu 'Sterowanie ręczne'
s_strzalka_LG = (110, 100)
s_strzalka_SG = (170, 100)
s_strzalka_PG = (230, 100)
s_strzalka_LS = (110, 160)
s_STOP = (170, 160)
s_strzalka_PS = (230, 160)
s_strzalka_LD = (110, 220)
s_strzalka_SD = (170, 220)
s_strzalka_PD = (230, 220)
s_temp_gora = (50, 65)
s_temp_dol = (50, 290)

# Przyciski panelu 'Wycinanie'
w_temp_gora = (45, 80)
w_temp_dol = (45, 250)
w_START = (350, 270)
w_STOP = (470, 270)



okno_wycinanie = pyautogui.locateOnScreen('stropian_wycinanie.png', confidence=0.9)
okno_sterowanie = pyautogui.locateOnScreen('stropian_sterowanie.png', confidence=0.9)
aktywne_okno = False
if okno_wycinanie: aktywne_okno = okno_wycinanie
elif okno_sterowanie: aktywne_okno = okno_sterowanie

print(f'Aktywne okno: {aktywne_okno}')


# Utworzenie 'nasłuchiwacza'
with keyboard.Listener(on_release=akcja) as listener:
    listener.join()

