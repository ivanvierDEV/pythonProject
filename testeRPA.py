import pyautogui
import pyautogui as pg


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

#pyautogui.press('winleft') # presionar alguma tecla, no caso teclar win
#pyautogui.press('enter') # presionar alguma tecla, no caso teclar enter
#pyautogui.typewrite('vamos testar a digitacao\n') # escrever algum texto onde o cursor estiver
#pyautogui.typewrite(['a', 'b', 'left', 'backspace', 'enter', 'f1'], interval=1) # uma sequencia de teclas com intervalo

#pyautogui.keyUp('up') não funciona
#pyautogui.press('up') # Tecla seta para cima
#pyautogui.keyDown('down') # teclar seta para baixo
#pyautogui.press('tab') # Teclar tab

#pyautogui.alert('Essa é uma caixa de alertaaaaa!') # caixa de alerta com botão OK
#pyautogui.confirm('1234') #Caixa de confirmar ou cancelar
#pyautogui.prompt('escreva e aperte ok') #digite alguma coisa confirm ou cancele


# --------- TIRAR PRINT DE TELA ------------
'''printTela = pyautogui.screenshot()
printTela.save('imagem1.png')'''






'''======== MOUSE --- AVANÇADO ======='''

#naTela = pyautogui.onScreen(x,y) print(naTela) # verifica se as coordenadas estão dentro da tela.
#none=100
#pyautogui.moveTo(none, 200)
#pyautogui.moveTo(100, 200, 2) # mover o mouse para posição x e y com dois segundos de duração

pyautogui.dragTo(549, 664, 2, button='left')


#estou terstando as versões














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









