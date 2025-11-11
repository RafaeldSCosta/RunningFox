# pygame-lihura
# pygame-lihura
NTEGRANTES DO GRUPO:

Julia Mendes, Livia Pinheiro e Rafael dos Santos

LINK PARA VÍDEO NO YOUTUBE:

O vídeo demonstra o funcionamento do jogo. Link: 

SOBRE O JOGO:

Running Fox é um jogo do gênero "crossy road" onde você controla uma raposa que deve fugir de vários inimigos. O objetivo é pegar os ovos no celeiro no menor tempo possível.

COMO JOGAR:
↑ :mover-se para frente (único movimento que emite som).
← →:movimentação lateral.
Pressione R para reiniciar a fase.
Pressione Q para sair para o menu.

MECÂNICA PRINCIPAL:
Evite colisões e tente terminar com todas as vidas para vencer a fase.

A raposa deve atravessar a fase desviando de obstáculos e inimigos.

O jogo é sincronizado com uma trilha sonora, criando ritmo e imersão.

A cada fase, a dificuldade e a velocidade aumentam.

Se perder todas as vidas → Game Over.

Ao alcançar os ovos no final → Vitória e entrada no ranking.

ESTRUTURA DE CÓDIGO:

main.py — script principal do jogo.
Inicializa o Pygame, define o tamanho da janela e a taxa de FPS, carrega sons, imagens e controla a lógica principal do jogo.
Gerencia os estados (menu, jogo, end), as transições entre telas, o tempo de jogo, o som de movimento da raposa e o sistema de fases e ranking.

screens.py — módulo responsável pelas telas (menus) e gerenciamento de estados.
Contém as seguintes classes:

    BaseScreen: classe base com funções comuns de desenho e carregamento de imagens.

    Start: tela inicial com logo, botão de início e animação de nuvens.

    Level: tela de transição entre fases, exibindo a imagem da fase atual.

    End: tela final de game over ou vitória, com opções de reiniciar (R) ou sair (Q).

    GameStateManager: gerencia o estado atual do jogo (menu, fase, fim) e permite alternar entre eles.

classes/game.py — define a classe principal CruzamentoFazenda.
Responsável por toda a lógica da gameplay: movimentação da raposa, checagem de colisões, controle de vidas, fases, e detecção de vitória ou derrota.

classes/hud.py — gerencia a interface (HUD).
Exibe na tela as vidas restantes do jogador e o cronômetro do tempo durante a partida.

ranking.py — controla o sistema de pontuação e ranking.
Carrega e salva os tempos no arquivo scores.json, ordenando os melhores resultados.
Inclui funções para:

    add_score(): adiciona um novo tempo.

    text_input_screen(): permite que o jogador insira seu nome após vencer.

    show_ranking_screen(): exibe o ranking na tela com fundo personalizado e opções para reiniciar (R) ou sair (Q).
    scores.json — arquivo JSON que armazena os nomes e tempos dos melhores jogadores (ordenados por menor tempo).

sons/ — pasta com todos os efeitos sonoros e trilhas:
    trilha.mp3: música de fundo contínua.

    raposa.mp3: som de movimento (tocado apenas ao andar para frente).

    start.mp3: som do início do jogo.

    fases.mp3: som de troca de fase.

    game_over.mp3: som de derrota.

imagens_pygame/ — contém todas as imagens e telas visuais:
    instru.png: tela de instruções (20 segundos, pode ser pulada com espaço).

    level_1.png, level_2.png: imagens de fase.

    win.png, game_over.png: telas finais de vitória e derrota.

    ranking.png: fundo para o ranking.

    titulo.png, botao_start.png: elementos visuais do menu inicial.