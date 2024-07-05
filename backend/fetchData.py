from class_implementation.DBClass import DataBase
from dotenv import load_dotenv
import os

load_dotenv()

db = DataBase(os.getenv("host"), os.getenv("user"), os.getenv("password"))

select_db = """
  USE projeto_estacio;
"""

db.execute_query("select_db", query=select_db)

fetch_data = """
  SELECT a.cpf, a.nome, a.idade, a.sexo, a.celular, a.curso, a.turno, f.horario FROM frequencia as f INNER JOIN aluno as a ON a.cpf = f.cpf; 
"""

for cpf in list(db.fetch_data(query=fetch_data)):
  print(cpf)
