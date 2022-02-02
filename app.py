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
    caracteristicas_dojo = db.Column(db.PickleType, nullable=False)
    dojo_activo = db.Column(db.Boolean, nullable=False)
    comentario_dojo = db.Column(db.String(255), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        nuevo_dojo = Dojo()
        
        nuevo_dojo.nombre_dojo = request.form["name"]
        nuevo_dojo.aforo_dojo = request.form["cellphone"]
        nuevo_dojo.fecha_creacion_dojo = '10-10-2010'
        nuevo_dojo.localizacion_dojo = request.form['dojoLocation']
        nuevo_dojo.caracteristicas_dojo = ["limpio", "ordenado", "nuevo"]
        nuevo_dojo.dojo_activo = True
        nuevo_dojo.comentario_dojo = request.form['comentarioDojo']

        try:
            db.session.add(nuevo_dojo)
            db.session.commit()
            return redirect(url_for(result))
        except:
            return 
    else:
        return redirect(url_for(index))

@app.route('/result')
def result():
    dojos = Dojo.query.order_by(Dojo.id).first()
    return render_template('result.html', dojos = dojos)

if __name__ == "__main__":
    app.run(debug=True)