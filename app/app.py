from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import os, sys
from flask_migrate import Migrate

import settings

app = Flask(__name__)
local = env_var = os.environ['LOCAL']
outside_docker_postgres = 'postgres://postgres:docker@localhost:5432/todo'
inside_docker_postgres = 'postgres://postgres:docker@db:5432/todo'
if(local == 'true'):
    app.config['SQLALCHEMY_DATABASE_URI'] = outside_docker_postgres
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = inside_docker_postgres

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

@app.route("/todo/create", methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        newTodo = Todo(description=description)
        db.session.add(newTodo)
        db.session.commit()
        body['description'] = newTodo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(400)
    if not error:
        return jsonify(body)



@app.route('/')
def index():
    return render_template("index.html", data=Todo.query.all())
