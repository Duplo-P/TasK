import json
import os 
from colorama import Fore

class BD:
    def __init__(self):
        self.bd = "bd.json"
        self.txt = "instrucao.txt"
        
    def criarTxt(self):
        string = """ 
        Este manual tem como objetivo apresentar e instruir o usuário sobre o programa de gestão de tarefas desenvolvido em Python. O programa permite adicionar, concluir, apagar e consultar tarefas, além de oferecer ajuda e a opção de sair.

Funcionalidades:

    Adicionar Tarefa:
        Descrição: Permite adicionar uma nova tarefa à lista.
        Instruções:
            O programa solicitará a descrição da tarefa. Digite a descrição e pressione Enter.
            A tarefa será adicionada à lista.

    Concluir Tarefa:
        Descrição: Permite marcar uma tarefa como concluída.
        Instruções:
            O programa exibirá a lista de tarefas com seus respectivos números.
            Digite o número da tarefa que deseja concluir e pressione Enter.
            A tarefa será marcada como concluída.

    Apagar Tarefa:
        Descrição: Permite remover uma tarefa da lista.
        Instruções:
            O programa exibirá a lista de tarefas com seus respectivos números.
            Digite o número da tarefa que deseja apagar e pressione Enter.
            A tarefa será removida da lista.

    Consultar Tarefa:
        Descrição: Permite visualizar os detalhes de uma tarefa específica.
        Instruções:
            O programa exibirá a lista de tarefas com seus respectivos números.

    Ajuda:
        Descrição: Exibe este manual de instruções.
        Instruções:
            O programa exibirá este manual de instruções.

    Sair:
        Comando: sair
        Descrição: Encerra o programa.
        Instruções:
            O programa será encerrado.
Desenvolvido por Duplo P Analytics."""
        with open(self.txt, "w") as txt:
            txt.write(string)
            
    def checkTxt(self):
        if not os.path.exists(self.txt):
            self.criarTxt()
        return True
    
    def readTxt(self):
        with open(self.txt) as txt:
            arq = txt.readlines()
        return arq
    
    def criarBd(self) -> None:
        dados = {"0":{"Tarefa":"Instalação do TasK", "Estado":"[ \U00002713 ]"}}
        with open(self.bd, "w") as date:
            json.dump(dados, date, indent = 8)
            
    def check(self)-> bool:
        if not os.path.exists(self.bd):
            self.criarBd()
        return True
    
    def read(self):
        self.check()
        with open(self.bd) as date:
            arq = json.load(date)
        return arq
    
    def save(self, dados:dict[str]) -> None:
        date_update = self.read()
        list_key = date_update.keys()
        date_update[str(int(list(list_key)[-1]) + 1)] = dados 
        with open(self.bd, "w") as date:
            json.dump(date_update, date, indent = 8)
        
    def addBd(self, date:dict[str])-> None:
        try:
            self.check()
            self.save(date)
        except:
            print("Dados Não Gravado")
            
    def safety(self, date_update):
        with open(self.bd, "w") as date:
            json.dump(date_update, date, indent = 8)
        
            

class Tarefa:
    def __init__(self):
        self.bd = BD()
        
    def add(self, task: dict[str, int]):
        self.bd.addBd(task)
        
    def delete(self, Id:str):
        bd = self.bd.read()
        if Id in list(bd.keys()):
            x = bd.pop(Id)
            self.bd.safety(bd)
            return f"Tarefa: {x["Tarefa"]} Removida."
        else:
            return f"Tarefa: {Id} Não existe."
        
    def done(self, Id):
        bd = self.bd.read()
        if Id in list(bd.keys()):
            bd[Id]["Estado"] = "[ \U00002713 ]"
            self.bd.safety(bd)
            return f"Tarefa: {bd[Id]["Tarefa"]} Concluída."
        else:
            return f"Tarefa: {Id} Não existe."
        
    def surch(self):
        for chave, valor in self.bd.read().items():
            if valor["Estado"] == "[ \U00002713 ]":
                print(f"Id: {chave}\tDescrição: " + Fore.GREEN + f"{valor["Tarefa"]}" + Fore.RESET + "\tEstado: " + Fore.GREEN + f"{valor["Estado"]}\n"+ Fore.RESET)
            else:
                print(f"Id: {chave}\tDescrição: " + Fore.MAGENTA + f"{valor["Tarefa"]}" + Fore.RESET + "\tEstado: " + Fore.MAGENTA + f"{valor["Estado"]}\n"+ Fore.RESET)

    def help(self):
        self.bd.checkTxt()
        for txt in self.bd.readTxt():
            print(txt)
        