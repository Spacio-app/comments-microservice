import os
from flask import Flask, render_template
from dotenv import load_dotenv
# importar funciones dentro del proyecto
from routes.comments import comments
from config.mongodb import mongo

load_dotenv()# carga el archivo .env

app = Flask(__name__)# indica si lo usa como punto de referecencia


app.config['MONGO_URI'] = os.getenv('MONGO_URI')# se obtiene la url de la base de datos
mongo.init_app(app)# se inicializa la base de datos

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(comments, url_prefix='/comments')# se registra la ruta de comments


if __name__ == '__main__':
    app.run(debug=True)