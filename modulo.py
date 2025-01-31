import json
import os 

class BD:
    def __init__(self):
        self.bd = "bd.json"
        
    def criarBd(self) -> None:
        dados = {"0":" "}
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
            

class Tarefa:
    def __init__(self):
        self.bd = BD()
        
    def add(self, task: dict[str, int]):
        self.bd.addBd(task)
        
    def delete(self, Id:str):
        bd = self.bd.read()
        if Id in list(bd.keys()):
            x = bd.pop(Id)
            self.bd.save(bd)
            return f"Tarefa: {x["Tarefa"]} Removida."
        else:
            return f"Tarefa: {Id} Não existe."
        
    def Done(self, Id):
        bd = self.bd.read()
        if Id in list(bd.keys()):
            bd[Id]["Estado"] = "[\U00002713]"
            self.bd.save(bd)
            return f"Tarefa: {bd[Id]["Tarefa"]} Concluída."
        else:
            return f"Tarefa: {Id} Não existe."
        
        
    def surch(self):
        for chave, valor in self.bd.read().items():
            print(f"Id: {chave}\tTarefa: {valor["Tarefa"]}\tEstado: {valor["Estado"]}\n")
        