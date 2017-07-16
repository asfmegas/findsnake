import database

bd = database.Database()
bd.criarTabela()
# bd.inserir(2, 150, '16/07/2017')
bd.obterLista()
bd.fecharConexao()