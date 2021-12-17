import pyautogui,
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

#with keyb.pressed(Key.cmd):
#    keyb.press('e')
#    keyb.release('e')

#teclas = pyautogui.KEYBOARD_KEYS
#print(teclas)
