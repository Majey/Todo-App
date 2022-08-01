from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from migrate import Migrate

app = Flask(__name__)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html', data = [
        {
        "description": "to do 1"
        },
        {
        "description": "to do 2"
        },
        {
        "description": "to do 3"
        },
        {
        "description": "to do 4"
        },
    ])


