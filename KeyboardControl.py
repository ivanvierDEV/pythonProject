import pyautogui
from pynput.keyboard import Key, Controller

keyb = Controller()

# DIGITAR UMA UNICA TECLA
 #keyb.press('1')
 #keyb.release('')

# DIGITAR UM TEXTO
# keyb.type('12346 olha o número')

# DIGITAR UMA TECLA ESPECIAL TIPO Ctrl, Alt...
# keyb.press(Key.cmd)
# keyb.release(Key.cmd)


# DIGITAR COMBINAÇÃO DE TECLAS

pyautogui.leftClick(x=603, y=617, interval=0.25)
with keyb.pressed(Key.shift):
    keyb.press(Key.left)
    keyb.release(Key.left)

#teclas = pyautogui.KEYBOARD_KEYS
#print(teclas)
