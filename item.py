class Item:
    """Classe base para todos os itens que podem ser encontrados no jogo."""
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def usar(self, personagem):
        print(f"{personagem.nome} tenta usar {self.nome}, mas nada acontece.")

class Arma(Item):
    """Representa um item do tipo Arma, que possui um valor de dano."""
    def __init__(self, nome, descricao, dano): 
        super().__init__(nome, descricao)
        self.dano = dano

class Pocao(Item):
    """Representa um item consumível, como poções de cura ou outros efeitos."""
    def __init__(self, nome, descricao, efeito, quantidade, valor_cura=0):
        super().__init__(nome, descricao)
        self.efeito = efeito
        self.quantidade = quantidade
        self.valor_cura = valor_cura

    def usar(self, personagem):
        if self.efeito == "cura" and self.quantidade > 0:
            personagem.vida += self.valor_cura
            if personagem.vida > personagem.vida_maxima:
                personagem.vida = personagem.vida_maxima
            self.quantidade -= 1
            print(f"{personagem.nome} usa {self.nome}, recuperando {self.valor_cura} de vida! Restam {self.quantidade}.")
        else:
            print(f"Não foi possível usar {self.nome}.")

class Armadura(Item):
    """Representa um item de defesa, que possui um valor de defesa."""
    def __init__(self, nome, descricao, defesa):
        super().__init__(nome, descricao)
        self.defesa = defesa

class Inventario:
    """Gerencia a coleção de itens de um personagem, controlando a capacidade."""
    def __init__(self, capacidade=50):
        self.itens = []
        self.capacidade = capacidade

    def adicionar_item(self, item):
        if len(self.itens) < self.capacidade:
            self.itens.append(item)
            print(f"'{item.nome}' foi adicionado ao inventário.")
        else:
            print("Inventário cheio!")
            
    def mostrar(self):
        print("\n--- Inventário ---")
        if not self.itens:
            print("Vazio")
        else:
            for i, item in enumerate(self.itens):
                print(f"{i+1}. {item.nome} ({item.descricao})")
        print("------------------")