import pandas as pd
import random
import menus_dic
import os
import time
from openpyxl import load_workbook
startups = []
fase_batalha = []
vencedores = []
rodada = 0


def iniciar_competicao(startups: list):
    """
    - Inicia a competição entre as startups.
    - Faz as rodadas de batalha até sobrar só uma vencedora.
    - Mostra o relatório final no fim da competição.
    Parâmetros:
    - startups: lista com todas as startups participantes.
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
    - Gerencia as batalhas da rodada.
    - Mostra as batalhas disponíveis e deixa o usuário escolher qual quer iniciar.
    - Também dá opção de ver o placar, abrir configurações ou sair do gerenciador.
    Parâmetros:
    - lista_geral: lista com pares de startups que vão batalhar.
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
    - Roda uma batalha entre duas startups.
    - Permite aplicar eventos em cada uma e decide quem venceu.
    Parâmetros:
    - sub_list: lista com duas startups que vão batalhar.
    Retorna:
    - A startup vencedora.
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
    Limpa o terminal, funciona em Windows, Linux e Mac.
    """
    sistema = os.name
    if sistema == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux/MacOS
        os.system('clear')


def delay():
    """Função que faz uma pausa de 1 a 2 segundos para apresentar os menus de forma mais fluída."""
    time.sleep(random.uniform(1, 2))  # Delay aleatório entre 1 e 2 segundos


def sorteio_de_batalha(lista_geral: list):
    """
    Sorteia as batalhas e coloca uma startup automaticamente na próxima fase se o número de participantes for ímpar.
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
    Compara as pontuações das startups e retorna a vencedora.
    Em caso de empate, aplica o Shark fight.
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
    Gera o relatório final, mostrando o ranking das startups e seus eventos aplicados.
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
    delay()


def placar_atual(fase_batalha: list, vencedores: list):
    """
    FEATURE EXTRA - 1
    Exibe o placar atual das startups após as batalhas.
    Combina as startups da fase atual com os vencedores e exibe uma tabela.
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
    FEATURE EXTRA - 2
    - Permite modificar os atributos de uma startup selecionada.
    Parâmetros:
    lista_geral (list): Lista de startups disponíveis para configuração.

    O usuário pode alterar:
    - Nome
    - Pontuação
    - Ano de fundação
    - Slogan
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
    delay()
