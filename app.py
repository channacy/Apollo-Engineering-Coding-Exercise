import os
from flask import Flask, request, jsonify
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Vehicle(db.Model):
    # Vehicle has vin, description, horse power, model name, model year, purchase price, fuel type
    vin = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column(db.Text)
    horse_power = db.Column(db.Integer)
    model_name = db.Column(db.Text)
    model_year = db.Column(db.Integer)
    purchase_price = db.Column(db.Float)
    fuel_type = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"Vehicle(vin = {self.vin}, description = {self.description}, horse_power = {self.horse_power},model_name={self.model_name},model_year={self.model_year},purchase_price={self.purchase_price},fuel_type={self.fuel_type})"

@app.route('/')
def home():
    return jsonify({"message": "Successfully Connected!"}), 201

@app.route('/vehicle', methods=["GET"])
def get_vehicles():
    data = Vehicle.query.all()
    return jsonify([str(vehicle) for vehicle in data]), 201

@app.route('/vehicle/<int:vin>', methods=["POST"])
def get_vehicle(vin):
    try:
        data = request.get_json()
        vin = vin
        desc = data.get('description')
        horse_power = data.get('horse_power')
        model_name = data.get('model_name')
        model_year = data.get('model_year')
        purchase_price = data.get('purchase_price')
        fuel_type = data.get('fuel_type')
        if not desc or not horse_power or not model_name or not model_year or not purchase_price or not fuel_type:
            return jsonify({"error": "All fields are required"}), 400
        vehicle = Vehicle(vin=vin, description=desc, horse_power=horse_power,model_name=model_name, model_year=model_year,purchase_price=purchase_price, fuel_type=fuel_type)
        db.session.add(vehicle)
        db.session.commit()
        return jsonify({
            'vin': vin,
            'description': desc,
            'horse_power': horse_power,
            'model_name': model_name,
            'model_year': model_year,
            'purchase_price': purchase_price,
            'fuel_type': fuel_type
        }), 201
    except:
        return jsonify({"error": "Internal Server Error"}), 500

# @app.errorhandler(400)
# def bad_request(error):
#     return jsonify({'error': str(error)}), 400

# @app.errorhandler(404)
# def not_found(error):
#     return jsonify({'error': str(error)}), 404
if __name__ == '__main__':
    app.run(debug=True)