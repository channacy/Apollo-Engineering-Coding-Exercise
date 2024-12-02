from api import db
from sqlalchemy.sql import func

class Vehicle(db.Model):
    # Vehicle has vin, description, horse power, model name, model year, purchase price, fuel type
    vin = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column(db.Text)
    horse_power = db.Column(db.Integer)
    model_name = db.Column(db.Text)
    model_year = db.Column(db.Integer)
    purchase_price = db.Column(db.Real)
    fuel_type = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())