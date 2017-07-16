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
import scores, database

db = database.Database()
db.createTable()

lista = db.getList()
ID = 0
print('-' * 70)
print('\t\tR A N K I N G - Os 10 melhores\n')

my_list = []
for linha in lista:
	my_list.append((linha[1], linha[2], linha[3]))

for linha in my_list:
	ID += 1
	print('\t{0}o. Acertos: {1}, Erros: {2}, Tentativas: {3}, Pontuação: {4}'.format(ID, linha[2], linha[1] - linha[2], linha[1], linha[0]))
	if ID == 11:
		break

print('-' * 70)
time.sleep(TIME)

count = 0
list_snakes = []
list_snakes_hits = [[],[],[],[],[]]

def main():
	global count, ID

	# Informações para o início do jogo.
	# print(FRAME[0])
	# time.sleep(TIME)
	score = scores.Scores()

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
	count = 0

	player_one = player.Player()
	my_camp.create_camp(0)

	# Rode enquanto os erros do player forem menores que 20 e os acertos menores que 25
	while True:

		if player_one.get_total_errors() < MIDDLE_MODE:

			# player_one.hit() retorna um False ou um número(True). Se False ele sair do while
			to_return = player_one.hit()
			if to_return:
				my_camp.create_camp(to_return)
				player_one.errors = my_camp.get_errors()

				if my_camp.error == 1:
					score.guess_hit()
				elif my_camp.error == 0:
					score.guess_error()

				print('-' * 70)
				print('\tPontuação: [ {} ]'.format(score.get_total()), end=' ')
				player_one.get_info()

				hits_player(to_return)

				count += 1
				# Se o player alcançar 25 acertos ele é declarado vencedor
				if player_one.get_hits() == my_camp.get_total_positions():
					print(FRAME[2])
					score.winner()
					# Salvar dados
					db.saveData(ID + 1, score.get_total(), count, player_one.get_hits(), '10/10/2017')
					db.closeConnection()
					time.sleep(2)
					print('As posições das cobras eram essas:')
					for i in range(len(list_snakes)):
						print('Cobra {0} : {1} -> Acertos: {2}\n'.format(i, list_snakes[i], list_snakes_hits[i]))
					break

			else:
				break
		else:
			print(FRAME[1])
			score.loser()
			# Salvar dados
			db.saveData(ID + 1, score.get_total(), count, player_one.get_hits(), '10/10/2017')
			db.closeConnection()
			time.sleep(2)
			print('As posições das cobras eram essas:')
			for i in range(len(list_snakes)):
				print('Cobra {0} : {1} -> Acertos: {2}\n'.format(i, list_snakes[i], list_snakes_hits[i]))
			break


# Exibir as posições das cobras e dos acertos do jogador
def hits_player(value):
	for i in range(len(list_snakes)):
		for item in list_snakes[i]:
			if value in list_snakes[i]:
				list_snakes_hits[i].append(value)
				break


if __name__ == '__main__':
	main()