from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from models import Vehicle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return jsonify({"message": "Successfully Connected!"}), 201

if __name__=='__main__':
    app.run(debug=True)

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404