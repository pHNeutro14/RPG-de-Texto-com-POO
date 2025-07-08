class Item:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        print(f"Item criado: {self.nome}")

    def usar(self, alvo):
        print(f"{alvo.nome} usa o item {self.nome}.")
        pass

    def descartar(self):
        print(f"Item {self.nome} descartado.")
        pass

class Arma(Item):
    def __init__(self, nome, descricao, dano, alcance): 
        super().__init__(nome, descricao)
        self.dano = dano
        self.alcance = alcance

    def equipar(self, personagem):
        print(f"{personagem.nome} equipa {self.nome}.")
        pass

    def melhorar(self):
        self.dano += 5
        print(f"{self.nome} foi melhorada! Dano agora: {self.dano}.")
        pass

class Pocao(Item):
    def __init__(self, nome, descricao, efeito, quantidade):
        super().__init__(nome, descricao)
        self.efeito = efeito
        self.quantidade = quantidade

    def beber(self, personagem):
        print(f"{personagem.nome} bebe {self.nome} e recebe o efeito: {self.efeito}.")
        self.quantidade -= 1
        pass

    def misturar(self):
        pass

class Armadura(Item):
    def __init__(self, nome, descricao, defesa, durabilidade): 
        super().__init__(nome, descricao)
        self.defesa = defesa
        self.durabilidade = durabilidade

    def vestir(self, personagem):
        print(f"{personagem.nome} veste {self.nome}.")
        pass
    
    def consertar(self):
        self.durabilidade = 100
        print(f"{self.nome} foi consertada.")
        pass