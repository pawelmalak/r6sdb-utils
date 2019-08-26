import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

def take_screenshots():
  # Delay to change active window to the game
  time.sleep(5)

  for i in range (0, 35):
    keyboard.press(Key.f12)
    mouse.position = (1800, 552)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)
    time.sleep(1)

take_screenshots()