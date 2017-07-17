__author__ = 'asfmgas.github.io'

import mydebugging
from mydebugging import *

log = mydebugging.MyDebug()
log.getLogDebug()
log.desabilitar()

"""
	Sempre o primeiro acerto valerá 10.0.
	Acertos em sequência valerão a última pontuação mais 1
	ou seja, 
	1o acerto vale 10.0
	2o acerto consecutivo valerá 11.0
	3o acerto consercutivo valerá 12.0
	e assim por diante. Se na 4o tentativa for um erro, o 
	próximo acerto valerá apenas 10.0 novamente.

	Para os erros será despontado 1 e crescente assim como os acertos.

	Se o jogador vencer será acrescido mais 10 pontos no final.
	Se o jogador perder será retirados 5 pontos do total.


	No final, o jogador não poderá ter pontuação negativa. Ou seja, caso o jogador
	termine o jogo com uma pontuação negativa será conventida em 0.

"""


class Scores(object):
	def __init__(self):
		self.point_hit = 10
		self.point_error = 1
		self.score_hit = 0
		self.score_error = 0
		self.score_total = 0

	def get_total(self):
		return self.score_total

	def guess_hit(self):
		log.comparador(self.score_total, self.score_hit, 'score_total', 'score_hit')
		self.score_total += (self.point_hit + self.score_hit)
		self.score_hit += 1
		self.score_error = 0

	def guess_error(self):
		log.comparador(self.score_total, self.score_error, 'score_total', 'score_error')
		self.score_total -= (self.point_error + self.score_error)
		self.score_error += 1
		self.score_hit = 0

	def loser(self):
		if self.score_total < 0:
			self.score_total = 0
		else:
			self.score_total -= 5

	def winner(self):
		if self.score_total + 10 < 0:
			self.score_total = 0
		else:
			self.score_total += 10