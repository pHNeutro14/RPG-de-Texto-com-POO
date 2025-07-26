from item import Inventario, Arma, Armadura

class Pontuacao:
    """Gerencia a experiência (xp) e as moedas de um personagem."""
    def __init__(self):
        self.xp = 0
        self.moedas = 0

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        print(f"Ganhou {quantidade} de experiência!")

    def gastar_moedas(self, quantidade):
        if self.moedas >= quantidade:
            self.moedas -= quantidade
            return True
        else:
            print("Moedas insuficientes!")
            return False

class Entidade:
    """Classe base para todos os seres vivos do jogo (personagens, inimigos, etc.)."""
    def __init__(self, nome, nivel, vida):
        self.nome = nome 
        self.nivel = nivel 
        self.vida = vida
        self.vida_maxima = vida

    def atacar(self, alvo):
        dano = self.nivel
        print(f"{self.nome} ataca {alvo.nome}, causando {dano} de dano!")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}/{self.vida_maxima}")
        if self.vida == 0:
            print(f"{self.nome} foi derrotado.")

class Personagem(Entidade):
    """Classe base para todos os personagens jogáveis, herdando de Entidade."""
    def __init__(self, nome, nivel, vida, classe):
        super().__init__(nome, nivel, vida)
        self.classe = classe
        self.inventario = Inventario()
        self.pontuacao = Pontuacao()
        self.xp_para_proximo_nivel = 100
        self.arma_equipada = None
        self.armadura_equipada = None
        self.missao_ativa = None

    def subir_nivel(self):
        if self.pontuacao.xp >= self.xp_para_proximo_nivel:
            self.nivel += 1
            self.vida_maxima += 20
            self.vida = self.vida_maxima
            self.pontuacao.xp -= self.xp_para_proximo_nivel
            self.xp_para_proximo_nivel = int(self.xp_para_proximo_nivel * 1.5)
            print(f"** PARABÉNS! {self.nome} subiu para o nível {self.nivel}! **")

    def equipar_item(self, item):
        if isinstance(item, Arma):
            self.arma_equipada = item
            print(f"{self.nome} equipou a arma: {item.nome}.")
        elif isinstance(item, Armadura):
            self.armadura_equipada = item
            print(f"{self.nome} vestiu a armadura: {item.nome}.")
        else:
            print(f"Não é possível equipar {item.nome}.")

class NPC(Personagem):
    """Representa um Personagem Não-Jogável (NPC) com quem o jogador pode interagir."""
    def __init__(self, nome, nivel, vida, fala, missao_oferecida=None):
        super().__init__(nome, nivel, vida, classe="NPC")
        self.fala = fala
        self.missao_oferecida = missao_oferecida

    def interagir(self, personagem):
        print(f"\n[{self.nome}]: '{self.fala}'")
        
        conversando = True
        while conversando:
            print("\nOpções de Diálogo:")
            escolha = input("(1) Pedir missão\n(2) Despedir-se\n> ")

            if escolha == '1':
                self.entregar_missao(personagem)
            elif escolha == '2':
                print(f"[{self.nome}]: Adeus, herói.")
                conversando = False
            else:
                print("Opção inválida.")

    def entregar_missao(self, personagem):
        if self.missao_oferecida and not self.missao_oferecida.concluida:
            if personagem.missao_ativa is None:
                personagem.missao_ativa = self.missao_oferecida
                print(f"[{self.nome}]: '{self.missao_oferecida.descricao}'")
                print(f"** Nova Missão: {self.missao_oferecida.titulo} **")
            else:
                print(f"[{self.nome}]: Você já está ocupado com a missão '{personagem.missao_ativa.titulo}'.")
        else:
            print(f"[{self.nome}]: Não tenho nenhuma missão para você agora.")
            
class Inimigo(Entidade):
    """Classe base para todos os inimigos que o jogador pode enfrentar."""
    def __init__(self, nome, nivel, vida, tipo, loot_xp, dano_base):
        super().__init__(nome, nivel, vida)
        self.tipo = tipo
        self.loot_xp = loot_xp
        self.dano_base = dano_base

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome}!")
        alvo.receber_dano(self.dano_base)

class Chefe(Inimigo):
    """Representa um Inimigo mais forte e único, com habilidades especiais."""
    def __init__(self, nome, nivel, vida, tipo, loot_xp, dano_base, habilidade_especial, dano_em_area):
        super().__init__(nome, nivel, vida, tipo, loot_xp, dano_base)
        self.habilidade_especial = habilidade_especial
        self.dano_em_area = dano_em_area

    def usar_habilidade(self, alvo):
        dano_habilidade = self.dano_base * 2
        print(f"{self.nome} usa sua habilidade especial: {self.habilidade_especial}!")
        print(f"Um golpe devastador atinge {alvo.nome}!")
        alvo.receber_dano(dano_habilidade)

    def rugir(self):
        print(f"{self.nome} solta um rugido aterrorizante!")

    def atacar(self, alvo):
        dano_chefe = int(self.dano_base * 1.5) 
        print(f"{self.nome} ataca ferozmente {alvo.nome}!")
        alvo.receber_dano(dano_chefe)

class Guerreiro(Personagem):
    """Classe especializada para o personagem do tipo Guerreiro."""
    def __init__(self, nome):
        super().__init__(nome=nome, nivel=1, vida=150, classe="Guerreiro")
        self.forca_extra = 10
        self.escudo = True
    
    def atacar(self, alvo):
        dano = self.forca_extra
        if self.arma_equipada:
            dano += self.arma_equipada.dano
        alvo.receber_dano(dano)

    def defender(self):
        print(f"{self.nome} se defende com o escudo!")

class Mago(Personagem):
    """Classe especializada para o personagem do tipo Mago."""
    def __init__(self, nome):
        super().__init__(nome=nome, nivel=1, vida=80, classe="Mago")
        self.grimorio = ["Míssil Arcano", "Raio de Gelo"]
        self.elemento = "Arcano"

    def lancar_feitico(self, nome_feitico, alvo):
        if nome_feitico in self.grimorio:
            dano = 15 
            print(f"{self.nome} lança '{nome_feitico}' de elemento {self.elemento} em {alvo.nome}!")
            alvo.receber_dano(dano)
        else:
            print(f"{self.nome} tenta, mas não conhece o feitiço '{nome_feitico}'.")

    def trocar_elemento(self):
        if self.elemento == "Arcano":
            self.elemento = "Fogo"
        else:
            self.elemento = "Arcano"
        print(f"{self.nome} agora canaliza o elemento {self.elemento}!")

    def atacar(self, alvo):
        if self.grimorio:
            self.lancar_feitico(self.grimorio[0], alvo)
        else:
            print(f"{self.nome} não tem feitiços em seu grimório!")
            super().atacar(alvo) 

class Arqueiro(Personagem):
    """Classe especializada para o personagem do tipo Arqueiro."""
    def __init__(self, nome):
        super().__init__(nome=nome, nivel=1, vida=100, classe="Arqueiro")
        self.agilidade = 15
        self.esta_mirando = False

    def mirar(self):
        print(f"{self.nome} para e mira cuidadosamente.")
        self.esta_mirando = True

    def atacar(self, alvo):
        dano = self.agilidade
        if self.esta_mirando:
            print("O tiro mirado é certeiro!")
            dano = int(dano * 1.5)
            self.esta_mirando = False
        if self.arma_equipada: dano += self.arma_equipada.dano
        alvo.receber_dano(dano)