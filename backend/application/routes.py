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

@app.route("/frequencia", methods=['GET', 'POST'])
@cross_origin()
def registrarFrequencia():
  # ts_temp = datetime(2024, 7, 25, 8)
  # ts = ts_temp.strftime('%Y-%m-%d %H:%M:%S')
  ts = datetime.now()
  try:
    cpf = request.json['cpf']
    insert_frequencia = f"""INSERT INTO `frequencia` (`cpf`, `horario`) VALUES ({cpf}, '{ts}');"""

    db.execute_query("insert_frequencia", query=insert_frequencia)

    response = app.response_class(
        response=json.dumps({'Message': 'CPF inserido com sucesso'}),
        status=200,
        mimetype='application/json'
    )
    return response

  except Exception as e:
    return e
  
@app.route("/novoAluno", methods=['GET', 'POST'])
@cross_origin()
def insertAluno():
  # ts_temp = datetime(2024, 7, 25, 8)
  # ts = ts_temp.strftime('%Y-%m-%d %H:%M:%S')
  ts = datetime.now()
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
    # insert_aluno = f"""INSERT INTO `aluno` (`cpf`) VALUES ({cpf});"""
    

    db.execute_query("insert_aluno", query=insert_aluno)

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


@app.route("/graph01")
@cross_origin()

def graph01():
  fetch_data = """
  SELECT cpf, horario FROM frequencia;
  """
  alunos_por_dia = db.fetch_data(query=fetch_data)
  df = pd.DataFrame(alunos_por_dia, columns=["cpf", "horario"])
  df['horario'] = df['horario'].astype(str).str[:10]
  por_dia = df.groupby(df['horario'])['cpf'].count().reset_index()

  fig_barra = px.bar(por_dia, x='horario', y='cpf', 
                       title='Quantidade de Alunos por Dia.',
                       labels={'horario': 'Dia','cpf': 'Alunos' },
                       color='horario', 
                       color_discrete_sequence=px.colors.qualitative.Pastel)

  fig_barra.show()

  graphJSON = plotly.io.to_json(fig_barra, pretty=True)
  return graphJSON

@app.route("/")
@cross_origin()
def index():
  # Graph One
  df = px.data.medals_wide()
  fig1 = px.bar(df, x="nation", y=['gold', 'silver', 'bronze'], title = "Wide=Form input")
  graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
  
  # Graph Two
  df = px.data.iris()
  fig2 = px.scatter_3d(df, x="sepal_length", y="sepal_width", z="petal_width", color="species", title="Iris Dataset")
  graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

  # Graph three
  df = px.data.gapminder().query("continent=='Oceania'")
  fig3 = px.line(df, x='year', y='lifeExp', color='country', title='Life Expectancy')
  graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    
  return render_template("index.html", tittle="Home", graph1JSON=graph1JSON, graph2JSON=graph2JSON, graph3JSON=graph3JSON)