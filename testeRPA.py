import pyautogui

#pyautogui.press('winleft') # presionar alguma tecla, no caso teclar win
#pyautogui.press('enter') # presionar alguma tecla, no caso teclar enter
#pyautogui.typewrite('vamos testar a digitacao\n') # escrever algum texto onde o cursor estiver
#pyautogui.typewrite(['a', 'b', 'left', 'backspace', 'enter', 'f1'], interval=1) # uma sequencia de teclas com intervalo

#pyautogui.keyUp('up') não funciona
#pyautogui.press('up')
#pyautogui.keyDown('down')

#pyautogui.alert('Essa é uma caixa de alertaaaaa!') # caixa de alerta com botão OK
#pyautogui.confirm('1234') #Caixa de confirmar ou cancelar
#pyautogui.prompt('escreva e aperte ok') #digite alguma coisa confirm ou cancele

printTela = pyautogui.screenshot()
printTela.save('imagem1.png')
#print('screenshot taken.')
#pyautogui.screenshot('C:/Users/ivanildo_carvalho/Desktop/Ivan/teste/fotoTESTE.png')


























# ABRIR EDGE, GOOGLE E PESQUISAR
'''pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(['backspace'], interval=1)
pyautogui.typewrite('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
pyautogui.typewrite(['enter'], interval=1)
pyautogui.typewrite('google.com.br')
pyautogui.typewrite(['enter'], interval=1)
pyautogui.typewrite('RPA com Python')"
pyautogui.typewrite(['enter'], interval=1)'''


# ABRIR SACG
'''pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite(['backspace'], interval=1)
pyautogui.typewrite('%ALLUSERSPROFILE%\Microsoft\AppV\Client\Integration\A029E8B3-FAD8-43AF-8E8F-ADD917100CFB\Root\ACClient.exe')
pyautogui.typewrite(['enter'], interval=1)'''









