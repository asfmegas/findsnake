__author__ = 'asfmgas.github.io'

import random
from constants import *
import pdb

class Camp(object):
	def __init__(self):
		# Guarda as cobras de de forma separadas
		self.group_snakes = []
		# Guarda as posições das cobras no campo
		self.position = []
		# Gera o campo em uma lista de inteiros em sequência de 1 a 100
		self.camp_snake = [i for i in range(1, 101)]
		self.errors = 0
		self.error = 0

	def get_snakes(self):
		for i in range(len(self.group_snakes)):
			print(self.group_snakes[i])

	# Adiciona a cobra no campo
	def add_snake_camp(self, snake):
		for pos in snake:
			if pos in self.position:
				return False

		self.group_snakes.append(snake)
		for i in snake:
			self.position.append(i)
		return True

	# Altera o campo definindo se o jogador acertou ou errou
	def change_position(self, pos, item):
		self.camp_snake.insert(pos, item)
		self.camp_snake.remove(pos)

	# Cria o campo
	def create_camp(self, shoot):
		print('#' * 75)
		print()
		count = 0 # contador para quebra de linha

		for pos in self.camp_snake:
			if pos == shoot:
				if shoot in self.position:
					print('{0:6d}'.format(1), end=' ')
					self.change_position(pos, HIT_VALUE)
					self.error = 1
				else:
					print('{0:6d}'.format(0), end=' ')
					self.change_position(pos, ERROR_VALUE)
					self.error = 0
					self.errors += 1

				# Se a tentativa for 1 então verificar apenas uma vez para não zerar os acertos
				if shoot == 1:
					shoot = 101
			else:
				print('{0:6d}'.format(pos), end=' ')
			
			# Quebra de linha do campo
			count += 1
			if count == 10:
				print()
				print()
				count = 0
			
		print('#' * 75)

		if self.error == 1:
			print(FRAME[4])
		else:
			if shoot != 0:
				print(FRAME[3])


	def get_errors(self):
		return self.errors

	def get_total_positions(self):
		return len(set(self.position))

	# Retorna um valor válido para iniciar as posições da cobra
	def set_position(self, value):
		while True:
			inicio = random.randint(1, 101)
			if value == HORIZONTAL:
				if (inicio < 7) or \
					(inicio > 10 and inicio < 17) or \
					(inicio > 20 and inicio < 27) or \
					(inicio > 29 and inicio < 37) or \
					(inicio > 40 and inicio < 47) or \
					(inicio > 50 and inicio < 57) or \
					(inicio > 60 and inicio < 67) or \
					(inicio > 70 and inicio < 77) or \
					(inicio > 80 and inicio < 87) or \
					(inicio > 90 and inicio < 97):
					return inicio
			else:
				if inicio >= 1 and inicio < 60:
					return inicio