from class_implementation.DBClass import DataBase
from datetime import datetime

# ts = datetime.now()
ts_temp = datetime(2024, 7, 13, 8)
ts = ts_temp.strftime('%Y-%m-%d %H:%M:%S')

db = DataBase()

select_db = """
  USE projeto_estacio;
"""
db.execute_query("select_db", query=select_db)

insert_frequencia = f"""
INSERT INTO `frequencia` (`cpf`, `horario`) 
VALUES
('MjIyMTA2Mjc2MDU=', '{ts}'),
('MTc2MTgyNjk2NDU=', '{ts}'),
('MTQ1NTg5Mzc2NTI=', '{ts}'),
('MzExNzg5NjU2Mjc=', '{ts}'),
('MzQ2NTk5Mjg2NTk=', '{ts}'),
('MzY4NzgyNTU2NjA=', '{ts}'),
('NDc3NDE4NTU2NjI=', '{ts}'),
('NDU3Njk5OTM2MjY=', '{ts}'),
('NjgzNzc5MzI2ODc=', '{ts}'),
('Njk5OTE1ODA2MTE=', '{ts}'),
('NjU1ODEwMTM2MDg=', '{ts}'),
('NTc3NzI1OTQ2NDA=', '{ts}'),
('NTc4NzkxNTY2NjY=', '{ts}'),
('NTE1NzQ4MjM2MTI=', '{ts}'),
('NTE3MDE1MDY2MDI=', '{ts}'),
('NTY4MDg0ODg2NDk=', '{ts}'),
('NzgzNzU1NTI2MDc=', '{ts}'),
('NzI4OTMxMDI2ODk=', '{ts}'),
('ODk5OTg2MjU2OTY=', '{ts}'),
('OTM1ODU2Nzk2MTc=', '{ts}');
"""

db.execute_query("insert_aluno", query=insert_frequencia)
