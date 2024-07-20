from flask import Flask
from conection import db
from flask_restful import Api
from resource_1 import Employees

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql://Quickupuser:Bob0408@localhost/dbquickup"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS']= False 


@app.before_request
def criar_banco():
    db.create_all()

api.add_resource (Employees,'/emplooyes', '/emplooyes/<int:id>')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug = True)