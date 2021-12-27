#from pynput.mouse import Button, Controller

#mouse = Controller()






'''------MOUSE-------'''

# LER A POSIÇÃO DO PONTEIRO
#print('A posição atual do ponteiro é {0}'.format(mouse.position))

# DEFINIR A POSIÇÃO DO PONTEIRO
#mouse.position = (1000, 500)
#print('Agora movemos para {0}'.format(mouse.position))

# PONTEIRO MOVIMENTO RELATIVO A POSIÇÃO ATUAL
#mouse.move(500, -50)

# PRESSIONAR E SOLTAR
#mouse.press(Button.right)
#mouse.release(Button.right)

# DUPLO CLICK
#mouse.click(Button.left, 2)

# SCROLL
#mouse.scroll(0, 10)
#mouse.scroll(0, -10)


# MONITORANDO MOUSE
'''
from pynput import mouse

def on_move(x, y):
    print('Ponteiro movido para {0}'.format(x, y))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed
                              else 'Released', (x, y)))
    if not pressed:
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

# ... OU, COLETAR ATÉ QUE ALGUMA TECLA SEJA PRECIONADA
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ... OU, COLETAR ATÉ QUE ALGUMA

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
'''

























