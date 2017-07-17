__author__ = 'asfmgas.github.io'

# para debug
import pdb
from constants import *

class Player(object):
	def __init__(self):
		self.hits = 0
		self.shoots = 0
		self.attemps = []
		self.errors = 0

	def hit(self):
		while True:
			try:
				value = input('Digite uma posição: ')
				if value == 's':
					return False
				else:
					value = int(value)
			except:
				print('\n Digite apenas números entre 1 a 100.\n')
				continue

			if value in list(range(1, 101)) and value not in self.attemps and value != 0:
				self.attemps.append(value)
				self.shoots += 1
				return value

	def get_total_errors(self):
		return self.errors

	def get_attempts(self):
		return self.get_attempts

	def get_data(self):
		return self.shoots, len(self.attemps)

	def get_info(self):
		self.hits = self.shoots - self.errors
		print('  Shoots[ {0} ]  Hits[ {1} ]  Errors[ {2} ]'.format(self.shoots, self.hits, self.errors))
		print('-' * WIDTH)

	def get_hits(self):
		self.hits = self.shoots - self.errors
		return self.hits