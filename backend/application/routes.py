from class_implementation.DBClass import DataBase
from application import app

import pandas as pd
import plotly
import plotly.express as px
import json
from flask_cors import CORS, cross_origin
from datetime import datetime
from flask import request, render_template
from dotenv import load_dotenv
load_dotenv()

db = DataBase()
db.select_db()

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
  try:
    # ts_temp = datetime(2024, 7, 25, 8)
    # ts = ts_temp.strftime('%Y-%m-%d %H:%M:%S')
    ts = datetime.now()
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
  try:
    nome_cpf_query = """
    SELECT nome, cpf, celular FROM aluno;
    """
    nome_cpf = db.fetch_data(query=nome_cpf_query)
    payload = []
    content = {}

    for result in nome_cpf:
        content = {'nome': result[0], 'cpf': result[1], 'celular': result[2]}
        payload.append(content)
        content = {}

    response = app.response_class(
        response=json.dumps(payload),
        status=200,
        mimetype='application/json'   
    )
    return response
  except Exception as e:
    return "exception"
  
# Gráfico para o aplicativo
@app.route("/graph01App")
@cross_origin()
def graph01App():
  try:
    fetch_data = """
    SELECT cpf, horario FROM frequencia;
    """
    alunos_por_dia = db.fetch_data(query=fetch_data)

    df = pd.DataFrame(alunos_por_dia, columns=["cpf", "horario"])
    df['horario'] = df['horario'].astype(str).str[:10]
    por_dia = df.groupby(df['horario'])['cpf'].count().reset_index()

    fig_barra = px.bar(por_dia, x='horario', y='cpf', 
                          title='Quantidade de Alunos por Dia',
                          labels={'horario': 'Dia','cpf': 'Alunos' },
                          color='cpf', 
                          color_discrete_sequence=px.colors.qualitative.Pastel
                          )
    # fig_barra.show()

    graphJSON = plotly.io.to_json(fig_barra, pretty=True)
    return graphJSON
  except Exception as e:
    return "Exception"

# Gráficos para web
@app.route("/")
@cross_origin()
def index():
  try:
    fetch_alunos="""
    SELECT * FROM aluno;
    """
    alunos = db.fetch_data(query=fetch_alunos)

    df_alunos = pd.DataFrame(alunos, columns=["cpf", "nome", "idade", "sexo", "celular", "curso", "turno"])

    registros_por_curso = df_alunos['curso'].value_counts()

    alunosPorCursoPie = px.pie(df_alunos, names=registros_por_curso.index, values=registros_por_curso.values, 
                          title='Porcentagem de Alunos por Curso',
                          # labels={'dia': 'Dia','cpf': 'Alunos' },
                          # color='cpf',
                          color_discrete_sequence=px.colors.qualitative.Pastel              
                          )
    alunosPorCursoPieJSON = json.dumps(alunosPorCursoPie, cls=plotly.utils.PlotlyJSONEncoder)

    df_alunos_por_curso = df_alunos.groupby(['curso', 'sexo'])['cpf'].count().reset_index()

    df_alunos_por_curso['sexo'] = df_alunos_por_curso['sexo'].map({
        'M': 'Masculino',
        'F': 'Feminino'
    })

    alunosPorCursoBar = px.bar(df_alunos_por_curso, x='cpf', y='curso',
                          title='Número de Alunos por Curso e Sexo',
                          labels={'cpf': 'Alunos','curso': 'Curso', 'sexo': 'Sexo:' },
                          color='sexo',
                          color_discrete_sequence=px.colors.qualitative.Pastel              
                          )
    alunosPorCursoBarJSON = json.dumps(alunosPorCursoBar, cls=plotly.utils.PlotlyJSONEncoder)

    df_alunos['turno'] = df_alunos['turno'].map({
        'M': 'Manhã',
        'T': 'Tarde',
        'N': 'Noite'
    })

    registros_por_turno = df_alunos['turno'].value_counts()
    # print(registros_por_curso.head())
    alunosPorTurnoPie = px.pie(df_alunos, names=registros_por_turno.index, values=registros_por_turno.values, 
                          title='Porcentagem de Alunos por Turno',
                          # labels={'dia': 'Dia','cpf': 'Alunos' },
                          # color='cpf',
                          color_discrete_sequence=px.colors.qualitative.Vivid              
                          )
    alunosPorTurnoPieJSON = json.dumps(alunosPorTurnoPie, cls=plotly.utils.PlotlyJSONEncoder)

    df_alunos_por_turno = df_alunos.groupby(['turno', 'sexo'])['cpf'].count().reset_index()
    df_alunos_por_turno['sexo'] = df_alunos_por_turno['sexo'].map({
        'M': 'Masculino',
        'F': 'Feminino'
    })

    alunosPorTurnoBar = px.bar(df_alunos_por_turno, x='cpf', y='turno',
                          title='Número de Alunos por Turno e Sexo',
                          labels={'cpf': 'Alunos','turno': 'Turno', 'sexo': 'Sexo:' },
                          color='sexo',
                          color_discrete_sequence=px.colors.qualitative.Vivid              
                          )
    
    alunosPorTurnoBarJSON = json.dumps(alunosPorTurnoBar, cls=plotly.utils.PlotlyJSONEncoder)
    
    df_alunos['idade'] = df_alunos['idade'].astype(int)                           
    mediaIdadePorCurso = df_alunos.groupby('curso').agg('idade').mean().reset_index().round(2)
    mediaIdadePorCursoBar = px.bar(mediaIdadePorCurso, 
                                  x='curso', 
                                  y='idade',
                                  title='Média de idade por curso',
                                  labels={'curso': 'Curso','idade': 'Média de Idade' },
                                  color='idade',
                                  color_discrete_sequence=px.colors.qualitative.Antique   
                                  )
    mediaIdadePorCursoJSON = json.dumps(mediaIdadePorCursoBar, cls=plotly.utils.PlotlyJSONEncoder)
                   
    return render_template("index.html", 
                          tittle="Alunos", 
                          alunosPorCursoPieJSON=alunosPorCursoPieJSON, 
                          alunosPorCursoBarJSON=alunosPorCursoBarJSON,
                          alunosPorTurnoPieJSON=alunosPorTurnoPieJSON, 
                          alunosPorTurnoBarJSON=alunosPorTurnoBarJSON,
                          mediaIdadePorCursoJSON=mediaIdadePorCursoJSON
                          )
  except Exception as e:
    return e
  
