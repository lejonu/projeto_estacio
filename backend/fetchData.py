from class_implementation.DBClass import DataBase

db = DataBase()
db.select_db()

fetch_data = """
  SELECT a.cpf, a.nome, a.idade, a.sexo, a.celular, a.curso, a.turno, f.horario FROM frequencia as f INNER JOIN aluno as a ON a.cpf = f.cpf; 
"""

for cpf in list(db.fetch_data(query=fetch_data)):
  print(cpf)
