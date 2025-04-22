
class Startups:
    """ 
    Classe que representa uma startup no jogo de competição.
    Atributos:
    - nome (str): Nome da startup.
    - fundacao (str): Ano de fundação da startup.
    - slogan (str): Slogan da startup.
    - point (int): Pontuação atual da startup.
    - eventos_aplicados (list): Lista de eventos aplicados à startup.
    """
    round_atual = 0

    def __init__(self, nome:str, fundacao:int, slogan:str, point:int):
        self.nome = nome
        self.fundacao = fundacao
        self.slogan = slogan
        self.point = int(point)
        self.eventos_aplicados = []

    def __str__(self):
        """Retorna uma string com o nome e a pontuação da startup."""
        return (f"Nome: {self.nome} || Pontuação: {self.point}")

    def pitch_convincente(self):  # Evento 1
        self.point += 6

    def produto_com_bugs(self):  # Evento 2
        self.point -= 4

    def boa_tração_de_usuários(self):  # Evento 3
        self.point += 3

    def investidor_irritado(self):  # Evento 4
        self.point -= 6

    def fake_news_no_pitch(self):  # Evento 5
        self.point -= 8
