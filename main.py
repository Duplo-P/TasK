import os 
import colorama as color

def corTxt(cor: int, txt: str):
    if cor == 0:
        return color.Fore.RED + txt + color.Fore.RESET
    elif cor == 1:
        return color.Fore.GREEN + txt + color.Fore.RESET
    elif cor == 2:
        return color.Fore.BLUE + txt + color.Fore.RESET
    elif cor == 3:
        return color.Fore.CYAN + txt + color.Fore.RESET
    elif cor == 4:
        return color.Fore.YELLOW + txt + color.Fore.RESET
    elif cor == 5:
        return color.Fore.MAGENTA + txt + color.Fore.RESET
    else:
        return txt
    
def size():
    largura, _= os.get_terminal_size()
    return largura
def sar():
    print(corTxt(0,"Sair?"))
    print(corTxt(0,"Sim ( S )\t ou Não ( N )"))
def menu():
    print(corTxt(4, "BEM VINDO AO GESTASK\n").center(size()))
    print(corTxt(5,"\n1 - Criar Tarefa\n2 - Concluir Tarefa\n3 - Apagar Tarefa\n4 - Ajuda\n5 - Sair").center(size()))
    op = input("-->> ")
   
#--------------------------------RUN-----------------
menu()
    
