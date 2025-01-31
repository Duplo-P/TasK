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
        self.check()
        self.save(date)

        
        
class Tarefa:
    def __init__(self):
        self.list = []
        
    def add(self, task):
        self.list.append(task)
        return "OK"
    
    def surch(self):
        pass
        