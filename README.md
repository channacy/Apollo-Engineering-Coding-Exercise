# Apollo-Engineering-Coding-Exercise

Instructions for creating and activating virtual environment on Mac/Linux
- `python3 -m venv .venv`
- `source ./.venv/bin/activate`

Instructions for creating and activating virtual environment on Windows
- `py -m venv venv`
- `source ./venv/bin/activate`

To deactivate a virtual environment:
- `deactivate`

To install the requirements:
- `pip install -r requirements.txt`

To run the app for the first time:
- `python app.py`

To start development server:
- `flask run`

To test the API via command line with cURL:
- `curl http://127.0.0.1:5000/vehicle`

To add a new vehicle:
- `curl -X POST http://127.0.0.1:5000/vehicle \-H "Content-Type: application/json" \-d '{"vin": 123456", description": "Sedan with sunroof", "manufacturer":"Tesla","horse_power": 180, "model_name": "Honda Civic", "model_year": 2022, "purchase_price": 25000.50, "fuel_type": "Gasoline"}'`

- To delete a vehicle:
`curl -X DELETE http://127.0.0.1:5000/vehicle/123456`

- To update a vehicle:
`curl -X PUT -H "Content-Type: application/json" -d '{"description":"updated!"}' http://127.0.0.1:5000/vehicle/123456`

