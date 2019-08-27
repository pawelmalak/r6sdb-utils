import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

items = input("Number of items: ")
delay = input("Delay between shoots (1.75 for charms, 1 for rest): ")

def take_screenshots(items, delay):

  # Delay to change active window to the game
  time.sleep(5)

  for i in range (0, items):
    keyboard.press(Key.f12)
    mouse.position = (1800, 552)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)
    time.sleep(delay)

take_screenshots(items, delay)