import pdb
import random

"""
Objetivo do jogo é eliminar as combras escondidas
Por: Alexsandro Façanha
ano: 07/2017
"""

"""

  1   2   3   4   5   6  | 7   8   9  10 
 11  12  13  14  15  16  |17  18  19  20 
 21  22  23  24  25  26  |27  28  29  30 
 31  32  33  34  35  36  |37  38  39  40 
 41  42  43  44  45  46  |47  48  49  50 
 51  52  53  54  55  56  |57  58  59  60 
 ------------------------+---------------> limite vertical
 61  62  63  64  65  66  |67  68  69  70 
 71  72  73  74  75  76  |77  78  79  80 
 81  82  83  84  85  86  |87  88  89  90 
 91  92  93  94  95  96  |97  98  99 100 
                         +--> limite horizontal

"""


entrada = ''
campo = [i for i in range(1, 101)]
cobra = []
listaCobras = []
tentativas = []
posiscoes = []
acerto = False
voltas = 0
acertos, erros = 0, 0


def trocarCaractere(item, x):
	campo.insert(item, x)
	campo.remove(item)

def exibirCampo(x):
	global acerto, voltas, acertos, erros
	print('#' * 40)
	count = 0

	for item in campo:
		if x == item:
			if x in posiscoes:
				trocarCaractere(item, 1)
				print('{0:3d}'.format(1), end=' ')
				acerto = True
				acertos += 1
				if acertos == contarPosicoes():
					print('\n\tParabéns!! Você venceu!!!\n')
			else:
				trocarCaractere(item, 0)
				print('{0:3d}'.format(0), end=' ')
				acerto = False
				erros += 1
		else:
			print('{0:3d}'.format(item), end=' ')
		count += 1
		if count == 10:
			print()
			count = 0
	print('#' * 40)
	if voltas > 0:
		if acerto: 
			print('\n;-) Você acertou!!!', end=' ')
		elif not acerto:
			print('\n:-( Você errou!', end=' ')
	voltas = 1

def contarPosicoes():
	lista = []
	for i in posiscoes:
		if i not in lista:
			lista.append(i)
	return len(lista)

def criarCobra():
	orientacao = random.randint(1, 2) # 1 horizontal ou 2 vertical
	while True:
		inicio = random.randint(1, 101)
		if inicio not in posiscoes:
			if orientacao == 1:
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
					cobra = [i for i in range(inicio, inicio + 5)]
					break
			else:
				if inicio >= 1 and inicio < 60:
					cobra = [i for i in range(inicio, inicio + 50, 10)]
					break
	return cobra


def grupoCobras():
	for i in range(0, 5):
		cobra = criarCobra()
		listaCobras.append(cobra)
		for z in cobra:
			posiscoes.append(z)

	# print(listaCobras)
	# print(posiscoes)

grupoCobras()
print('Você tem {} alvos com no máximo 25 possíveis erros. Boa sorte!!!'.format(contarPosicoes()))
exibirCampo(' ')


while True:

	if erros < 20:
		while True:
			entrada = input('Digite um número: ').lower()
			if entrada in str(campo) and entrada != '0' and entrada not in tentativas:
				try:
					exibirCampo(int(entrada))
					tentativas.append(entrada)
					print('Tentativas: {0} | Acertos: {1} | Erros: {2} | Alvos: {3}\n'.format(len(tentativas), acertos, erros, contarPosicoes()))
					break
				except:
					print()
			elif entrada == 's':
				break
	else:
		print('Gamer Over\nSuas tentativas acabaram!\n\n')
		break

	if entrada == 's':
		break
