import csv
import sqlite3

# função para inserir dados automaticamente no banco de dados
# a parttir de um arquivo csv
def inserir_dados():
    conexao = sqlite3.connect(database='db.sqlite3')
    cursor = conexao.cursor() 
    
    with open(r'dados.csv','r') as csvdados:
        r = csv.reader(csvdados, delimiter=',', quotechar='"')
        next(r)

        for row in r:
             cursor.execute('''
                    INSERT INTO todo_tarefas (titulo, descricao, prazo, data_conclusao, situacao)
                    VALUES(?,?,?,?,?)
                    ''', row)
    
    conexao.commit()
    conexao.close()
  
