# Torneio de Startups

Bem-vindo ao **Torneio de Startups**, um sistema de Torneios entre Startups desenvolvido em Python. Aqui, cada startup é avaliada por seu desempenho em eventos positivos ou negativos, competindo em fases eliminatórias até restar apenas uma campeã.

---

## Lista de Funcionalidades

- Seleção do número de participantes (4, 6 ou 8).
- Cadastro interativo de startups (nome, ano de fundação e slogan).
- Batalhas por rodada com seleção (Rounds).
- Eventos atribuídos manualmente conforme o desempenho simulado de cada startup.
- Relatório final com ranking, estatísticas e o slogan da startup campeã
- Interface em terminal com menus simples e objetivos

-- Features:
- Menu de configurações para alterar nome, pontuação, ano ou slogan
- Placar em tempo real da competição.

---

## Requisitos

- Python **3.10** ou superior
- Biblioteca: [`pandas==2.2.3`]

Para instalar os requisitos:

```bash
pip install -r requirements.txt
```

## Clonar o repositório
git clone https://github.com/teu_usuario/nome-do-repositorio.git
cd nome-do-repositorio

## Executar o programa
python app.py

---

## Etapas do Torneio:

# 1. Cadastro de Startups

O cadastro funciona em um formato simples, dividido em duas partes. 

A primeira parte é uma verificação de quantas Startups serão criadas de acordo com o padrao a seguir: 4 a 8 sendo par - (4, 6 ou 8) - é realizado um loping e uma verificação de numero(str) e depois convertido para (int) essa variavel é "n_competidores".

A segunda parte é o Cadastro em si onde um "for" ira rodar com a quantidade certa de startups a serem criadas, elas terão as seguntes entradas: Nome(str), Ano de Fundação(int) e Slogan(str) - tera tambem a pontuação, mas ela é iniciada com 70 por padrão.
Ao final de cada laço, é criado um objeto da "class Startups" e adicionado a uma lista global de todas as startups criadas - "startups = []" -.

# 2. Batalhas

As startups são organizadas em pares.

Usuário aplica eventos a cada uma: positivos ou negativos.

Eventos

Exemplos:

Pitch Convincente (+6)

Produto com Bugs (-4)

Fake News no Pitch (-8)

Eliminação

A startup com maior pontuação vence a batalha.

Empates são resolvidos com sorteio (“Shark Fight”).

Relatório Final

Exibe ranking final, estatísticas de eventos e o slogan da campeã.