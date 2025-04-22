import pandas as pd
from Startups import Startups
import batalha
import menus_dic
n_competidores = 0


def cadastro():
    batalha.limpar_terminal()
    global n_competidores
    print("Seja Bem Vindo(a), cadastre as Startups competidoras aqui!!!")
    print(menus_dic.menu_quantidade_startups())
    while True:
        n_competidores = str(input("Selecione quantas Startups participarão do Torneio: "))
        if not n_competidores:
            print("Nenhuma entrada detectada. Por favor, digite um número.")
            continue
        if n_competidores in '468':
            n_competidores = int(n_competidores)
            break
        else:
            print("Numero Invalido Tente Novamente.")  # ad. Tratamento de erro


def criar_startups():
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
