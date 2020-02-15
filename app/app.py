from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

from app import settings

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

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route("/todo/create", methods=['POST'])
def create_todo():
    description = request.get_json()['description']
    newTodo = Todo(description=description)
    db.session.add(newTodo)
    db.session.commit()
    return jsonify({
        'description': newTodo.description
   })

@app.route('/')
def index():
    return render_template("index.html", data=Todo.query.all())
