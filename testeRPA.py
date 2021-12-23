import pyautogui
import PIL
import pyautogui as pg
from pynput.keyboard import Key, Controller
keyb = Controller()


#pyautogui.PAUSE = 2.5 # pausar pyautoqui

#pyautogui.FAILSAFE = True

#-------MOVER MOUSE-------

#PEGAR POSIÇÃO DO MOUSE
#posicao = pyautogui.size() # ou usar pg.size() para pegar somente número
#print(posicao)

'''As coordenadas XY têm origem 0, 0 no canto superior esquerdo da tela. X aumenta indo para a direita,
Y aumenta indo para baixo (x, y, duration=num_segundos)'''
#pyautogui.moveTo(157, 962, duration=2) # Mover para a posição x e y, o arumento pode ser somente número (x, y, tempo)
#pyautogui.moveRel(-300, 800, duration=1) # mover mouse em relação a posição atual
#pyautogui.dragTo(10, 15, duration=1) # selecionar ou arrastar janelas
#pyautogui.dragRel(20, 20, duration=2) # Selecionar ou arrastar janelas em relação a pesição atual
#pyautogui.click(x=157,y=962, clicks=1, interval=2, button="right") # Mover o mouse com click escolhendo o botão
#pyautogui.rightClick() # click com o botão direito
#pyautogui.doubleClick() # click com o botão direito
#pyautogui.scroll(3000) # Rolar scroll - positivo para cima e negativo para baixo

#pyautogui.mouseDown(x=moveToX, y=moveToY, button='left') # estudar, não entendi***
#pyautogui.mouseUp(x=moveToX, y=moveToY, button='left') # estudar, não entendi***


# -------TECLADO-------
#pyautogui.write('OlÁ Mundo') # pressionar teclas de um único caractere
#pyautogui.write('Olá Muuuuundo', interval=0.25) # pressionar tecla de um único caractere com intervalo

# A PRINCÍPIO O COMANDO KEYDOWN E KEYUP NÃO FUNCIONOU
'''pyautogui.keyDown('shift')
pyautogui.press('right', presses=28, interval=1)
pyautogui.keyUp('shift')'''

'''pyautogui.leftClick(x=603, y=617, interval=0.25)
with pyautogui.hold('shift'):
    pyautogui.press(['left', 'left','left'])'''

'''pyautogui.leftClick(x=603, y=617, interval=0.25)
with Controller().pressed(Key.shift):
    Controller().press(Key.left)
    Controller().press(Key.left)
    Controller().press(Key.left)
    Controller().press(Key.left)
    Controller().press(Key.left)
    Controller().release(Key.left)'''

#pyautogui.hotkey('ctrl', 'shift', 'esc') # combinação de teclas
#pyautogui.press(['left','left','left','right']) # presionar várias vezes teclas de funcionalidade semelhante
#pyautogui.press('left', presses=28)
#pyautogui.typewrite(['a', 'b', 'left', 'backspace', 'enter', 'f1'], interval=1) # uma sequencia de teclas com intervalo
#pyautogui.press('winleft') # presionar alguma tecla, no caso teclar win
#pyautogui.press('enter') # presionar alguma tecla, no caso teclar enter
#pyautogui.typewrite('vamos testar a digitacao\n') # escrever algum texto onde o cursor estiver


#pyautogui.keyUp('up') não funciona
#pyautogui.press('up') # Tecla seta para cima
#pyautogui.keyDown('down') # teclar seta para baixo
#pyautogui.press('tab') # Teclar tab

#pyautogui.alert('Essa é uma caixa de alertaaaaa!') # caixa de alerta com botão OK
#pyautogui.confirm('1234') #Caixa de confirmar ou cancelar
#pyautogui.prompt('escreva e aperte ok') #digite alguma coisa confirm ou cancele


#pyautogui.press('prtsc')


# --------- TIRAR PRINT DE TELA ------------
'''printTela = pyautogui.screenshot()
printTela.save('imagem1.png')'''






'''======== MOUSE --- AVANÇADO ======='''

#naTela = pyautogui.onScreen(x,y) print(naTela) # verifica se as coordenadas estão dentro da tela.
#none=100
#pyautogui.moveTo(none, 200)
#pyautogui.moveTo(100, 200, 2) # mover o mouse para posição x e y com dois segundos de duração

#pyautogui.dragTo(549, 664, 2, button='left')
#pyautogui.dragTo(549, 404, button='left')
#pyautogui.drag(440, 0, 1, button='left') # mover com o botão esquerdo selecionado em linha reta
#pyautogui.rightClick(x=603, y=617, interval=0.25) # clicar com o botão direito no ponto x e y
#pyautogui.scroll(100) # scrollar o mouse, valor negativo para baixo e positivo para cima



'''BALAQUINHAS NO MOUSE, EFEITO ELASTICO, MOVIMENTOA RÁPIDO EM SEGUIDA DEVAGAR'''
#pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
#pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
#pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
#pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
#pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end
#pyautogui.mouseDown(); pyautogui.mouseUp()  # does the same thing as a left-button mouse click
#pyautogui.mouseDown(button='right')  # press the right button down



'''-------CAIXAS DE MENSAGENS--------'''

#pyautogui.alert(text='Você quer pegar um vírus?', title='Olá, amiginho(a)!', button='OK')
#msg = pyautogui.prompt(text='Digite uma mensagem antes de clicar OK ou Cancel ', title='Escolha OK ou Cancelar', default='')
#msg = pyautogui.password(text='text', default='default', mask='*')


'''-------- PRINTSCREEN ---------'''

#pyautogui.screenshot('myscreenshot7.png')
#im = pyautogui.screenshot(region=(0,0,300,400))





button5location = pyautogui.locateOnScreen('C:/Users/ivanildo_carvalho/Desktop/Ivan/Python/teste/botao5.PNG')
print(button5location)







# ABRIR EDGE, GOOGLE E PESQUISAR
'''pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(['backspace'], interval=1)
pyautogui.typewrite('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
pyautogui.typewrite(['enter'], interval=1)
pyautogui.typewrite('google.com.br')
pyautogui.typewrite(['enter'], interval=1)
pyautogui.typewrite('RPA com Python')
pyautogui.typewrite(['enter'], interval=1)'''


# ABRIR SACG
'''pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(['backspace'], interval=1)
pyautogui.typewrite('%ALLUSERSPROFILE%\Microsoft\AppV\Client\Integration\A029E8B3-FAD8-43AF-8E8F-ADD917100CFB\Root\ACClient.exe')
pyautogui.typewrite(['enter'], interval=1)'''









