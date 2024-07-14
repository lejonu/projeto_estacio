from class_implementation.DBClass import DataBase
from dotenv import load_dotenv
import base64
import os
load_dotenv()

db = DataBase(os.getenv("host"), os.getenv("user"), os.getenv("password"))
db.create_db(database="proj_extensao")

select_db = """
  USE projeto_estacio;
"""

db.execute_query("select_db", query=select_db)

insert_aluno = """
INSERT INTO `aluno` (`cpf`,`nome`,`idade`,`sexo`,`celular`,`curso`,`turno`) 
VALUES 
('MjIyMTA2Mjc2MDU=','Q2F0YXJpbmEgU29waGllIEdhYnJpZWxseQ==',32,'F','MzE5ODUzMzYzMzk=','DICAS E MACETES','N'),
('MTc2MTgyNjk2NDU=','Q2FtaWxhIE5pY29sZSBDbGFyYSBBcGFy7WNpbw==',26,'F','MzE5ODQ2ODc5MzE=','DIREÇÃO DEFENSIVA','T'),
('MTQ1NTg5Mzc2NTI=','U/RuaWEgQWxpY2UgR2FicmllbGx5IENhbXBvcw==',25,'F','MzE5OTI3NjAxOTc=','EQUIPAMENTOS OBRIGATÓRIOS','T'),
('MzExNzg5NjU2Mjc=','WWFzbWluIElzYWJlbGxhIFRlcmV6YSBQaW50bw==',23,'F','MzE5ODkwMDgyNTU=','MEIO AMBIENTE','M'),
('MzQ2NTk5Mjg2NTk=','QW5kcmVhIE1hcmlhIElzaXMgZGEgQ29zdGE=',23,'F','MzE5ODYyMTAyODk=','EQUIPAMENTOS OBRIGATÓRIOS','M'),
('MzY4NzgyNTU2NjA=','R2FlbCBQZWRybyBWaWFu',32,'M','MzE5OTYzNzA5OTA=','LEGISLAÇÃO DE TRÂNSITO','N'),
('NDc3NDE4NTU2NjI=','RW5yaWNvIEJlcm5hcmRv',41,'M','MzE5ODQ2ODc5MzE=','EQUIPAMENTOS OBRIGATÓRIOS','T'),
('NDU3Njk5OTM2MjY=','TWFyaWFoIE1hbHUgU2FuZHJhIER1YXJ0ZQ==',22,'F','MzE5OTQ4OTI2NTA=','EQUIPAMENTOS OBRIGATÓRIOS','T'),
('NjgzNzc5MzI2ODc=','UGlldHJvIENhdeMgTGVhbmRybyBDYXZhbGNhbnRp',19,'M','MzE5OTY2ODk5MTU=','LEGISLAÇÃO DE TRÂNSITO','T'),
('Njk5OTE1ODA2MTE=','Q2F14yBLYXXqIFNhbnRvcw==',55,'M','MzE5ODQ2ODc5MzE=','DIREÇÃO DEFENSIVA','T'),
('NjU1ODEwMTM2MDg=','TGl6IEFsbGFuYSBTb3V6YQ==',18,'F','MzE5OTUyNDcxNDY=','MEIO AMBIENTE','M'),
('NTc3NzI1OTQ2NDA=','SWFnbyBHYWVsIFZpdG9yIFZpYW5h',19,'M','MzE5ODQ2ODc5MzE=','MEIO AMBIENTE','N'),
('NTc4NzkxNTY2NjY=','Sulzc2ljYSBTb3BoaWUgTGHtcyBWaWVpcmE=',27,'F','MzE5OTcxMDE2MTI=','MEIO AMBIENTE','N'),
('NTE1NzQ4MjM2MTI=','Sm9yZ2UgQWxleGFuZHJlIEVtYW51ZWwgUm9kcmlndWVz',27,'M','MzE5OTc2NTY4MDM=','DIREÇÃO DEFENSIVA','T'),
('NTE3MDE1MDY2MDI=','U2ViYXN0aeNvIExlYW5kcm8gRmVycmVpcmE=',45,'M','MzE5ODU2MDAzNzU=','LEGISLAÇÃO DE TRÂNSITO','M'),
('NTY4MDg0ODg2NDk=','QW50b25lbGxhIEVsaXNhIEFuZHJlYQ==',23,'F','MzE5OTc2MDY5Mjg=','EQUIPAMENTOS OBRIGATÓRIOS','M'),
('NzgzNzU1NTI2MDc=','R2FicmllbGEgTGl6IEZvZ2HnYQ==',19,'F','MzE5OTE3NTkwNjg=','LEGISLAÇÃO DE TRÂNSITO','N'),
('NzI4OTMxMDI2ODk=','VmluaWNpdXMgSGVpdG9yIFJlbmF0byBSYW1vcw==',32,'M','MzE5OTUyMjYyMTY=','DICAS E MACETES','T'),
('ODk5OTg2MjU2OTY=','TO12aWEgUmFmYWVsYSBGZXJuYW5kZXM=',20,'F','MzE5ODQ2ODc5MzE=','MECÂNICA BÁSICA','N'),
('OTM1ODU2Nzk2MTc=','TGV2aSBNaWd1ZWwgUGF1bG8gTm92YWVz',34,'M','MzE5OTUyOTIzNzk=','DICAS E MACETES','N');
"""

db.execute_query("insert_aluno", query=insert_aluno) 
