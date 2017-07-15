__author__ = 'asfmgas.github.io'

ALIVE = True
DEAD = False
HORIZONTAL = 1
VERTICAL = 2
SNAKE_SIZE = 5

EASY_MODE = 25
MIDDLE_MODE = 20
HARD_MODE = 15

HIT_VALUE = 1
ERROR_VALUE = 0

TIME = 5

FRAME = [
"""
####################################################################

\tEncontre as cobras

\tEm um campo com 100 posições existem 5 cobras escondidas.
\tCada cobra oculpa 5 posições. Cabe a você encontrar essas
\tposições antes que suas tentativas terminem.


\tobs.: Você pode sair a qualquer momento, basta digitar "s"

####################################################################
""",
"""
#################################################

	Que pena, suas tentativas acabaram.

		    Gamer Over


#################################################
""",
"""
#################################################

	Parabéns você encontrou todas as cobras

		      Winner


#################################################
""",
"""
	Você errou :-(
""",
"""
	Parabéns! Você acertou!!!
"""]

