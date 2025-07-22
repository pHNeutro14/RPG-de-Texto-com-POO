import random
from entidade import Inimigo, Chefe, Personagem, Guerreiro, Mago, Arqueiro
from item import Pocao

class Missao:
    def __init__(self, titulo, descricao, tipo_objetivo, alvo_objetivo, recompensa_xp):
        self.titulo = titulo
        self.descricao = descricao
        self.tipo_objetivo = tipo_objetivo 
        self.alvo_objetivo = alvo_objetivo 
        self.recompensa_xp = recompensa_xp
        self.concluida = False

class Combate:
    def __init__(self, personagem, inimigo):
        self.personagem = personagem
        self.inimigo = inimigo
    
    def iniciar_combate(self):
        print(f"\n--- Combate iniciado: {self.personagem.nome} vs {self.inimigo.nome} ---")
        while self.personagem.vida > 0 and self.inimigo.vida > 0:
            self.turno_jogador()
            if self.inimigo.vida <= 0: return self.verificar_vitoria()
            self.turno_inimigo()
            if self.personagem.vida <= 0: return self.verificar_vitoria()
        return self.verificar_vitoria()

    def turno_jogador(self):
        print(f"\nSua Vida: {self.personagem.vida}/{self.personagem.vida_maxima} | Vida do {self.inimigo.nome}: {self.inimigo.vida}/{self.inimigo.vida_maxima}")
        print("--- Seu Turno ---")
        acao_valida = False

        while not acao_valida:
            print("Escolha sua ação:")

            if isinstance(self.personagem, Guerreiro):
                escolha = input("(1) Atacar\n(2) Defender\n> ")
                if escolha == '1': self.personagem.atacar(self.inimigo); acao_valida = True
                elif escolha == '2': self.personagem.defender(); acao_valida = True
                else: print("Opção inválida.")

            elif isinstance(self.personagem, Mago):
                escolha = input("(1) Lançar Míssil Arcano\n(2) Trocar Elemento\n> ")
                if escolha == '1': self.personagem.lancar_feitico("Míssil Arcano", self.inimigo); acao_valida = True
                elif escolha == '2': self.personagem.trocar_elemento(); acao_valida = True
                else: print("Opção inválida.")

            elif isinstance(self.personagem, Arqueiro):
                escolha = input("(1) Atirar Flecha\n(2) Mirar\n> ")
                if escolha == '1': self.personagem.atacar(self.inimigo); acao_valida = True
                elif escolha == '2': self.personagem.mirar(); acao_valida = True
                else: print("Opção inválida.")

    def turno_inimigo(self):
        print("\n--- Turno do Inimigo ---")
        self.inimigo.atacar(self.personagem)

    def verificar_vitoria(self):
        if self.inimigo.vida <= 0:
            print(f"Você venceu o combate contra {self.inimigo.nome}!")
            if hasattr(self.personagem, 'pontuacao'):
                 self.personagem.pontuacao.ganhar_xp(self.inimigo.loot_xp)
                 self.personagem.subir_nivel()
            return True
        elif self.personagem.vida <= 0:
            print(f"Você foi derrotado por {self.inimigo.nome}.")
            return False

    def entregar_missao(self, personagem):
        if personagem.missao_ativa:
            print(f"[{self.nome}]: Termine sua missão atual primeiro!")
            return
        personagem.missao_ativa = self.missao_oferecida
        print(f"[{self.nome}]: '{self.missao_oferecida.descricao}'")
        print(f"** Nova Missão: {self.missao_oferecida.titulo} **")

class NPC(Personagem):
    def __init__(self, nome, nivel, vida, fala, missao_oferecida=None):
        super().__init__(nome, nivel, vida, classe="NPC")
        self.fala = fala
        self.missao_oferecida = missao_oferecida

    def interagir(self, personagem):
        print(f"[{self.nome}]: '{self.fala}'")

    def entregar_missao(self, personagem):
        if personagem.missao_ativa:
            print(f"[{self.nome}]: Termine sua missão atual primeiro!")
            return
        personagem.missao_ativa = self.missao_oferecida
        print(f"[{self.nome}]: '{self.missao_oferecida.descricao}'")
        print(f"** Nova Missão: {self.missao_oferecida.titulo} **")

