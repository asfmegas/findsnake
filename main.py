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
list_snakes = []
list_snakes_hits = [[],[],[],[],[]]

def main():
	global count
	print(FRAME[0])
	time.sleep(TIME)

	my_camp = camp.Camp()

	while True:
		new_snake = snake.Snake()
		i = new_snake.get_orientation()
		s = new_snake.get_snake(my_camp.set_position(i))
		if my_camp.add_snake_camp(s):
			list_snakes.append(s)
			count += 1
		if count == 5:
			break


	player_one = player.Player()
	my_camp.create_camp(0)
	while True:
		if player_one.get_total_errors() < MIDDLE_MODE:

			# player_one.hit() -> True|False 
			# Retorna um False ou um número(True). Se False ele sair do while
			to_return = player_one.hit()
			if to_return:
				my_camp.create_camp(to_return)
				player_one.errors = my_camp.get_errors()
				player_one.get_info()

				hits_player(to_return)


				if player_one.get_hits() == my_camp.get_total_positions():
					print(FRAME[2])
					time.sleep(2)
					print('As posições das cobras eram essas:')
					for i in range(len(list_snakes)):
						print('Cobra {0} : {1} -> Acertos: {2}\n'.format(i, list_snakes[i], list_snakes_hits[i]))
					break

			else:
				break
		else:
			print(FRAME[1])
			time.sleep(2)
			print('As posições das cobras eram essas:')
			for i in range(len(list_snakes)):
				print('Cobra {0} : {1} -> Acertos: {2}\n'.format(i, list_snakes[i], list_snakes_hits[i]))
			break


def hits_player(value):
	for i in range(len(list_snakes)):
		for item in list_snakes[i]:
			if value in list_snakes[i]:
				list_snakes_hits[i].append(value)
				break


if __name__ == '__main__':
	main()