#autores @brujeriatech And @azahar qxzcw
import requests
import random
import os
import time

os.system("clear")
print('''
        ,---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
        |1/2| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | + | ' | <-    |
        |---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|
        | ->| | Q | W | E | R | T | Y | U | I | O | P | ] | ^ |     |
        |-----',--',--',--',--',--',--',--',--',--',--',--',--'|    |
        | Caps | A | S | D | F | G | H | J | K | L | \ | [ | * |    |
        |----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----|
        |    | < | Z | X | C | V | B | N | M | , | . | - |          |
        |----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|
        | ctrl |  | alt |                          |altgr |  | ctrl |
        '------'  '-----'--------------------------'------'  '------'
''')
print("Authores Azahar Y brujeriatech ! ")
print("sends Usernames and passwords  Randoms Atack bucle ")
print("")
url = input("URL phishing a atacar > ") 
print("")
# Genera username y passwords random
def random_word():
    word = ''
    for i in range(10):
        word += random.choice('abcdefghijklmnopqrstuvwxyz1234567890._')
    return word

# Manda la petición
def send_post(url, username, password):
    data = {"password": password}
    try:
        r = requests.post(url, data=data)
        if r.status_code == 200:
            print('OK - Enviado: username ' + username + ' password ' + password)
        else:
            return "Error"
    except requests.exceptions.RequestException as e:
        return "Error"

#bucle
while True:
    username = random_word()
    password = random_word()
    send_post(f"{url}" + username, username, password)
