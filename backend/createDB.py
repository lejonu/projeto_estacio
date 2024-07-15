from class_implementation.DBClass import DataBase

db = DataBase()
db.create_db()
db.select_db()

create_table_aluno = """
CREATE TABLE IF NOT EXISTS `aluno` (
  `cpf` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(200) NULL,
  `idade` INT(3) NULL,
  `sexo` ENUM('M', 'F') NULL,
  `celular` VARCHAR(45) NULL,
  `curso` VARCHAR(100) NULL,
  `turno` ENUM('M', 'T', 'N') NULL,
  PRIMARY KEY (`cpf`));
"""
db.execute_query("create_table_aluno", query=create_table_aluno)

create_table_frequencia = """
CREATE TABLE IF NOT EXISTS `frequencia` (
  `id_frequencia` INT NOT NULL AUTO_INCREMENT,
  `horario` DATETIME NULL,
  `cpf` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_frequencia`, `cpf`),
  INDEX `fk_frequencia_aluno_idx` (`cpf` ASC) VISIBLE,
  CONSTRAINT `fk_frequencia_aluno`
    FOREIGN KEY (`cpf`)
    REFERENCES `projeto_estacio`.`aluno` (`cpf`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
"""

db.execute_query("create_table_frequencia", query=create_table_frequencia) 
