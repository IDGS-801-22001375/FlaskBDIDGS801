from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

from config import DevelopmentConfig
from models import db, Alumnos
from maestros.routes import maestros
from alumnos.routes import alumnos
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(maestros)
app.register_blueprint(alumnos)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
	csrf.init_app(app)
	app.run(port=5002, debug=True)