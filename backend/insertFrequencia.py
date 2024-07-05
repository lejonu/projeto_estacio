from class_implementation.DBClass import DataBase
from dotenv import load_dotenv
import os
from datetime import datetime

# ts = datetime.now()
ts_temp = datetime(2024, 7, 1, 8)
ts = ts_temp.strftime('%Y-%m-%d %H:%M:%S')

load_dotenv()
db = DataBase(os.getenv("host"), os.getenv("user"), os.getenv("password"))

select_db = """
  USE projeto_estacio;
"""
db.execute_query("select_db", query=select_db)

insert_frequencia = f"""
INSERT INTO `frequencia` (`cpf`, `horario`) 
VALUES
('69991580611', '{ts}'),
('56808488649', '{ts}'),
('51701506602', '{ts}'),
('93585679617', '{ts}'),
('31984405530', '{ts}'),
('68377932687', '{ts}'),
('31994849146', '{ts}'),
('57879156666', '{ts}'),
('36878255660', '{ts}');
"""

db.execute_query("insert_aluno", query=insert_frequencia)
