import pyautogui
import time

link = 0
navegador = 0
palavra_chave = 0

navegador = input('Cole o nome do navegador (e: chrome, edge etc): ')
link = input('Cole o link do site: ')
palavra_chave = input('Digite a palavra-chave: ')
while navegador == '' or link == '' or palavra_chave == '':
    print('Você precisa preencher todos os campos')
    navegador = input('Cole o nome do navegador (e: chrome, edge etc): ')
    link = input('Cole o link do site: ')
    palavra_chave = input('Digite a palavra-chave: ')

else:
    print('O programa vai iniciar em 5 segundos, por favor, não mexa no mouse e no teclado')
    time.sleep(5)
    pyautogui.PAUSE = 1
    pyautogui.press('win')
    pyautogui.write(navegador)
    pyautogui.press('enter')
    pyautogui.write(link)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=508, y=193)
    pyautogui.write(palavra_chave)
    pyautogui.press('enter')


    time.sleep(3)
    while True:
        pyautogui.click(x=347, y=322)
        pyautogui.click(x=535, y=324)
        time.sleep(2)