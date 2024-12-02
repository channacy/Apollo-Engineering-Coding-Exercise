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
        return f"vin = {self.vin}, description = {self.description}, horse_power = {self.horse_power},model_name={self.model_name},model_year={self.model_year},purchase_price={self.purchase_price},fuel_type={self.fuel_type}"

@app.route('/')
def home():
    return jsonify({"message": "Successfully Connected!"}), 201

@app.route('/vehicle', methods=["GET"])
def get_vehicles():
    vehicles = Vehicle.query.all()
    vehicle_list = []
    for vehicle in vehicles:
        vehicle_list.append({
            'vin': vehicle.vin,
            'description': vehicle.description,
            'horse_power': vehicle.horse_power,
            'model_name': vehicle.model_name,
            'model_year': vehicle.model_year,
            'purchase_price': vehicle.purchase_price,
            'fuel_type': vehicle.fuel_type
        })
    return jsonify(vehicle_list), 200

@app.route('/vehicle/<int:vin>', methods=["GET"])
def get_vehicle(vin):
    vehicle = Vehicle.query.get_or_404(vin)
    if vehicle:
        return jsonify({
            'vin': vehicle.vin,
            'description': vehicle.description,
            'horse_power': vehicle.horse_power,
            'model_name': vehicle.model_name,
            'model_year': vehicle.model_year,
            'purchase_price': vehicle.purchase_price,
            'fuel_type': vehicle.fuel_type
        }), 200
    else:
        return "Vehicle not found.", 400

@app.route('/vehicle/<int:vin>', methods=["PUT"])
def update_vehicle(vin):
    try:
        data = request.get_json()
        vehicle = Vehicle.query.get_or_404(vin)
        if 'description' in data:
            vehicle.description = data.get('description')
        if 'horse_power' in data:
            vehicle.horse_power = data.get('horse_power')
        if 'model_name' in data:
            vehicle.model_name = data.get('model_name')
        if 'model_year' in data:
            vehicle.model_year = data.get('model_year')
        if 'purchase_price' in data:
            vehicle.purchase_price = data.get('purchase_price')
        if 'fuel_type' in data:
            vehicle.fuel_type = data.get('fuel_type')
        return "Vehicle updated succesfully.", 200
    except Exception as e:
        return jsonify({"Error": str(e)})

@app.route('/vehicle/<int:vin>', methods=["DELETE"])
def delete_vehicle(vin):
    try:
        vehicle = Vehicle.query.get_or_404(vin)
        db.session.delete(vehicle)
        db.session.commit()
        return jsonify("Success"), 204
    except Exception as e:
        return jsonify({"Error": str(e)}), 400

@app.route('/vehicle/<int:vin>', methods=["POST"])
def add_vehicle(vin):
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
            return jsonify({"error": "All fields are required"}), 422
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
    except Exception as e:
        return jsonify({"Error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)