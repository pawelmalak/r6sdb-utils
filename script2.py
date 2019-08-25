import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

def take_screenshot():
  time.sleep(5)

  for i in range (0, 10):
    # keyboard.press(Key.f12)
    # mouse.position = (1798, 549)
    # mouse.position = (1779, 569)
    mouse.position = (627, 295)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(1)

take_screenshot()