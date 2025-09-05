# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["ma_base"]  # nom de la base
collection = db["messages"]  # nom de la collection

@app.route('/')
def hello_world():
    collection.insert_one({"message": "Hello, World!"})
    last_message = collection.find().sort("_id", -1).limit(1)
    msg = next(last_message, {"message": "Hello, World!"})["message"]
    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)