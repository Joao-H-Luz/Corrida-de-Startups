from Startups import Startups

# Menus do Projeto
def menu_quantidade_startups():
    return """
==== Menu de Cadastro ====
[4] - Startups
[6] - Startups
[8] - Startups
==========================
"""


def menu_eventos():
    return """
========   MENU DE EVENTOS   ========
[1] - Pitch_convincente (+6)
[2] - Produto_com_bugs (-4)
[3] - Boa_tração_de_usuários (+3)
[4] - Investidor_irritado (-6)
[5] - Fake_news_no_pitch (-8) 
=====================================
"""


def menu_config():
    return """
    --- Escolha o que deseja modificar ---

    [1] - Nome
    [2] - Pontuação
    [3] - Ano de Fundação
    [4] - Slogan 
    """


# Dicionários do Projeto
eventos = {1: Startups.pitch_convincente,
           2: Startups.produto_com_bugs,
           3: Startups.boa_tração_de_usuários,
           4: Startups.investidor_irritado,
           5: Startups.fake_news_no_pitch}


nomes_eventos = {1: "Pitch Convincente (+6)",
                 2: "Produto com Bugs (-4)",
                 3: "Boa Tração de Usuários (+3)",
                 4: "Investidor Irritado (-6)",
                 5: "Fake News no Pitch (-8)"}
