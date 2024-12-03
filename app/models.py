from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vehicle(db.Model):
    # Vehicle has vin, description, horse power, model name, model year, purchase price, fuel type
    vin = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    manufacturer = db.Column(db.Text)
    description = db.Column(db.Text)
    horse_power = db.Column(db.Integer)
    model_name = db.Column(db.Text)
    model_year = db.Column(db.Integer)
    purchase_price = db.Column(db.Float)
    fuel_type = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def to_dict(self):
        return {
            'vin': self.vin,
            'manufacturer': self.manufacturer,
            'description': self.description,
            'horse_power': self.horse_power,
            'model_name': self.model_name,
            'model_year': self.model_year,
            'purchase_price': self.purchase_price,
            'fuel_type': self.fuel_type,
        }