@app.route("/frequencia_alunos")
@cross_origin()
def frequencia_alunos():
  try:
    # Gráfico quantidade de alunos por dia
    fetch_frequencia_alunos="""
    SELECT a.cpf, a.nome, a.idade, a.sexo, a.celular, a.curso, a.turno, f.horario FROM aluno AS a INNER JOIN frequencia AS f ON a.cpf = f.cpf;
    """
    frequencia_alunos = db.fetch_data(query=fetch_frequencia_alunos)
    # for i in frequencia_alunos:
    #   print(i)
    #   exit()
    df_frequencia = pd.DataFrame(frequencia_alunos, columns=["cpf", "nome", "idade", "sexo", "celular", "curso", "turno", "dia"])
    df_frequencia['dia'] = df_frequencia['dia'].astype(str).str[:10]
    df_frequencia['cpf'] = df_frequencia['cpf'].astype(str)
    # print(df_freq)
    df_frequencia_alunos = df_frequencia.groupby(['dia'])['cpf'].count().reset_index()

    alunosPorDia = px.bar(df_frequencia_alunos, x='dia', y='cpf', 
                          title='Quantidade de Alunos por Dia',
                          labels={'dia': 'Dia','cpf': 'Alunos' },
                          color='cpf',
                          color_discrete_sequence=px.colors.qualitative.Pastel
                          
                          )
    alunosPorDiaJSON = json.dumps(alunosPorDia, cls=plotly.utils.PlotlyJSONEncoder)

    frequenciaPorCurso = df_frequencia['curso'].value_counts()
    frequenciaPorCursoPie = px.pie(df_frequencia, names=frequenciaPorCurso.index, values=frequenciaPorCurso.values, 
                          title='Porcentagem de Frequência por Curso',
                          color_discrete_sequence=px.colors.qualitative.Pastel              
                          )
    requenciaPorCursoPieJSON  = json.dumps(frequenciaPorCursoPie, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template("frequencia_alunos.html", 
                          tittle="Frequência", 
                          alunosPorDiaJSON=alunosPorDiaJSON,
                          requenciaPorCursoPieJSON=requenciaPorCursoPieJSON
                          )
  except Exception as e:
    return e
