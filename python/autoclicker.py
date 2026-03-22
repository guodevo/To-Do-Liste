import pyautogui
from pynput.keyboard import *
import time

delay = 1
key_trigger = KeyCode.from_char("z")
exit_key = KeyCode.from_char("c")
stop_key = KeyCode.from_char("x")

paused = True
running = True

def on_press_z_x(key):
    global paused, running
    if key == key_trigger:
        if paused:
            paused = False
        else:
            paused = True

    elif key == exit_key:
        running = False

    elif key == stop_key:
        paused = True


def main():
    lis = Listener(on_press=on_press_z_x)
    lis.start()
    pyautogui.PAUSE = delay

    while running:
        if not paused:
            pyautogui.click(pyautogui.position())
        time.sleep(0.1)
           
    lis.stop()


if __name__ == "__main__":
    main()
        