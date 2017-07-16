__author__ = 'asfmgas.github.io'

import sqlite3

class Database(object):
	def __init__(self):
		self.db = None
		self.cursor = None
		self.__conection()

	def __conection(self):
		try:
			self.db = sqlite3.connect(r'dados.db')
			self.cursor = self.db.cursor()
		except Exception as erro:
			print('Erro ao tentar conexão com banco de dados:', erro)
			print('Tipo do erro:', type(erro))

	def createTable(self):
		try:
			self.cursor.execute("CREATE TABLE IF NOT EXISTS snake (id integer, score_total integer, shoots integer, hits integer, data text)")
		except Exception as erro:
			print('Erro ao criar tabela:', erro)
			print('Tipo de erro:', type(erro))

	def saveData(self, ID=1, pontos=0, tentativas=0, acertos=0, data='01/01/1990'):
		try:
			self.cursor.execute("INSERT INTO snake VALUES (?, ?, ?, ?, ?)", (ID, pontos, tentativas, acertos, data,))
			self.db.commit()
		except Exception as erro:
			print('Erro ao salvar dados:', erro)
			print('Tipo de erro:', type(erro))

	def closeConnection(self):
		try:
			self.cursor.close()
			self.db.close()
		except Exception as erro:
			print('Erro ao tentar fechar conexao:', erro)
			print('Tipo de erro:', type(erro))

	def getList(self):
		try:
			return self.cursor.execute('SELECT * FROM snake ORDER BY score_total DESC')
		except Exception as erro:
			print('Erro ao listar dados:', erro)
			print('Tipo de erro:', type(erro))
			return False

	def getTotal(self):
		count = 0
		try:
			dados = self.cursor.execute('SELECT * FROM snake')
			for linha in dados:
				count += 1
			return count
		except Exception as erro:
			print('Erro ao listar dados:', erro)
			print('Tipo de erro:', type(erro))
			return count

