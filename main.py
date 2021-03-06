__author__ = 'alex.facanha18@gmail.com <asfmegas.github.io>'


"""
Objetivo do jogo é descobrir as combras escondidas no campo
Por: Alexsandro Façanha
ano: 07/2017

"""

import snake, camp, player
import scores, database
import _thread as thread
import os
from constants import *

import time, sys
from datetime import date

# para debug
import pdb

db = database.Database()
db.createTable()

count = 0
ID = 1
mode = 0
my_mode = ''

# Para pular as informações iniciais digitar qualquer coisa após o comando
option = sys.argv
if len(option) < 2:
	# Informações para o início do jogo.
	print(FRAME[0])
	time.sleep(TIME)
	print(FRAME[5])

	print('Pressione "Enter" para continuar...')
	input()

lista = db.getList()
my_list = []

now = date.today()
today = now.strftime("%d/%m/%Y")

# Adiciona itens do banco de dados na lista e defini um valor para o ID
for linha in lista:
	ID += 1
	my_list.append((linha[1], linha[2], linha[3], linha[4]))

while True:
	mode = input('\tDefina o modo: 1 EASY; 2 NORMAL; 3 HARD: ')
	if mode in '1 2 3'.split():
		if mode == '1':
			mode = EASY
			my_mode = 'easy'
		elif mode == '3':
			mode = HARD
			my_mode = 'hard'
		else:
			mode = NORMAL
			my_mode = 'normal'
		break
	elif mode.lower() == 's':
		sys.exit()


print('-' * WIDTH)
print('\tR A N K I N G - As 10 melhores partidas no modo {}.\n'.format(my_mode))

# Exibe apenas os 10 melhores colocados da lista
for linha in my_list:
	if linha[3] == mode:
		count += 1
		print('  {0}o. Acertos[{1:3d} ]  Erros[{2:3d} ]  Tentativas[{3:3d} ]  Pontuação[ {4:3d} ]'.format(count, \
																											linha[2], \
																											linha[1] - linha[2], \
																											linha[1], \
																											linha[0]))
		if count == 11:
			break

count = 0
print('-' * WIDTH)
print('Pressione "Enter" para continuar...')
input()


list_snakes = []
list_snakes_hits = [[] for i in range(mode)]

def main():
	global count, ID

	score = scores.Scores()

	my_camp = camp.Camp()

	while True:
		new_snake = snake.Snake()
		i = new_snake.get_orientation()
		s = new_snake.get_snake(my_camp.set_position(i))
		if my_camp.add_snake_camp(s):
			list_snakes.append(s)
			count += 1
		if count == mode:
			break
	count = 0

	player_one = player.Player()
	my_camp.create_camp(0)

	if mode == EASY: my_mode = EASY_MODE
	elif mode == NORMAL: my_mode = NORMAL_MODE
	elif mode == HARD: my_mode = HARD_MODE

	# Rode enquanto os erros do player forem menores que 20 e os acertos menores que 25
	while True:

		if player_one.get_total_errors() < my_mode:

			# player_one.hit() retorna um False ou um número(True). Se False ele sair do while
			to_return = player_one.guess()
			if to_return:
				my_camp.create_camp(to_return)
				player_one.errors = my_camp.get_errors()

				if my_camp.error == 1:
					score.guess_hit()
				elif my_camp.error == 0:
					score.guess_error()

				print('-' * WIDTH)
				print('\tPontuação: [ {} ]'.format(score.get_total()), end=' ')
				player_one.get_info()

				thread.start_new_thread(hits_player, (to_return, ))
				# hits_player(to_return)


				count += 1
				# Se o player alcançar 25 acertos ele é declarado vencedor
				if player_one.get_hits() == my_camp.get_total_positions():
					print(FRAME[2])
					time.sleep(2)
					score.winner()
					print('\tSua pontuação foi [ {} ]\n'.format(score.get_total()))

					# Salvar dados
					db.saveData(ID, score.get_total(), count, player_one.get_hits(), mode, today)
					db.closeConnection()

					print('As posições das cobras eram essas:\n')
					for i in range(len(list_snakes)):
						print('Cobra {0} : {1} -> Acertos: {2}\n'.format(i + 1, list_snakes[i], list_snakes_hits[i]))
					break

			else:
				break
		else:
			print(FRAME[1])
			time.sleep(2)
			score.loser()
			print('\tSua pontuação foi [ {} ]\n'.format(score.get_total()))

			# Salvar dados
			db.saveData(ID, score.get_total(), count, player_one.get_hits(), mode, today)
			db.closeConnection()

			print('As posições das cobras eram essas:\n')
			for i in range(len(list_snakes)):
				print('Cobra {0} : {1} -> Acertos: {2}\n'.format(i + 1, list_snakes[i], list_snakes_hits[i]))
			break


# Exibir as posições das cobras e dos acertos do jogador
def hits_player(value):
	# pdb.set_trace()
	for i in range(len(list_snakes)):
		for item in list_snakes[i]:
			if value in list_snakes[i]:
				list_snakes_hits[i].append(value)
				break
	thread.exit()


if __name__ == '__main__':
	main()