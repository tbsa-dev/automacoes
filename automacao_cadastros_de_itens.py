import pyautogui
import time

#Site utilizado é apenas um site testes

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
login = "teste@gmail.com" 
senha = "12345oli,kumjynhtbgrvfcdxdw"
#Abrir o chrome e logar no site
pyautogui.PAUSE = 0.3
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(2) #Aguardar 2 segundos para o chrome abrir
pyautogui.write(site)
pyautogui.press("enter")  
time.sleep(2) #Aguardar 2 segundos para o site carregar
pyautogui.click(x=682, y=453) #Clicar no campo de login
pyautogui.write(login)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2) #Aguardar 2 segundos para o site carregar
pyautogui.click(x=685, y=315) #Clicar no botão de produtos

import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: 
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("enter")

    pyautogui.scroll (100000)
    pyautogui.click(x=685, y=315) 