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
INSERT INTO `aluno` (`cpf`, `nome`, `idade`, `sexo`, `celular`, `curso`, `turno`) 
VALUES 
('34659928659', 'Andrea Maria Isis da Costa', '23', 'Feminino', '31986210289', 'EQUIPAMENTOS OBRIGATÓRIOS', 'MANHA'),
('72893102689', 'Vinicius Heitor Renato Ramos', '32', 'Masculino', '31995226216', 'DICAS E MACETES', 'TARDE'),
('78375552607', 'Gabriela Liz Fogaça', '19', 'Feminino', '31991759068', 'LEGISLAÇÃO DE TRÂNSITO', 'NOITE'),
('89998625696', 'Lívia Rafaela Fernandes', '20', 'Masculino', '31984687931', 'MECÂNICA BÁSICA', 'NOITE'),
('47741855662', 'Enrico Bernardo', '41', 'Masculino', '31984687931', 'EQUIPAMENTOS OBRIGATÓRIOS', 'TARDE'),
('31178965627', 'Yasmin Isabella Tereza Pinto', '45', 'Feminino', '31989008255', 'MEIO AMBIENTE', 'MANHA'),
('51574823612', 'Jorge Alexandre Emanuel Rodrigues', '27', 'Masculino', '31997656803', 'DIREÇÃO DEFENSIVA', 'TARDE'),
('57772594640', 'Iago Gael Vitor Viana', '29', 'Masculino', '31984687931', 'MEIO AMBIENTE', 'NOITE'),
('14558937652', 'Sônia Alice Gabrielly Campos', '25', 'Feminino', '31992760197', 'EQUIPAMENTOS OBRIGATÓRIOS', 'TARDE'),
('65581013608', 'Liz Allana Souza', '18', 'Masculino', '31995247146', 'MEIO AMBIENTE', 'MANHA'),
('45769993626', 'Mariah Malu Sandra Duarte', '22', 'Feminino', '31994892650', 'EQUIPAMENTOS OBRIGATÓRIOS', 'TARDE'),
('17618269645', 'Camila Nicole Clara Aparício', '26', 'Feminino', '31984687931', 'DIREÇÃO DEFENSIVA', 'TARDE'),
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
