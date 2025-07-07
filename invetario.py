class Inventario:
    def __init__(self, capacidade=10):
        self.itens = []
        self.capacidade = capacidade

    def adicionar_item(self, item):
        if len(self.itens) < self.capacidade:
            self.itens.append(item)
            print(f"'{item.nome}' foi adicionado ao inventário.")
        else:
            print("Inventário cheio!")

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"'{item.nome}' foi removido do inventário.")
        else:
            print(f"'{item.nome}' não encontrado no inventário.")

    def mostrar(self):
        print("--- Inventário ---")
        if not self.itens:
            print("Vazio")
        else:
            for item in self.itens:
                print(f"- {item.nome} ({item.descricao})")
        print("------------------")