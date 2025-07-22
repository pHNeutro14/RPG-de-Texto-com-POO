from entidade import Guerreiro, Mago, Arqueiro, NPC
from sistema import Mapa, Missao
from item import Arma, Pocao

if __name__ == "__main__":
    

    print("="*30)
    print(" BEM-VINDO AO MEU RPG EM PYTHON ")
    print("="*30)
    nome_do_heroi = input("Digite o nome do seu herói: ")
    heroi = None
    while heroi is None:
        escolha = input(f"\n{nome_do_heroi}, escolha sua classe: (1) Guerreiro, (2) Mago, (3) Arqueiro\n> ")
        if escolha == '1': heroi = Guerreiro(nome=nome_do_heroi)
        elif escolha == '2': heroi = Mago(nome=nome_do_heroi)
        elif escolha == '3': heroi = Arqueiro(nome=nome_do_heroi)
        else: print("\nOpção inválida!")
    print(f"\n{heroi.nome}, o {heroi.classe}, está pronto para a aventura!")

    print("Você recebe um equipamento básico para sua jornada.")
    arma_inicial = Arma(nome="Adaga Gasta", descricao="Melhor que nada.", dano=5)
    pocao_inicial = Pocao(nome="Poção de Cura Fraca", descricao="Restaura 20 de vida.", efeito="cura", quantidade=10, valor_cura=20)
    heroi.inventario.adicionar_item(arma_inicial)
    heroi.inventario.adicionar_item(pocao_inicial)
    heroi.equipar_item(arma_inicial)
    mapa_do_mundo = Mapa()
    missao_chefe = Missao("O Esmagador das Montanhas", 
                      "Viaje até as Montanhas Gélidas e derrote seu líder aterrorizante.", 
                      "derrotar", "Grolnok, o Esmagador", 250)
                      
    npc_da_vila = NPC(nome="Cleverton, o Grande", nivel=10, vida=100, fala="O mal que assola esta terra reside no pico das Montanhas Gélidas.", missao_oferecida=missao_chefe)

    jogando = True
    while jogando:
        
        mapa_do_mundo.mostrar_mapa()
        print(f"\nO que você deseja fazer em '{mapa_do_mundo.get_regiao_atual().nome}'?")
        
        acao = input("(1) Explorar a região\n(2) Mover-se no mapa\n(3) Falar com Cleverton\n(4) Usar Poção de Cura\n(5) Ver inventário e status\n(6) Sair do Jogo\n> ")

        if acao == '1':
            mapa_do_mundo.get_regiao_atual().explorar(heroi)
        
        elif acao == '2':
            direcao = input("Para onde? (avancar / voltar)\n> ")
            mapa_do_mundo.mover(direcao)
            
        elif acao == '3':
            npc_da_vila.interagir(heroi)

        elif acao == '4':
            pocao_encontrada = None
            for item in heroi.inventario.itens:
                if isinstance(item, Pocao) and item.efeito == "cura":
                    pocao_encontrada = item
                    break 
            if pocao_encontrada:
                pocao_encontrada.usar(heroi)
                if pocao_encontrada.quantidade <= 0:
                    heroi.inventario.itens.remove(pocao_encontrada)
            else:
                print("Você não tem poções de cura!")

        elif acao == '5':
            heroi.inventario.mostrar()
            print(f"Vida: {heroi.vida}/{heroi.vida_maxima} | Nível: {heroi.nivel} | XP: {heroi.pontuacao.xp}/{heroi.xp_para_proximo_nivel}")
            
        elif acao == '6':
            print("Obrigado por jogar!")
            jogando = False
            
        else:
            print("Ação desconhecida.")

        if heroi.vida <= 0:
            print("\nSua jornada chega a um fim trágico... GAME OVER.")
            jogando = False