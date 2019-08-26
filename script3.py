import os
import ctypes
import pywin32
import time

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
   _fields_ = [("wVk", ctypes.c_ushort),
               ("wScan", ctypes.c_ushort),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
   _fields_ = [("uMsg", ctypes.c_ulong),
               ("wParamL", ctypes.c_short),
               ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
   _fields_ = [("dx", ctypes.c_long),
               ("dy", ctypes.c_long),
               ("mouseData", ctypes.c_ulong),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
   _fields_ = [("ki", KeyBdInput),
               ("mi", MouseInput),
               ("hi", HardwareInput)]


class Input(ctypes.Structure):
   _fields_ = [("type", ctypes.c_ulong),
("ii", Input_I)]

def press_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008 | 0x0002

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


#    get_game_window()
# press_key(0x14)    # t - opens chat
# release_key(0x14)

# press_key(0x23);release_key(0x23); # h
# press_key(0x12);release_key(0x12); # e
# press_key(0x26);release_key(0x26); # l
# press_key(0x26);release_key(0x26); # l
# press_key(0x18);release_key(0x18); # o

# press_key(0x1C);release_key(0x1C); # Submit it


def take_screenshot():
  time.sleep(5)

  # for i in range (0, 10):
  #   # keyboard.press(Key.f12)
  #   # mouse.position = (1798, 549)
  #   # mouse.position = (1779, 569)
  #   mouse.position = (627, 295)
  #   mouse.press(Button.left)
  #   mouse.release(Button.left)
  #   time.sleep(1)
  press_key(0xCD);release_key(0xCD); # h

take_screenshot()