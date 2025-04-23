import pandas as pd
import random
import menus_dic
import os
import time
startups = []
fase_batalha = []
vencedores = []
rodada = 0


def iniciar_competicao(startups: list):
    """
    Inicia a competição entre startups, organizando as rodadas de batalha até restar apenas uma vencedora.

    Parâmetros:
    startups (list): Lista contendo os objetos das startups participantes da competição.

    Comportamento:
    - Zera as variáveis globais relacionadas à fase de batalha, vencedores e número da rodada.
    - Executa rodadas de batalhas sorteando confrontos entre as startups.
    - Ao final de cada rodada, avança com os vencedores para a próxima.
    - Quando restar apenas uma startup, exibe o relatório final da competição.

    Observações:
    - Utiliza variáveis globais: `fase_batalha`, `vencedores` e `rodada`.
    - Funções auxiliares utilizadas: `limpar_terminal()`, `sorteio_de_batalha()`, `gerenciador_de_batalha()`, `relatorio_final()`.
    """
    global fase_batalha, vencedores, rodada
    rodada = 0
    fase_batalha.clear()
    vencedores.clear()

    participantes = startups[:]
    todas_as_startups = startups[:]

    while len(participantes) > 1:
        rodada += 1
        limpar_terminal()
        print(f"\n===== INÍCIO DA RODADA {rodada} =====")
        sorteio_de_batalha(participantes)
        gerenciador_de_batalha(fase_batalha)
        participantes = vencedores[:]
        vencedores.clear()
        if len(participantes) <= 1:
            break
    relatorio_final(todas_as_startups)


def gerenciador_de_batalha(lista_geral: list):
    """
    Gerencia as batalhas de uma rodada, permitindo ao usuário escolher quais confrontos iniciar.

    Parâmetros:
    lista_geral (list): Lista de batalhas da rodada atual, onde cada batalha é uma tupla com duas startups.

    Comportamento:
    - Exibe as batalhas disponíveis.
    - Permite ao usuário iniciar uma batalha específica, visualizar o placar, ou acessar as configurações.
    - Ao escolher uma batalha, ela é removida da lista e o vencedor é adicionado à lista global `vencedores`.
    - Oferece opção para sair do gerenciador.

    Entradas válidas:
    - Número da batalha a ser iniciada (índice da lista).
    # Features:
    - '99' para mostrar o placar atual.
    - '00' para acessar o menu de configurações.
    - 's' para sair do gerenciador.

    Observações:
    - Utiliza variáveis globais: `fase_batalha`, `vencedores`.
    - Depende das funções auxiliares: `limpar_terminal()`, `placar_atual()`, `config()`, `batalha()`.
    - A variável `startups` precisa estar disponível no escopo global para ser usada nas configurações.
    """
    global vencedores, fase_batalha
    while lista_geral:

        print("===== Gerenciador de Batalha =====")
        print("--- Batalhas disponíveis ---")
        for i, j in enumerate(lista_geral):
            print(f"{i} - {j[0].nome} vs {j[1].nome}")
        escolha = str(input(
            "Digite o número da Batalha que deseja iniciar | 99 para mostrar o placar | 00 para entrar nas configurações (ou 's' para sair): ")).strip().lower()
        limpar_terminal()
        if escolha == '99':
            limpar_terminal()
            placar_atual(fase_batalha, vencedores)
            continue

        if escolha == '00':
            limpar_terminal()
            config(startups)
            continue

        if escolha == 's':
            print("Encerrando o gerenciamento de Batalha")
            break
        try:
            escolha = int(escolha)
            if 0 <= escolha < len(lista_geral):
                bat_escolhida = lista_geral.pop(escolha)
                vencedor = batalha(bat_escolhida)
                vencedores.append(vencedor)
            else:
                print("Número de batalha inválido!")
        except ValueError:
            print("Entrada inválida. Digite um número ou 's' para sair.")


