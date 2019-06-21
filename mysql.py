import MySQLdb

host = "localhost"
user = "root"
password = "buibui10"
db = "ex03"
port = 3306

conex = MySQLdb.connect(host, user, password, db, port)

c = conex.cursor(MySQLdb.cursors.DictCursor)

def consultarCidade(fields, tables, where=None):

	global c #indicar pra pega o cursor 
	
	query = "SELECT " + fields + " FROM " + tables
	if (where):#verifica se o where foi passado
		query = query + " WHERE " + where 	
	c.execute(query)
	return c.fetchall()

#result = consultar("id, nome", "tb_cidade")
#print (result[0]["nome"]) #linha 0 campo nome

def inserirCidade(latitude, longitude, nome):
	global c, conex

	query = f"INSERT INTO tb_cidade VALUES (DEFAULT, {latitude}, {longitude}, '{nome}')"
	#print(query)
	c.execute(query)
	conex.commit()

#inserirCidade(35,25, 'Caieiras')


def atualizarCidade(latitude, longitude, nome, id):
	global c, conex

	query = f"UPDATE tb_cidade SET latitude = {latitude}, " \
			f"longitude = {longitude},  nome = '{nome}'" \
			f" WHERE id = {id}" 

	#print(query)
	c.execute(query)
	conex.commit()

#atualizarCidade(40,50, 'São Paulo', 1)

def deletarCidade(id):
	global c, conex

	queryTempo = "DELETE FROM tb_tempo WHERE id_cidade = " + id #para apagar o registro FK
	query = "DELETE FROM tb_cidade WHERE id = " + id

	#print(query)
	#print(queryTempo)

	c.execute(queryTempo)
	c.execute(query)

	conex.commit()


deletarCidade("1")
print(consultarCidade("*", "tb_cidade"))