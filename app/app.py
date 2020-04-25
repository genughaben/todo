import os, sys
from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import app.settings

app = Flask(__name__)

local = True
if 'LOCAL' in os.environ:
    if os.environ['LOCAL'] == 'True':
        local = True
    else:
        local = False

outside_docker_postgres = 'postgres://postgres:docker@localhost:5432/todo'
inside_docker_postgres = 'postgres://postgres:docker@db:5432/todo'

if(local):
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
        return f'<Todo {self.id} {self.description} {self.completed}>'


@app.route('/')
def index():
    return render_template("index.html", data=Todo.query.order_by('id').all())


@app.route("/todo/create", methods=['POST'])
def create_todo():
    print('whats up?')
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
    return jsonify(body)


@app.route("/todo/<todo_id>/set-completed", methods=['POST'])
def set_todo_completed(todo_id):
    error = False
    try:
        new_completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = new_completed
        db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(500)
    if not error:
        return redirect(url_for('index'))


@app.route("/todo/<todo_id>/delete", methods=['DELETE'])
def delete_todo(todo_id):
    error = False
    try:
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(500)
    if not error:
        return jsonify({"success": True })