def batalha(sub_list: list):
    """
    Executa uma batalha entre duas startups, permitindo ao usuário aplicar eventos em cada uma.

    Parâmetros:
    sub_list (list): Lista com duas startups que irão batalhar, na forma [startup1, startup2].

    Comportamento:
    - Para cada startup, permite a aplicação de eventos disponíveis (sem repetição).
    - Eventos são escolhidos via input do usuário a partir de um menu.
    - Cada evento é aplicado diretamente na startup, e seu ID é registrado.
    - Após os eventos serem aplicados em ambas as startups, é determinada a vencedora.
    - A tela é limpa ao final da batalha.

    Retorna:
    Startup: Objeto da startup vencedora da batalha.

    Observações:
    - Utiliza funções auxiliares: `menus_dic.menu_eventos()`, `verificar_vencedor()`, `limpar_terminal()`.
    - Os eventos aplicados são armazenados na lista `eventos_aplicados` da startup.
    - O dicionário `menus_dic.eventos` contém os eventos disponíveis (ID como chave e função como valor).
    """
    startup1, startup2 = sub_list
    print(f"\n--- Batalha entre {startup1.nome} e {startup2.nome} ---")

    for i, startup in enumerate([startup1, startup2], start=1):
        print(f"\nSelecione os eventos para a Startup {startup.nome}")
        eventos_usados = []

        while True:
            print(menus_dic.menu_eventos())
            print("0: Encerrar seleção")

            try:
                escolha = int(input("Digite o número do evento: "))
                if escolha == 0:
                    break
                elif escolha in menus_dic.eventos and escolha not in eventos_usados:
                    func = menus_dic.eventos[escolha]
                    func(startup)
                    eventos_usados.append(escolha)
                    startup.eventos_aplicados.append(escolha)
                    print(
                        f"Evento '{menus_dic.nomes_eventos[escolha]}' aplicado em {startup.nome}")
                else:
                    print("Evento inválido ou já usado.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    vencedor = verificar_vencedor(startup1, startup2)
    limpar_terminal()
    return vencedor


def limpar_terminal():
    """
    Limpa o terminal de acordo com o sistema operacional.

    Comportamento:
    - Se o sistema for Windows (`os.name == 'nt'`), executa o comando `cls`.
    - Para outros sistemas (Linux/MacOS), executa o comando `clear`.
    """
    sistema = os.name
    if sistema == 'nt': 
        os.system('cls')  # Para Windows
    else:  
        os.system('clear')  # Para Linux/MacOS


def sorteio_de_batalha(lista_geral: list):
    """
    Realiza o sorteio das batalhas da rodada, formando pares de startups para competir.

    Parâmetros:
    lista_geral (list): Lista de startups participantes da rodada atual.

    Comportamento:
    - Limpa a lista global `fase_batalha` e cria uma cópia da lista original.
    - Se o número de startups for ímpar, uma é escolhida aleatoriamente para avançar direto à próxima fase.
    - Embaralha as startups restantes e forma pares de batalhas, que são adicionadas à lista `fase_batalha`.

    Observações:
    - Utiliza variáveis globais: `fase_batalha`, `vencedores`.
    - Usa a função `random.shuffle()` para garantir aleatoriedade nos confrontos.
    - A startup que avança automaticamente (em caso de número ímpar) é informada ao usuário via `print`.
    """
    global vencedores, fase_batalha
    fase_batalha.clear()
    lista_temp = lista_geral[:]
    num_startups = len(lista_temp)
    # Se o número de startups for ímpar, uma vai direto pros vencedores
    if num_startups % 2 != 0:
        print("Número ímpar de startups, uma será automaticamente para a próxima fase.")
        startup_automatica = lista_temp.pop(random.randint(
            0, len(lista_temp) - 1))  # remove uma da lista de pares
        vencedores.append(startup_automatica)
        print(
            f"A startup {startup_automatica.nome} passou automaticamente para a próxima fase.")
    # Embaralha as startups restantes
    random.shuffle(lista_temp)
    for i in range(0, len(lista_temp), 2):
        fase_batalha.append([lista_temp[i], lista_temp[i+1]])


def verificar_vencedor(startup1, startup2):
    """
    Compara os pontos das duas startups e define a vencedora da batalha.

    Parâmetros:
    startup1: Objeto da primeira startup.
    startup2: Objeto da segunda startup.

    Comportamento:
    - A startup com maior pontuação vence e recebe +30 pontos.
    - Em caso de empate, ocorre uma "shark fight" (sorteio aleatório) para definir o vencedor, que recebe +32 pontos.
    - A startup vencedora é retornada e sua pontuação é atualizada.

    Retorna:
    Startup: Objeto da startup vencedora.

    Observações:
    - A função altera o atributo `point` diretamente nas startups.
    - Utiliza o módulo `random` para desempate em caso de pontuação igual.
    """
    if startup1.point > startup2.point:
        startup1.point += 30
        print(f"{startup1.nome} venceu a batalha e ganhou 30 pontos!")
        vencedor = startup1
    else:
        startup2.point += 30
        print(f"{startup2.nome} venceu a batalha e ganhou 30 pontos!")
        vencedor = startup2
    # Shark fight
    if startup1.point == startup2.point:
        vencedor = random.choice([startup1, startup2])
        vencedor.point += 32
    return vencedor


def relatorio_final(lista_startups):
    """
    Gera e exibe o relatório final da competição entre startups.

    Parâmetros:
    lista_startups (list): Lista com todas as startups que participaram da competição.

    Comportamento:
    - Verifica se há dados disponíveis para o relatório.
    - Conta quantas vezes cada evento foi aplicado em cada startup.
    - Cria um DataFrame com nome, pontuação final, eventos aplicados e estatísticas de cada evento.
    - Ordena o ranking pela pontuação final (decrescente) e exibe na tela.
    - Exibe o nome e o slogan da startup campeã.

    Observações:
    - Atributos esperados em cada startup:
        - `nome`: nome da startup.
        - `point`: pontuação final da startup.
        - `eventos_aplicados`: lista com os IDs dos eventos aplicados.
        - `slogan`: slogan da startup (usado apenas para a campeã).
    """
    if not lista_startups:
        print("Nenhum dado disponível para gerar o relatório final.")
        return

    nomes_eventos = menus_dic.nomes_eventos
    colunas_eventos = list(nomes_eventos.values())

    dados = []

    for startup in lista_startups:
        # Contagem dos eventos
        contagem_eventos = {nome: 0 for nome in colunas_eventos}

        for id_evento in startup.eventos_aplicados:
            nome_evento = nomes_eventos.get(id_evento)
            if nome_evento:
                contagem_eventos[nome_evento] += 1

        eventos_str = ", ".join(str(e) for e in startup.eventos_aplicados)

        linha = {
            "Nome": startup.nome,
            "Pontuação Final": startup.point,
            "Eventos Aplicados": eventos_str
        }

        linha.update(contagem_eventos)
        dados.append(linha)

    colunas_finais = ["Nome", "Pontuação Final",
                      "Eventos Aplicados"] + colunas_eventos
    df = pd.DataFrame(dados, columns=colunas_finais)
    df = df.sort_values(by="Pontuação Final", ascending=False)

    print("\nRelatório Final - Ranking das Startups:")
    print('')
    print(df.to_string(index=False))

    campeao_nome = df.iloc[0]["Nome"]
    campeao_obj = next(
        (s for s in lista_startups if s.nome == campeao_nome), None)

    print(f"\nStartup Campeã: {campeao_nome}")
    if campeao_obj:
        print(f"Slogan: {campeao_obj.slogan}")
    else:
        print("Slogan: [Slogan não encontrado]")
    


def placar_atual(fase_batalha: list, vencedores: list):
    """
    Exibe o placar atual das startups que ainda estão na competição.

    Parâmetros:
    fase_batalha (list): Lista de batalhas da fase atual, onde cada item é uma lista/tupla com duas startups.
    vencedores (list): Lista de startups que já venceram suas batalhas nesta rodada.

    Comportamento:
    - Junta todas as startups ainda ativas na rodada (as que estão em batalha e as que já venceram).
    - Cria um DataFrame com o nome e a pontuação atual de cada uma.
    - Exibe esse placar na tela em formato de tabela.

    Observações:
    - A função é apenas informativa, não altera o estado do jogo.
    - Utiliza o módulo `pandas` para montar e imprimir a tabela.
    """
    startups_ativas = []
    for par in fase_batalha:
        startups_ativas.extend(par)
    startups_ativas.extend(vencedores)

    dados = [[startup.nome, startup.point] for startup in startups_ativas]
    df_status = pd.DataFrame(dados, columns=["Nome", "Pontuação"])

    print("Placar Atual dos Competidores:")
    print(df_status.to_string(index=False))


def config(lista_geral: list):
    """
    Exibe o menu de configurações e permite modificar atributos de uma startup.

    Parâmetros:
    lista_geral (list): Lista de startups disponíveis para configuração.

    Comportamento:
    - Exibe uma lista de startups e permite ao usuário escolher qual deseja configurar.
    - Apresenta um menu de opções para modificar atributos da startup selecionada:
        1. Nome
        2. Pontuação
        3. Ano de fundação
        4. Slogan
    - O usuário pode alterar um ou mais desses atributos, e as mudanças são aplicadas diretamente na startup.

    Observações:
    - Se o usuário escolher uma opção inválida ou inserir um valor incorreto, a função exibirá uma mensagem de erro e retornará ao menu.
    """
    limpar_terminal()
    print("--- Menu de Configurações ---")
    for i, startup in enumerate(lista_geral):
        print(f"{i} - {startup.nome}")

    try:
        escolha_startup = int(
            input("Digite o número da startup que deseja configurar: "))
        if 0 <= escolha_startup < len(lista_geral):
            startup = lista_geral[escolha_startup]
        else:
            print("Escolha inválida!")
            return
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
        return

    print(menus_dic.menu_config())

    try:
        escolha_atributo = int(
            input("Digite o número do atributo que deseja modificar: "))

        if escolha_atributo == 1:
            novo_nome = input("Digite o novo nome: ")
            startup.nome = novo_nome
            print(f"Nome alterado para: {startup.nome}")

        elif escolha_atributo == 2:
            nova_pontuacao = int(input("Digite a nova pontuação: "))
            startup.pontuacao = nova_pontuacao
            print(f"Pontuação alterada para: {startup.pontuacao}")

        elif escolha_atributo == 3:
            novo_ano_fundacao = input("Digite o novo ano de fundação: ")
            startup.ano_fundacao = novo_ano_fundacao
            print(f"Ano de fundação alterado para: {startup.ano_fundacao}")

        elif escolha_atributo == 4:
            novo_slogan = input("Digite o novo slogan: ")
            startup.slogan = novo_slogan
            print(f"Slogan alterado para: {startup.slogan}")

        else:
            print("Opção inválida!")
            return

    except ValueError:
        print("Entrada inválida. Digite um número válido.")
