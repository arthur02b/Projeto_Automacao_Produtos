import pyautogui
import time

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=712, y=465)

pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("enter")
time.sleep(3)

import pandas as pd     

caminho = "C:\\Users\\arthu\\OneDrive\\Documentos\\Hashtag - Pyton\\A1\\produtos.csv"
tabela = pd.read_csv(caminho)
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=714, y=302)
    codigo = tabela.loc[linha, "codigo"]
    
    pyautogui.write(str(codigo))
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
    time.sleep(1)
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    time.sleep(3)
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    
    
    
