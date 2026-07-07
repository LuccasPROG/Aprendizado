import pyautogui
import time
import pandas
import os

pyautogui.PAUSE = 0.5

caminho = os.path.join(os.path.dirname(__file__), 'produtos.csv')
tabela = pandas.read_csv(caminho)
link = 'dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=601, y=500)
pyautogui.write('lucaseviliton2019@gmail.com')
pyautogui.click(x=640, y=661)
pyautogui.write('123456')
pyautogui.click(x=981, y=742)
time.sleep(3)
# pyautogui.click(x=839, y=253)

for linha in tabela.index:
    pyautogui.click(x=729, y=330)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)

    pyautogui.click(x=696, y=482)
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)

    pyautogui.click(x=618, y=631)
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)

    pyautogui.click(x=681, y=783)
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)

    pyautogui.click(x=760, y=935)
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    
    pyautogui.scroll(-150)

    pyautogui.click(x=608, y=645)
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)


    pyautogui.click(x=615, y=788)
    obs = str(tabela.loc[linha, 'obs'])
    pyautogui.write(obs)

    pyautogui.click(x=840, y=890)

    pyautogui.scroll(150)