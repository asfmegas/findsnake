__author__ = 'asfmgas.github.io'

import random
import pdb
from constants import *


class Snake(object):
	def __init__(self):
		# self.life = ALIVE
		self.pos_inital = 0
		self.body = []
		self.orientation = 0
		self.__define_orientation()

	# Define a orientação que a cobra terá (horizontal ou vertical)
	def __define_orientation(self):
		self.orientation = random.randint(1, 2)

	def get_orientation(self):
		return self.orientation

	# Retorna a cobra
	def get_snake(self, value):
		self.pos_inital = value
		if self.orientation == HORIZONTAL:
			self.body = [i for i in range(self.pos_inital, self.pos_inital + SNAKE_SIZE)]
		else:
			self.body = [i for i in range(self.pos_inital, self.pos_inital + SNAKE_SIZE * 10, 10)]
		return self.body