class Evento: 
    def __init__(self, descricao, tipo, personagem, regiao):
        self.descricao = descricao 
        self.tipo = tipo
        self.personagem = personagem
        self.regiao = regiao

    def executar(self):
        print(self.descricao)
        if self.tipo == "combate":
            nome_inimigo = random.choice(self.regiao.tipos_de_inimigos)
            inimigo_evento = Inimigo(nome=nome_inimigo, nivel=self.regiao.dificuldade, vida=30 + 10*self.regiao.dificuldade, tipo="Besta", loot_xp=20*self.regiao.dificuldade, dano_base=5 + 2*self.regiao.dificuldade)
            combate = Combate(self.personagem, inimigo_evento)
            combate.iniciar_combate()
        elif self.tipo == "tesouro":
            print("Você encontra um baú antigo!")
            item = Pocao("Poção de Cura", "Cura um pouco.", "cura", 1, 30)
            self.personagem.inventario.adicionar_item(item)

class Regiao: 
    def __init__(self, nome, dificuldade, tipos_de_inimigos, is_chefe=False):
        self.nome = nome
        self.dificuldade = dificuldade
        self.tipos_de_inimigos = tipos_de_inimigos
        self.is_chefe = is_chefe

    def explorar(self, personagem):
        print(f"\n{personagem.nome} explora {self.nome}...")
        if self.is_chefe:
            self.gerar_evento_chefe(personagem)
        else:
            self.gerar_evento_normal(personagem)

    def gerar_evento_normal(self, personagem):
        chance = random.randint(1, 100)
        if chance <= 60:
            evento = Evento("Você é emboscado!", "combate", personagem, self)
            evento.executar()
        elif chance <= 80:
            evento = Evento("Algo brilha no chão...", "tesouro", personagem, self)
            evento.executar()
        else:
            print("A área parece calma por enquanto.")

    def gerar_evento_chefe(self, personagem):
        print("Um ar pesado e ameaçador toma conta do lugar...")
        print("Você encontra um trono rústico, e nele, uma figura imponente se levanta!")
        
        chefe_orc = Chefe(nome="Grolnok, o Esmagador", nivel=5, vida=200, tipo="Chefe Orc", 
                          loot_xp=200, dano_base=15, 
                          habilidade_especial="Fúria Selvagem", dano_em_area=False)
        
        combate = Combate(personagem, chefe_orc)
        combate.iniciar_combate()

class Mapa:
    def __init__(self):
        self.regioes = [
            Regiao("Floresta dos Sussurros", 1, ["Lobo", "Goblin Batedor"]),
            Regiao("Pântano Sombrio", 3, ["Sanguessuga Gigante", "Zumbi do Pântano"]),
            Regiao("Montanhas Gélidas", 5, [], is_chefe=True)
        ]
        self.posicao_atual_idx = 0

    def mover(self, direcao):
        if direcao == "avançar" and self.posicao_atual_idx < len(self.regioes) - 1:
            self.posicao_atual_idx += 1
            print(f"Você viaja para {self.get_regiao_atual().nome}.")
        elif direcao == "voltar" and self.posicao_atual_idx > 0:
            self.posicao_atual_idx -= 1
            print(f"Você retorna para {self.get_regiao_atual().nome}.")
        else:
            print("Você não pode ir por esse caminho.")

    def mostrar_mapa(self):
        print("\n--- Mapa do Mundo ---")
        for i, regiao in enumerate(self.regioes):
            if i == self.posicao_atual_idx:
                print(f"-> {i+1}. {regiao.nome} (Você está aqui)")
            else:
                print(f"   {i+1}. {regiao.nome}")
        print("---------------------")
    
    def get_regiao_atual(self):
        return self.regioes[self.posicao_atual_idx]