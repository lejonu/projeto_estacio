import pandas as pd
import plotly
import plotly.express as px
import json
from application import app
from class_implementation.DBClass import DataBase
from dotenv import load_dotenv
import os
from flask_cors import CORS, cross_origin
from datetime import datetime
from flask import request, render_template

load_dotenv()

db = DataBase(os.getenv("host"), os.getenv("user"), os.getenv("password"))

select_db = """
  USE projeto_estacio;
"""
db.execute_query("select_db", query=select_db)

# Routes para o aplicativo

@app.route("/novoAluno", methods=['GET', 'POST'])
@cross_origin()
def novoAluno():
  try:
    cpf = request.json['cpf']
    nome = request.json['nome']
    idade = request.json['idade']
    sexo = request.json['sexo']
    celular = request.json['celular']
    curso = request.json['curso']
    turno = request.json['turno']

    insert_aluno = f"""INSERT INTO `projeto_estacio`.`aluno` (`cpf`, `nome`, `idade`, `sexo`, `celular`, `curso`, `turno`) 
    VALUES ('{cpf}', '{nome}', '{idade}', '{sexo}', '{celular}', '{curso}', '{turno}');"""

    db.execute_query("insert_aluno", query=insert_aluno)

    response = app.response_class(
        response=json.dumps({'Message': 'CPF inserido com sucesso'}),
        status=200,
        mimetype='application/json'
    )
    return response

  except Exception as e:
    return e

@app.route("/registrarFrequencia", methods=['GET', 'POST'])
@cross_origin()
def registrarFrequencia():
  # ts_temp = datetime(2024, 7, 25, 8)
  # ts = ts_temp.strftime('%Y-%m-%d %H:%M:%S')
  ts = datetime.now()
  try:
    cpf = request.json['cpf']
    insert_frequencia = f"""INSERT INTO `frequencia` (`cpf`, `horario`) VALUES ('{cpf}', '{ts}');"""

    db.execute_query("insert_frequencia", query=insert_frequencia)

    response = app.response_class(
        response=json.dumps({'Message': 'CPF inserido com sucesso'}),
        status=200,
        mimetype='application/json'
    )
    return response

  except Exception as e:
    return e
  

@app.route("/alunos")
@cross_origin()
def getAlunos():
  print("Entrou na route alunos")
  nome_cpf_query = """
  SELECT nome, cpf FROM aluno;
  """
  nome_cpf = db.fetch_data(query=nome_cpf_query)
  payload = []
  content = {}

  for result in nome_cpf:
      content = {'nome': result[0], 'cpf': result[1]}
      payload.append(content)
      content = {}

  response = app.response_class(
      response=json.dumps(payload),
      status=200,
      mimetype='application/json'
      
  )
  return response



# Gráficos
@app.route("/")
@cross_origin()
def index():
  fetch_alunos="""
  SELECT * FROM aluno;
  """
  alunos = db.fetch_data(query=fetch_alunos)

  df_alunos = pd.DataFrame(alunos, columns=["cpf", "nome", "idade", "sexo", "celular", "curso", "turno"])
  # print(df_alunos.head())
  registros_por_curso = df_alunos['curso'].value_counts()
  # print(registros_por_curso.head())
  alunosPorCursoPie = px.pie(df_alunos, names=registros_por_curso.index, values=registros_por_curso.values, 
                        title='Porcentagem de Alunos por Curso.',
                        # labels={'dia': 'Dia','cpf': 'Alunos' },
                        # color='cpf',
                        color_discrete_sequence=px.colors.qualitative.Pastel              
                        )
  alunosPorCursoPieJSON = json.dumps(alunosPorCursoPie, cls=plotly.utils.PlotlyJSONEncoder)

  df_alunos_por_curso = df_alunos.groupby(['curso', 'sexo'])['cpf'].count().reset_index()

  alunosPorCursoBar = px.bar(df_alunos_por_curso, x='cpf', y='curso',
                        title='Número de Alunos por Curso e Sexo.',
                        labels={'cpf': 'Alunos','curso': 'Curso', 'sexo': 'Sexo:' },
                        color='sexo',
                        color_discrete_sequence=px.colors.qualitative.Pastel              
                        )
  alunosPorCursoBarJSON = json.dumps(alunosPorCursoBar, cls=plotly.utils.PlotlyJSONEncoder)


  # df_alunos_por_curso = df_alunos.groupby('curso')['cpf'].count()
  # print(df_alunos_por_curso.head())

  return render_template("index.html", 
                         tittle="Alunos", 
                         alunosPorCursoPieJSON=alunosPorCursoPieJSON, 
                         alunosPorCursoBarJSON=alunosPorCursoBarJSON
                         )

@app.route("/frequencia_alunos")
@cross_origin()
def frequencia_alunos():
  # Gráfico quantidade de alunos por dia
  fetch_frequencia_alunos="""
  SELECT a.cpf, a.nome, a.idade, a.sexo, a.celular, a.curso, a.turno, f.horario FROM aluno AS a INNER JOIN frequencia AS f ON a.cpf = f.cpf;
  """
  frequencia_alunos = db.fetch_data(query=fetch_frequencia_alunos)
  # for i in frequencia_alunos:
  #   print(i)
  #   exit()
  df_freq = pd.DataFrame(frequencia_alunos, columns=["cpf", "nome", "idade", "sexo", "celular", "curso", "turno", "dia"])
  df_freq['dia'] = df_freq['dia'].astype(str).str[:10]
  df_freq['cpf'] = df_freq['cpf'].astype(str)
  # print(df_freq)
  frequenciaAlunos = df_freq.groupby(['dia'])['cpf'].count().reset_index()

  alunosPorDia = px.bar(frequenciaAlunos, x='dia', y='cpf', 
                        title='Quantidade de Alunos por Dia.',
                        labels={'dia': 'Dia','cpf': 'Alunos' },
                        color='cpf',
                        color_discrete_sequence=px.colors.qualitative.Pastel
                        
                        )
  alunosPorDiaJSON = json.dumps(alunosPorDia, cls=plotly.utils.PlotlyJSONEncoder)

  return render_template("frequencia_alunos.html", 
                         tittle="Frequência", 
                         alunosPorDiaJSON=alunosPorDiaJSON
                         )

# @app.route("/alunos_cadastrados")
# @cross_origin()
# def alunos_cadastrados():
