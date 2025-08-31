# In app.py (optional if already present)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/todo')
def todo_page():
    return render_template('todo.html')
