__author__ = 'asfmgas.github.io'

ALIVE = True
DEAD = False
HORIZONTAL = 1
VERTICAL = 2
SNAKE_SIZE = 5

EASY_MODE = 22
NORMAL_MODE = 20
HARD_MODE = 15

HIT_VALUE = 1
ERROR_VALUE = 0

TIME = 5

WIDTH = 75
HEIGHT = 0

EASY = 8
NORMAL = 5
HARD = 3




FRAME = [
"""
#######################################################################################

	Encontre as cobras

	O objetivo do jogo é encontrar as "cobras" que estão escondidas no campo.
	Elas possuem 5 posições e podem está na horizontal ou na vertical. O "campo"
	que possui 100 posições entre 1 e 100. O acerto corresponde a 10 e o erro 
	corresponde a -1 ponto. A quantidade de "cobras", assim como os possíveis 
	erros, variam de acordo com o modo que foi definido.

	obs.: Você pode sair a qualquer momento, basta digitar "s"

#######################################################################################
""",
"""
#######################################################################################

\t\t\tQue pena, suas tentativas acabaram.

\t\t\t\tGamer Over

#######################################################################################
""",
"""
#######################################################################################

\t\t\tParabéns você encontrou todas as cobras

\t\t\t\tWinner

#######################################################################################
""",
"""
	Você errou :-(
""",
"""
	Parabéns! Você acertou!!!
""",
"""
	Sobre os modos do jogo

	No EASY o jogador possui 22 possíveis erros e precisará encontrar 8 "cobras".
	No NORMAL o jogador possui 20 possível erros e encontrará 5 "cobras".
	No HARD o jogador terá 15 possíveis erros e encontrará apenas 3 "cobras".

#######################################################################################
"""]


