import threading
from pynput.keyboard import Key, Controller

keyboard = Controller()
control_index = 0

def hello_world():
  global control_index 
  
  if control_index != 10: 
    threading.Timer(1.0, hello_world).start()
    keyboard.press('a')
    control_index += 1
  else:
    exit()

hello_world()