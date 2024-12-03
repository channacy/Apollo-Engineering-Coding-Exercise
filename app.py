import os
from flask import Flask, request, jsonify
from models import db, Vehicle

def create_app(app_config=None):
    basedir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__)

    if app_config:
        app.config.update(app_config)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route('/vehicle', methods=["GET"])
    def get_vehicles():
        try:
            vehicles = Vehicle.query.all()
            vehicle_list = []
            for vehicle in vehicles:
                vehicle_list.append(vehicle.to_dict())
            return jsonify(vehicle_list), 200
        except Exception as e:
            return jsonify({"Error": str(e)}), 400

    @app.route('/vehicle/<int:vin>', methods=["GET"])
    def get_vehicle(vin):
        try:
            vehicle = Vehicle.query.get_or_404(vin)
            if vehicle:
                return jsonify(vehicle.to_dict()), 200
            else:
                return jsonify({"Error": "Cannot find vehicle with specified vin."}), 422
        except Exception as e:
            return jsonify({"Error": str(e)}), 400

    @app.route('/vehicle/<int:vin>', methods=["PUT"])
    def update_vehicle(vin):
        try:
            data = request.get_json()
            vehicle = Vehicle.query.get(vin)
            if not vehicle:
                return jsonify({"Error": "Cannot find vehicle with specified vin."}), 422
            if 'manufacturer' in data:
                vehicle.manufacturer = data.get('manufacturer')
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
            db.session.commit()
            return jsonify(vehicle.to_dict()), 200
        except Exception as e:
            return jsonify({"Error": str(e)}), 400

    @app.route('/vehicle/<int:vin>', methods=["DELETE"])
    def delete_vehicle(vin):
        try:
            vehicle = Vehicle.query.get_or_404(vin)
            if not vehicle:
                return jsonify({"error": "Vehicle to delete not found."}), 422
            db.session.delete(vehicle)
            db.session.commit()
            return jsonify(vehicle.to_dict()), 204
        except Exception as e:
            return jsonify({"Error": str(e)}), 400

    @app.route('/vehicle', methods=["POST"])
    def add_vehicle():
        try:
            data = request.get_json()
            vin = data.get('vin')
            manufacturer = data.get('manufacturer')
            desc = data.get('description')
            horse_power = data.get('horse_power')
            model_name = data.get('model_name')
            model_year = data.get('model_year')
            purchase_price = data.get('purchase_price')
            fuel_type = data.get('fuel_type')
            if not desc or not horse_power or not model_name or not model_year or not purchase_price or not fuel_type:
                return jsonify({"error": "All fields: vin, manufacturer, description, horse_power, model_name, model_year, purchase_price, fuel_type are required to create new vehicle."}), 422
            vehicle = Vehicle(vin=vin, manufacturer=manufacturer, description=desc, horse_power=horse_power,
                              model_name=model_name, model_year=model_year, purchase_price=purchase_price, fuel_type=fuel_type)
            db.session.add(vehicle)
            db.session.commit()
            return jsonify(vehicle.to_dict()), 201
        except Exception as e:
            return jsonify({"Error": str(e)}), 400

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        print("Creating tables...")
        db.create_all()
    app.run(debug=True)
