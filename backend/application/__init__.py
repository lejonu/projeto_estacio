from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
from application import routes
