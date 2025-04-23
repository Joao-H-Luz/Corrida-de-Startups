import pandas as pd
from Startups import Startups
import batalha
import menus_dic
n_competidores = 0


def cadastro():
    """
    Realiza o cadastro das startups competidoras no torneio.

    Comportamento:
    - Exibe uma mensagem de boas-vindas e um menu para o usuário selecionar a quantidade de startups que irão competir.
    - O usuário deve inserir um número válido (4, 6 ou 8) para determinar quantas startups participarão.
    - O número selecionado é validado antes de prosseguir.

    Observações:
    - A função usa a variável global `n_competidores` para armazenar a quantidade de startups a serem cadastradas.
    - Se o usuário inserir um valor inválido ou vazio, será solicitado que ele tente novamente.
    """
    batalha.limpar_terminal()
    global n_competidores
    print("Seja Bem Vindo(a), cadastre as Startups competidoras aqui!!!")
    print(menus_dic.menu_quantidade_startups())
    while True:
        n_competidores = str(
            input("Selecione quantas Startups participarão do Torneio: "))
        if not n_competidores:
            print("Nenhuma entrada detectada. Por favor, digite um número.")
            continue
        if n_competidores in '468':
            n_competidores = int(n_competidores)
            break
        else:
            print("Numero Invalido Tente Novamente.")


def criar_startups():
    """
    Cria as startups para o torneio, solicitando informações ao usuário.

    Comportamento:
    - Exibe uma mensagem de boas-vindas para a criação das startups.
    - Para cada startup, solicita ao usuário o nome, o ano de fundação e o slogan.
    - O ano de fundação é validado para garantir que o usuário insira um número válido.
    - As startups criadas são adicionadas à lista global `startups`.

    Observações:
    - A função utiliza a variável global `n_competidores` para determinar quantas startups serão criadas.
    - Para cada startup, é criada uma instância da classe `Startups`, com os atributos `nome`, `fundacao`, `slogan` e uma pontuação inicial de 70.
    - Caso o usuário insira um valor inválido para o ano de fundação, será solicitado que ele tente novamente até que um valor válido seja fornecido.
    """
    batalha.limpar_terminal()
    global n_competidores
    print("Vamos criar as Startups!!!")
    for i in range(0, n_competidores):
        nome = input(f"Digite o Nome da {i}°: ")
        while True:
            fundacao_str = input("Digite o ano de Fundação: ").strip()
            if not fundacao_str:
                print("Você não digitou nada! Tente novamente.")
                continue
            try:
                fundacao = int(fundacao_str)
                break
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
        slogan = input("Digite  o Slogan da Satartup: ")
        batalha.startups.append(Startups(nome, fundacao, slogan, 70))
