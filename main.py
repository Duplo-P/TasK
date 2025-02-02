from modulo import *
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

def sair():
    txt = corTxt(2,"Sim ( S )\t") + " ou " + corTxt(0,"\tNão ( N )")
    while True:
        os.system("clear")
        print(corTxt(4,"SAIR?\n").center(size()))
        print(txt.center(size()))
        op = input("->> ").upper()
        if op == "S":
            os.system("clear")
            return exit(corTxt(0,"Programa termindado.."))
        elif op == "N":
            return menu()
        else:
            print("Escolha uma das Opções.")
            
def pergunta():
    print(corTxt(3,"S ( Sair ) Enter ( Continuar )"))
    op = input("->> ").upper()
    if op == "S":
        os.system("clear")
        return menu()
    
def saida():
    input(corTxt(3,"Preciona Enter para sair..."))
    os.system("clear")
    
def ajudar(obj):
    os.system("clear")
    print(corTxt(4, "AJUDA\n").center(size())) 
    obj.help() 
    saida()    

def apagar(obj):
    while True:
        os.system("clear")
        print(corTxt(4,"APAGAR\n").center(size())) 
        obj.surch()
        id = input(corTxt(11,"Digite o Id: "))
        print(corTxt(1, obj.delete(id)))
        pergunta()

def add(obj):
    while True:
        os.system("clear")
        print(corTxt(4,"ADD").center(size()))
        tarefa = input("Tarefa: ").title()
        estado = "[ Em Progresso ]"
        obj.add({"Tarefa":tarefa, "Estado":estado})
        print(corTxt(1, "Tarefa Guardado com Sucesso."))
        pergunta()
        
def concluir(obj):
    while True:
        os.system("clear")
        print(corTxt(4,"CONCLUIR\n").center(size()))
        obj.surch()
        id = input("Tarefa: ")
        print(corTxt(1, obj.done(id)))
        pergunta()

def mostrar(obj):
    os.system("clear")
    print(corTxt(4,"CONSUTAR\n").center(size()))
    obj.surch()
    saida()
    
def menu():
    os.system("clear")
    Task = Tarefa()
    while True:
        print(corTxt(4, "BEM VINDO AO GESTASK\n").center(size()))
        print(corTxt(5,"\n1 - Criar Tarefa\n2 - Concluir Tarefa\n3 - Apagar Tarefa\n4 - Mostrar\n5 - Ajuda\n6 - Sair").center(size()))
        op = input("-->> ")
        if op == "1":
            add(Task)
        elif op == "2":
            concluir(Task)
        elif op == "3":
            apagar(Task)
        elif op == "4":
            mostrar(Task)
        elif op == "5":
            ajudar(Task)
        elif op == "6":
            sair()
        else:
            os.system("clear")
            print("Escolhe uma das opções.")
   
#--------------------------------RUN-----------------
menu()
    
