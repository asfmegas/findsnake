__author__ = 'asfmgas.github.io'

"""
Objetivo do jogo é descobrir as combras escondidas no campo
Por: Alexsandro Façanha
ano: 07/2017
"""

import snake, camp, player
from constants import *
import time
import pdb

count = 0


def main():
	global count
	print(FRAME[0])
	# time.sleep(TIME)

	my_camp = camp.Camp()

	while True:
		new_snake = snake.Snake()
		i = new_snake.get_orientation()
		if my_camp.add_snake_camp(new_snake.get_snake(my_camp.set_position(i))):
			count += 1
		if count == 5:
			break

	# my_camp.get_snakes()
	# print(my_camp.get_total_positions())

	player_one = player.Player()
	my_camp.create_camp(0)
	while True:
		if player_one.get_total_errors() < MIDDLE_MODE:

			# player_one.hit() -> True|False 
			# Retorna um False ou um número(True). Se False ele sair do while
			to_return = player_one.hit()
			if to_return:
				my_camp.create_camp(to_return)
				print(' Você possui {} possíveis erros.'.format(my_camp.get_total_positions()))
				player_one.errors = my_camp.get_errors()
				player_one.get_info()

				if player_one.get_hits == 25:
					print(FRAME[2])
					print('As posições das cobras eram essas:')
					my_camp.get_snakes()
					break

			else:
				break
		else:
			print(FRAME[1])
			print('As posições das cobras eram essas:')
			my_camp.get_snakes()
			break


if __name__ == '__main__':
	main()