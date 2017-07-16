import logging

DEBUG = 1
CRITICAL = 2
INFOR = 3
WARNING = 4
ERROR = 5

class MyDebug:

	def getLogDebug(self):
		return logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

	def getLogError(self):
		return logging.basicConfig(level=logging.ERROR, format=' %(asctime)s - %(levelname)s - %(message)s')

	def getLogInfo(self):
		return logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

	def salvarDebug(self, nome='myFileLog.txt'):
		logging.basicConfig(filename=nome, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

	def comparador(self, valor1=0, valor2=0, nome1='x', nome2='y'):
		logging.debug(str(nome1) + ': ' + str(valor1) + ' ' + str(nome2) + ' : ' + str(valor2))

	def inicioDebug(self, dados):
		logging.debug('Inicio do debug: ' + str(dados))

	def fimDebug(self, dados):
		logging.debug('Fim do debug: ' + str(dados))

	def contadorDebug(self, valor):
		logging.debug('Contador: ' + str(valor))

	def verificarValor(self, valor):
		logging.error('Erro encontrado: ' + str(valor))

	def desabilitar(self, valor=1):
		if valor == 1: logging.disable(logging.DEBUG)
		elif valor == 2: logging.disable(logging.CRITICAL)
		elif valor == 3: logging.disable(logging.INFO)
		elif valor == 4: logging.disable(logging.WARNING)
		elif valor == 5: logging.disable(logging.ERROR)

	# Para comparações de valores
	def compararValor(self, var, valor):
		assert var == valor, '\n\n\tO valor esperado era "' + str(valor) + '" mas o valor foi "' + str(var) + '": não foi o esperado!\n'