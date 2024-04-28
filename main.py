import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='xxx',
    database='crud-python'
)

cursor = conexao.cursor()

# CREATE
# nome_produto = 'Cacau'
# valor = 15
# comm = f'INSERT INTO vendas (nome_prod, valor_prod) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comm)
# conexao.commit()

# READ
# comm = 'SELECT * FROM vendas'
# cursor.execute(comm)
# resultado = cursor.fetchall() #Ler Banco de Dados
# print(resultado)

# UPDATE
# valor = 6
# nome_produto = "Cacau"
# comm = f'UPDATE vendas SET valor_prod = {valor} WHERE nome_prod = "{nome_produto}"'
# cursor.execute(comm)
# conexao.commit() #Edita o Banco de Dados


# DELETE
nome_produto = "Cacau"
comm = f'DELETE FROM vendas WHERE nome_prod = "{nome_produto}"'
cursor.execute(comm)
conexao.commit()


cursor.close()
conexao.close()