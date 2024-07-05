from class_implementation.DBClass import DataBase
from dotenv import load_dotenv
import os
load_dotenv()
db = DataBase(os.getenv("host"), os.getenv("user"), os.getenv("password"))
db.create_db(database="proj_extensao")

select_db = """
  USE projeto_estacio;
"""

db.execute_query("select_db", query=select_db)

insert_aluno = """
INSERT INTO `projeto_estacio`.`aluno` (`cpf`, `nome`, `idade`, `sexo`, `celular`, `curso`, `turno`) 
VALUES 
('69991580611', 'Cauã Kauê Santos', '70', 'Masculino', '31984687931', 'DIREÇÃO DEFENSIVA', 'TARDE'),
('56808488649', 'Antonella Elisa Andrea', '72', 'Feminino', '31997606928', 'EQUIPAMENTOS OBRIGATÓRIOS', 'MANHA'),
('22210627605', 'Catarina Sophie Gabrielly', '34', 'Feminino', '31985336339', 'DICAS E MACETES', 'NOITE'),
('51701506602', 'Sebastião Leandro Ferreira', '45', 'Masculino', '31985600375', 'LEGISLAÇÃO DE TRÂNSITO', 'MANHA'),
('93585679617', 'Levi Miguel Paulo Novaes', '34', 'Masculino', '31995292379', 'DICAS E MACETES', 'NOITE'),
('31984405530', 'Anthony João Assis', '28', 'Masculino', '31984405530', 'MECÂNICA BÁSICA', 'TARDE'),
('68377932687', 'Pietro Cauã Leandro Cavalcanti', '19', 'Masculino', '31996689915', 'LEGISLAÇÃO DE TRÂNSITO', 'TARDE'),
('31994849146', 'Marli Eliane Nicole dos Santos', '43', 'Feminino', '31994849146', 'EQUIPAMENTOS OBRIGATÓRIOS', 'NOITE'),
('57879156666', 'Jéssica Sophie Laís Vieira', '27', 'Feminino', '31997101612', 'MEIO AMBIENTE', 'TARDE'),
('36878255660', 'Gael Pedro Viana', '32', 'Masculino', '31996370990', 'LEGISLAÇÃO DE TRÂNSITO', 'NOITE');
"""

db.execute_query("insert_aluno", query=insert_aluno) 
