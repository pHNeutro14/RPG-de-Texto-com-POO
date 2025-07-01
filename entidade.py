class Entidade:
    def __init__(self, nome, nivel, vida, mana, forca, inteligencia, destreza):
        self.nome = nome
        self.nivel = nivel
        self.vida = vida
        self.mana = mana
        self.forca = forca
        self.inteligencia = inteligencia
        self.destreza = destreza

    def atacar():pass

    def receber_dano():pass

class Personagem(Entidade):
    def __init__(self, nome, nivel, vida, mana, forca, inteligencia, destreza, classe_rpg, experiencia=0, inventario=None):
        super().__init__(nome, nivel, vida, mana, forca, inteligencia, destreza)
        
        self.classe_rpg = classe_rpg
        self.experiencia = experiencia
        self.invetario = inventario

    def receber_experiencia():pass

    def subir_nivel():pass

    def equipar_item():pass

class Guerreiro(Personagem):
    def __init__(self, nome): pass    

class Mago(Personagem): pass

class Arqueiro(Personagem): pass
