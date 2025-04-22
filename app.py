import cadastro
from Startups import Startups
import batalha as bt
import menus_dic

big_list = bt.startups

print("Torneio de Startups")
print("")
cadastro.cadastro()
cadastro.criar_startups()
bt.iniciar_competicao(big_list)
