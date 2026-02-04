# Importa as bibliotecas (bem óbvio)

import keyboard
import pyautogui as py
import time
import json
import random
import tkinter as tk
from tkinter import simpledialog

# Faz o tkinter funcionar

root = tk.Tk()
root.withdraw()

# Abre os arquivos json

arquivo = open("nomes.json", "r")
dados = json.load(arquivo)

arquivo2 = open("email.json", "r")
dados2 = json.load(arquivo2)

# Aqui tu bota o link do site

link_do_negocio = "LINK_DO_SITE"

# Isso aqui faz uma caixinha aparecer e tu bota um número inteiro de quantas vezes vc quer que repita 

gugu = simpledialog.askinteger("Quantidade de loops", "Quantas vezes você quer que repita?")

# Aqui faz um loop de acordo com o número que você colocou ali na caixa de texto, escolhe dois nomes e um email aleatório dos json, e faz o resto ali

for i in range(gugu):

    nome1 = random.choice(dados)
    nome2 = nome1['nome']

    nome3 = random.choice(dados)
    nome4 = nome3['nome']

    email1 = random.choice(dados2)
    email2 = email1['email']

    
    keyboard.press_and_release("ctrl+shift+p")
    time.sleep(0.5)
    keyboard.write(link_do_negocio)
    keyboard.press("enter")
    time.sleep(6)
    py.click(x = 1421, y = 464)
    time.sleep(0.4)
    keyboard.write(nome2)
    time.sleep(0.4)
    py.click(x = 1461, y = 542)
    time.sleep(0.4)
    keyboard.write(nome4)
    time.sleep(0.4)
    py.click(x = 1484, y = 615)
    time.sleep(0.4)
    keyboard.write(email2)
    time.sleep(0.4)
    py.click(x = 1279, y = 874)
    time.sleep(0.5)
    py.click(x = 1374, y = 831)
    time.sleep(0.2)
    py.scroll(-200)
    time.sleep(0.3)
    py.click(x = 1461, y = 932)
    time.sleep(3)
    py.scroll(-2000)
    time.sleep(0.5)
    py.click(x = 1007, y = 758)
    time.sleep(3)
    keyboard.press_and_release("alt+f4")
    time.sleep(6)



    
