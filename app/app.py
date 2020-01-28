from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from app import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgres://postgres:docker@db:5432/todo'
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
    description = request.form.get('description', '')
    newTodo = Todo(description=description)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template("index.html", data=Todo.query.all())
