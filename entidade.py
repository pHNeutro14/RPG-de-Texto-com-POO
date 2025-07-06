class Entidade:
    def __init__(self, nome, nivel, vida):
        self.nome = nome 
        self.nivel = nivel 
        self.vida = vida

    def atacar(self, alvo):

        print(f"{self.nome} ataca {alvo.nome}!")
        pass

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado.")
        pass

class Personagem(Entidade):
    def __init__(self, nome, nivel, vida, classe):
        super().__init__(nome, nivel, vida)
        self.classe = classe
        #self.inventario = Inventario() 

    def subir_nivel(self):
        self.nivel += 1
        print(f"{self.nome} subiu para o nível {self.nivel}!")
        pass

    def equipar_item(self, item):
        if item in self.inventario.itens:
            print(f"{self.nome} equipou {item.nome}.")
        else:
            print("Item não está no inventário.")
        pass

class Inimigo(Entidade):
    def __init__(self, nome, nivel, vida, tipo, loot):
        super().__init__(nome, nivel, vida)
        self.tipo = tipo 
        self.loot = loot

    def agir(self):
        print(f"O inimigo {self.nome} está agindo...")
        pass

    def fugir(self):
        print(f"{self.nome} tenta fugir!")
        pass

class Boss(Inimigo):
    def __init__(self, nome, nivel, vida, tipo, loot, habilidade_especial, dano_em_area):
        super().__init__(nome, nivel, vida, tipo, loot)
        self.habilidade_especial = habilidade_especial
        self.dano_em_area = dano_em_area 

    def usar_habilidade(self):
        print(f"{self.nome} usa sua habilidade especial: {self.habilidade_especial}!")
        pass

    def invocar_minions(self):
        print(f"{self.nome} invoca seus lacaios!")
        pass

class Guerreiro(Personagem):
    def __init__(self, nome):
        vida_base = 150
        super().__init__(nome=nome, nivel=1, vida=vida_base, classe="Guerreiro")
        self.forca_extra = 10
        self.escudo = True

    def golpe_espada(self, alvo):
        print(f"{self.nome} desfere um golpe de espada massivo em {alvo.nome}!")
        dano = 10 + self.forca_extra
        alvo.receber_dano(dano)

    def defender(self):
        print(f"{self.nome} levanta seu escudo para se defender.")
        pass

class Mago(Personagem):
    def __init__(self, nome):
        vida_base = 80
        super().__init__(nome=nome, nivel=1, vida=vida_base, classe="Mago")
        self.livro_de_magia = ["Bola de Fogo"]
        self.elementos = ["Fogo"]

    def lancar_feitico(self, feitico, alvo):
        if feitico in self.livro_de_magia:
            print(f"{self.nome} lança {feitico} em {alvo.nome}!")
        else:
            print("Feitiço desconhecido.")
        pass
    
    def regenerar_magia(self):
        print(f"{self.nome} medita para regenerar sua magia.")
        pass