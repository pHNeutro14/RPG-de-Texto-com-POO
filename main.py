# Importa as classes de personagens e NPCs do arquivo de entidades.
from entidade import Guerreiro, Mago, Arqueiro, NPC
# Importa as classes de sistemas do jogo, como o Mapa e as Missões.
from sistema import Mapa, Missao
# Importa as classes de itens que o jogador pode usar.
from item import Arma, Pocao

# Garante que o código abaixo só será executado quando este arquivo for rodado diretamente.
if __name__ == "__main__":
        
    # Exibe uma mensagem de boas-vindas para o jogador.
    print("="*26)
    print(" BEM-VINDO AO RPG DE TEXTO ")
    print("="*26)
    
    # Pede ao jogador para inserir o nome do herói.
    nome_do_heroi = input("Digite o nome do seu herói: ")
    
    # Inicia a variável 'heroi' como None (vazia).
    heroi = None
    # Inicia um loop que continua até o jogador fazer uma escolha de classe válida (1, 2 ou 3).
    while heroi is None:
        escolha = input(f"\n{nome_do_heroi}, escolha sua classe: (1) Guerreiro, (2) Mago, (3) Arqueiro\n> ")
        # Cria uma instância da classe escolhida (Guerreiro, Mago ou Arqueiro).
        if escolha == '1': heroi = Guerreiro(nome=nome_do_heroi)
        elif escolha == '2': heroi = Mago(nome=nome_do_heroi)
        elif escolha == '3': heroi = Arqueiro(nome=nome_do_heroi)
        else: print("\nOpção inválida!")
    
    print(f"\n{heroi.nome}, o {heroi.classe}, está pronto para a aventura!")

    print("Você recebe um equipamento básico para sua jornada.")
    # Cria instâncias dos objetos de item que o jogador terá no início.
    arma_inicial = Arma(nome="Adaga Gasta", descricao="Melhor que nada.", dano=5)
    pocao_inicial = Pocao(nome="Poção de Cura Fraca", descricao="Restaura 20 de vida.", efeito="cura", quantidade=10, valor_cura=20)
    
    # Adiciona os itens criados ao inventário do herói.
    heroi.inventario.adicionar_item(arma_inicial)
    heroi.inventario.adicionar_item(pocao_inicial)
    
    # Equipa a arma inicial automaticamente para que o herói já comece com ela em mãos.
    heroi.equipar_item(arma_inicial)
    
    # Cria a instância principal do mapa do mundo, que contém todas as regiões.
    mapa_do_mundo = Mapa()
    
    # Cria um objeto de missão que será entregue pelo NPC.
    missao_chefe = Missao("O Esmagador das Montanhas", 
                          "Viaje até as Montanhas Gélidas e derrote seu líder aterrorizante.", 
                          "derrotar", "Grolnok, o Esmagador", 250)
                          
    # Cria o NPC, definindo seu nome, status e associando a missão a ele.
    npc_da_vila = NPC(nome="Cleverton, o Grande", nivel=10, vida=100, fala="O mal que assola esta terra reside no pico das Montanhas Gélidas.", missao_oferecida=missao_chefe)

    # A variável 'jogando' controla o estado principal do jogo. O loop continua enquanto for True.
    jogando = True
    while jogando:
        
        # A cada turno, o mapa é exibido para orientar o jogador.
        mapa_do_mundo.mostrar_mapa()
        print(f"\nO que você deseja fazer em '{mapa_do_mundo.get_regiao_atual().nome}'?")
        
        # Pede ao jogador para escolher uma ação do menu principal.
        acao = input("(1) Explorar a região\n(2) Mover-se no mapa\n(3) Falar com Cleverton\n(4) Usar Poção de Cura\n(5) Ver inventário e status\n(6) Sair do Jogo\n> ")

        # Bloco de decisão que executa o código correspondente à escolha do jogador.
        if acao == '1':
            # Delega a ação de explorar para o método da região atual. 
            # Toda a lógica de eventos (combate, tesouro) está encapsulada lá.
            mapa_do_mundo.get_regiao_atual().explorar(heroi)
        
        elif acao == '2':
            # Pede uma direção e delega a ação de mover para o objeto do mapa.
            direcao = input("Para onde? (avancar / voltar)\n> ")
            mapa_do_mundo.mover(direcao)
            
        elif acao == '3':
            # Inicia a interação com o objeto NPC.
            npc_da_vila.interagir(heroi)

        elif acao == '4':
            # Lógica para encontrar e usar uma poção de cura do inventário.
            pocao_encontrada = None
            # Itera sobre a lista de itens do herói.
            for item in heroi.inventario.itens:
                # Verifica se o item é uma Poção e se é de cura.
                if isinstance(item, Pocao) and item.efeito == "cura":
                    pocao_encontrada = item
                    break # Para a busca assim que a primeira poção é encontrada.
            
            if pocao_encontrada:
                # Se uma poção foi encontrada, chama o método 'usar' dela.
                pocao_encontrada.usar(heroi)
                # Se a quantidade chegar a zero, o item é removido do inventário.
                if pocao_encontrada.quantidade <= 0:
                    heroi.inventario.itens.remove(pocao_encontrada)
            else:
                # Informa o jogador caso ele não tenha poções.
                print("Você não tem poções de cura!")

        elif acao == '5':
            # Mostra a lista de itens e os status atuais do herói.
            heroi.inventario.mostrar()
            print(f"Vida: {heroi.vida}/{heroi.vida_maxima} | Nível: {heroi.nivel} | XP: {heroi.pontuacao.xp}/{heroi.xp_para_proximo_nivel}")
            
        elif acao == '6':
            # Encerra o jogo.
            print("Obrigado por jogar!")
            jogando = False # Altera a variável para que o loop 'while' termine.
            
        else:
            # Captura qualquer entrada inválida no menu principal.
            print("Ação desconhecida.")

        # Ao final de cada turno, verifica se a vida do herói chegou a zero.
        if heroi.vida <= 0:
            print("\nSua jornada chega a um fim trágico... GAME OVER.")
            jogando = False # Encerra o loop principal.