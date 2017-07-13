import pdb
import random

"""
Objetivo do jogo é eliminar as combras escondidas
Por: Alexsandro Façanha
ano: 07/2017
"""

"""
Descrição:

 0  1  2  3  4  5   6  7  8  9
10 11 12 13 14 15 |16 17 18 19
20 21 22 23 24 25 |26 27 28 29
30 31 32 33 34 35 |36 37 38 39
40 41 42 43 44 45 |46 47 48 49
50 51 52 53 54 55 |56 57 58 59
______________________________+-> limite vertical
60 61 62 63 64 65 |66 67 68 69
70 71 72 73 74 75 |76 77 78 79
80 81 82 83 84 85 |86 87 88 89
90 91 92 93 94 95 |96 97 98 99
				  +-> limite horizontal

"""
entrada = ''
campo = [i for i in range(1, 101)]
cobra = []

def exibirCampo(x):
	print('#' * 40)
	count = 0
	for item in campo:
		if x == item:
			campo.insert(item, 0)
			campo.remove(item)
			print('{0:3d}'.format(0), end=' ')
		else:
			print('{0:3d}'.format(item), end=' ')
		count += 1
		if count == 10:
			print()
			count = 0
	print('#' * 40)

def criarCobra():
	orientacao = random.randint(1, 2)
	print(orientacao)
	while True:
		inicio = random.randint(1, 101)
		if orientacao == 1:
			if (inicio < 6) or (inicio > 9 and inicio < 16) or \
			(inicio > 19 and inicio < 26) or(inicio > 29 and inicio < 36) or \
			(inicio > 39 and inicio < 46) or(inicio > 49 and inicio < 56) or \
			(inicio > 59 and inicio < 66) or(inicio > 69 and inicio < 76) or \
			(inicio > 79 and inicio < 86) or(inicio > 89 and inicio < 96):
				cobra = [i for i in range(inicio, inicio + 5)]
				break
		else:
			if inicio >= 1 and inicio < 60:
				cobra = [i for i in range(inicio, inicio + 50, 10)]
				break
	return cobra

	# print(cobra)

def grupoCobras():
	lista = []
	for i in range(0, 5):
		lista.append(criarCobra())
	print(lista)

exibirCampo(' ')
# criarCobra()
grupoCobras()

while True:

	while True:
		entrada = input('Digite um número: ').lower()
		if entrada in str(campo) and entrada != '0':
			exibirCampo(int(entrada))
			break
		elif entrada == 's':
			break

	if entrada == 's':
		break







