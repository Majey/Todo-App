from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:ICUI4CU1997@localhost:5432/todoapp"
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self) -> str:
        return f"<Todo {self.id}, {self.description}>"

db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data = Todo.query.all())


