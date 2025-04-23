# Torneio de Startups

Bem-vindo ao **Torneio de Startups**, um sistema de Torneios entre Startups desenvolvido em Python. Aqui, cada startup é avaliada por seu desempenho simulado em Eventos, competindo em fases eliminatórias até restar apenas uma campeã.

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
## Clonar o repositório
```bash
git clone https://github.com/Joao-H-Luz/Corrida-de-Startups.git
```

## Criar Ambiente Virtual
- Windows
```bash
Python -m venv venv
```
Ativar o ambiente no CMD:
```bash
venv\Scripts\activate
```

- Linux/Mac
```bash
python3 -m venv venv
```
Ativar o ambiente Linux/Mac
```bash
source venv/bin/activate
```

## Requisitos

- Python **3.10** ou superior
- Biblioteca: [`pandas==2.2.3`]

Para instalar os requisitos:

```bash
pip install -r requirements.txt
```

## Executar o programa
```bash
python app.py
```

---

## Etapas do Torneio:

# 1. Cadastro de Startups

O cadastro funciona em um formato simples, dividido em duas partes. 

A primeira parte é uma verificação de quantas Startups serão criadas de acordo com o padrão a seguir: 4 a 8 sendo par - (4, 6 ou 8) - é realizado um looping e uma verificação de numero(str) e depois convertido para (int) essa variável é "n_competidores".

A segunda parte é o Cadastro em si onde um "for" ira rodar com a quantidade certa de startups a serem criadas, elas terão as seguintes entradas: Nome(str), Ano de Fundação(int) e Slogan(str) - terá também a pontuação, mas ela é iniciada com 70 por padrão.
Ao final de cada laço, é criado um objeto da "class Startups" e adicionado a uma lista global de todas as startups criadas - "startups = [ ]".

# 2. Batalhas

A Batalha é o coração do código onde toda a sequencia do torneio é encadeada e assim deixando com que seja automatizado todas as etapas apos o cadastro.

Aqui por exemplo esta a função "iniciar_competicao" ela é a responsável pelo Avanço automático de faze. A sua logica funciona com base em um laço de que verifica se o numero de startups em uma lista copia da ("startups = [ ]") é 1. Enquanto o requisito não for alcançado ela aciona uma sequencia de função responsáveis por:
- Sortear o par de Startups para a Batalha
- Gerenciar o menu da Batalha e suas funções auxiliares
- Gerenciar todas as listas presentes no código para a manutenção dos itens e garantia que o andamento do código ficara fluido ate a etapa final.

## 2.1 Sortear startups

A função "sorteio_de_batalha", é chamada em todo inicio de uma nova rodada, para esta função ela sempre recebe uma (lista simples) e retorna uma (lista de listas) ou uma sub-list.
O sorteio inicia com uma verificação, se o numero de objetos na lista é par ou impar. Por padrão a primeira verificação - (Primeira Rodada) - sempre será par, por causa do cadastro que obriga a sempre cadastrar pares. 

Caso ocorra de terem números impares na lista: 
- Ex: Iniciou o Torneio com 6 startups, a função "sorteio_de_batalha" retorna 3 batalhas, e destas retorno 3 vencedores, mas agora temos um numero impar de vencedores.

Neste caso o programa seleciona de maneira aleatória um objeto para "pular de fase", restando um numero par de objetos para o sorteio e ao final o vencedor disputa com a Startup que havia pulado de fase.

## 2.2 Gerenciar Batalha

O Gerenciador de Batalha em si é o coração do projeto, ele traz a parte gráfica de menus para auxiliar o usuário na manutenção e elaboração das batalhas.
A principal função do "gerenciador_de_batalha" é exibir o menu e controlar os inputs do sistema quando o torneio estiver em andamento. Nele tu pode acessar:

- "99" Mostra o Placar do Torneio em tempo real
- "00" Abre e gerencia outro menu de configurações
- "s" Sai imediatamente do Torneio  retornando direto o Relatório final com o campeão sendo a startup com maior pontuação até o momento.

Além de gerenciar outras funções como:
- "batalha" que é um sub menu dos Eventos
- "verificar_vencedor" que verifica qual é a startup vencedora da quela batalha.

## 2.2.1 Batalha

A função Batalha gerencia um sub menu que comanda as chamadas de função interna da class Startup, utilizando de menus e dicionários para selecionar a startup e o evento/função, a qual ela ira chamar.

Ex:
"1: Startups.pitch_convincente"
"2: Startups.produto_com_bugs"
"3: Startups.boa_tração_de_usuários"

## 2.2.2 Verificação de vencedor

A função "verificar_vencedor" é bem simples, ela compara com uma sequencia de "if/else" para ver qual das duas Startups na batalha ficou com a maior pontuação no final, o vencedor ganha "30 pontos".

Se ao final da seleção de eventos os dois objetos estiverem com a mesma pontuação será realizada o "Shark fight" onde será escolhida aleatoriamente uma das duas para ser a vencedora e ela ganhara "32 pontos".

## 2.3 Funções Auxiliares/Feature Extra

As Features Extras são duas funções para melhorar a dinâmica do Torneio.

A primeira é um placar dinâmico implementado com pandas e df para criar uma tabela temporária somente com as startups ativas na batalha, ou seja as que não foram eliminadas ainda.

A segunda Feature é um sub menu "config", nele tu pode gerenciar qual startup tu deseja selecionar e qual alteração de atributo tu deseja fazer. E possível alterar Nome, Ano de Fundação, Slogan e Pontuação de qualquer Startup em qualquer ponto do jogo antes de tu começar uma batalha.


# 3. Eventos

A logica seguida por traz dos eventos foi unir as funções na class Startup e utilizar um dicionário com a chave sendo um numero e o valor a chamada de função, assim toda vez que tu entrar na função "batalha" e selecionar o numero do Evento que deseja, ele por traz dos panos ira verificar se o numero digitado é referente a alguma chave do dicionário e se for ele chama a função passando como paramento a startup que já foi selecionada pela função "batalha".


# 4. Relatório Final

O Relatório Final é um pouco mais complexo, dividido em duas partes.
A primeira parte é responsável por gerar um DataFrame temporário que lista todas as Startups cadastradas - (Input: "startups = [ ]" ) - diferente das Features essa tabela mostra além dos nomes e pontuação, quais os eventos foram aplicados a essa Sturtup e uma coluna para cada evento mostrando a quantidade por completo dos Eventos. O Ranking é ordenado pelo valor da pontuação do maior para o menor.

A segunda parte e responsável por buscar na lista principal a Startup vencedora e buscar o nome e o Slogan que são mostrados logo abaixo da tabela - (Input: "startups = [ ]" ).