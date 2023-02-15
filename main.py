"""
pip install pyautogui
pip install pynput
pip install opencv-python
pip install opencv-contrib-python  ---> Jeśli z tym wcześniejszym nie bedzie działać
"""
from pynput import keyboard
import pyautogui


def kliknij(zdjecie):
    # 'confidence' przyjmuje liczbe od 0-1. Jest to dokładność znajdowanego obrazu. Np. przy 0.6 znajduje nieprawidłowe przyciski.
    przycisk = pyautogui.locateOnScreen(zdjecie, confidence=0.8)

    if przycisk != None:
        print(' - znalezione zdjęcie')
        pyautogui.click(przycisk)
    else:
        print(' - nie ma takiego obrazka na ekranie')

def akcja(klawisz):
    if klawisz == keyboard.Key.media_previous:
        print(f'Stop - {klawisz}', end='')
        kliknij('stop.png')
    elif klawisz == keyboard.Key.media_next:
        print(f'Do zera - {klawisz}', end='')
        kliknij('dozera.png')
    elif klawisz == keyboard.Key.media_volume_down:
        print(f'Start - {klawisz}', end='')
        kliknij('start.png')
    elif klawisz == keyboard.Key.media_volume_up:
        print(f'Rozpędzanie - {klawisz}', end='')
        kliknij('rozpedzanie.png')
    elif klawisz == keyboard.Key.esc:
        print(f'Zamknięcie programu - {klawisz}')
        return False
    else:
        print('Odpuszczony klawisz: {}'.format(klawisz))


# Robi screenshot i zapisuje w folderze
#pyautogui.screenshot('pulpitpy.png')

# Utworzenie 'nasłuchiwacza'
with keyboard.Listener(on_release=akcja) as listener:
    listener.join()

