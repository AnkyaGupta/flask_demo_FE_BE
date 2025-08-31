
# In app.py (optional if already present)
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/todo')
def todo_page():
    return render_template('todo.html')


# Setup MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.items

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')
    
    if item_name and item_desc:
        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_desc
        })
        return "Item saved successfully!", 200
    else:
        return "Missing item name or description", 400

