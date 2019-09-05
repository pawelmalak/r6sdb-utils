import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

def take_screenshots(items, delay, verbose = False):

  # Delay to change active window to the game
  time.sleep(5)

  for i in range (0, items):
    # Make screenshot
    keyboard.press(Key.f12)

    # Print number of screenshots left
    if verbose:
      print(items - i, 'left')

    # Move to the next item
    mouse.position = (1800, 552)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)
    
    # Wait for item to load
    time.sleep(delay)