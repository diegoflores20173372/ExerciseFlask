import traceback
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///dojo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Dojo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_dojo = db.Column(db.String(128), nullable=False)
    aforo_dojo = db.Column(db.Integer, nullable=False)
    fecha_creacion_dojo = db.Column(db.DateTime, nullable=False)
    localizacion_dojo = db.Column(db.String(255), nullable=False)
    caracteristicas_dojo = db.Column(db.PickleType)
    dojo_activo = db.Column(db.Boolean, nullable=False)
    comentario_dojo = db.Column(db.String(255))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        nuevo_dojo = Dojo()
        
        nuevo_dojo.nombre_dojo = request.form["nombre"]
        nuevo_dojo.aforo_dojo = request.form["aforo"]
        split_fecha = request.form["fecha"].split(sep="-")
        nuevo_dojo.fecha_creacion_dojo = datetime(int(split_fecha[0]), int(split_fecha[1]), int(split_fecha[2]))
        nuevo_dojo.localizacion_dojo = request.form['dojoLocation']
        nuevo_dojo.caracteristicas_dojo = request.form.getlist('caracteristicasDojo')
        nuevo_dojo.dojo_activo = bool(request.form['estadoDojo'])
        nuevo_dojo.comentario_dojo = request.form['comentarioDojo']

        
        try:
            db.session.add(nuevo_dojo)
            db.session.commit()
            return result()
        except:
            print(traceback.format_exc())
            return 'Problemas al insertar en la Base de Datos'
    else:
        return redirect(url_for('index'))

@app.route('/result')
def result():
    dojo = Dojo.query.order_by(Dojo.id)[-1]
    return render_template('result.html', dojo = dojo)

if __name__ == "__main__":
    app.run(debug=True)