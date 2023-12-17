import os
from colorama import Fore
open("token1.txt", "w").close()
print(Fore.CYAN + """

░ █▀▀ █▀▀ ░░▄▀ █░░ █ █▀▀ █░█ ▀█▀ █▀ ▀█▀ █▀█ █▀█ █▀▀
▄ █▄█ █▄█ ▄▀░░ █▄▄ █ █▄█ █▀█ ░█░ ▄█ ░█░ █▄█ █▀▄ ██▄
discord: sh4dv
""")
print(Fore.RESET)
def zyje():
    if os.path.exists("token.txt"):
        print(Fore.GREEN + "Found token.txt") # for support contact me on discord sh4dv or my server discord.gg/lightstore
        return True
    else:
        print("Cannot find token.txt")
        return False

if zyje():
    with open("token.txt", "r") as file:
        lines = file.readlines()  

    with open("token1.txt", "a") as filee:
        for line in lines:
            lista = line.strip().split(':') 
            if len(lista) > 2:  
                liista = lista[2]
                filee.write(liista + '\n')
                tuken = liista.split('.')
                if len(tuken) > 2:
                    print(Fore.GREEN + "Added: " + Fore.LIGHTBLACK_EX + tuken[0] + "**" + tuken[2])
                else:
                    print(Fore.GREEN + "Added: " + Fore.LIGHTBLACK_EX + liista)
    ilosc = len(lines)
    print(Fore.BLUE)
    print(f"Splitted tokens: {ilosc}")
    print(Fore.RESET)
    open("token.txt", "w").close()
	