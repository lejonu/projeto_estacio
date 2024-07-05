from class_implementation.DBClass import DataBase
from dotenv import load_dotenv
import os

load_dotenv()

db = DataBase(os.getenv("host"), os.getenv("user"), os.getenv("password"))

db.create_db(database="projeto_estacio")


select_db = """
  USE projeto_estacio;
"""

db.execute_query("select_db", query=select_db)

create_table_aluno = """
CREATE TABLE IF NOT EXISTS `aluno` (
  `cpf` VARCHAR(11) NOT NULL,
  `nome` VARCHAR(45) NULL,
  `idade` VARCHAR(2) NULL,
  `sexo` VARCHAR(45) NULL,
  `celular` VARCHAR(11) NULL,
  `curso` VARCHAR(100) NULL,
  `turno` VARCHAR(10) NULL,
  PRIMARY KEY (`cpf`));
"""
db.execute_query("create_table_aluno", query=create_table_aluno)

create_table_frequencia = """
CREATE TABLE IF NOT EXISTS `frequencia` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cpf` VARCHAR(11) NOT NULL,
  `horario` DATETIME NOT NULL,
  PRIMARY KEY (`id`, `cpf`),
  INDEX `fk_frequencia_aluno_idx` (`cpf` ASC) VISIBLE,
  CONSTRAINT `fk_frequencia_aluno`
    FOREIGN KEY (`cpf`)
    REFERENCES `aluno` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
"""

db.execute_query("create_table_frequencia", query=create_table_frequencia) 
