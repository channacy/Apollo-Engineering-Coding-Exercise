
# Apollo Engineering Coding Exercise - 🚗 Vehicle CRUD API

A CRUD Representational State Transfer (REST) API designed to create, read, update, delete vehicle information. 

Each vehicle has a unique vin number (also serving as primary key), manufacturer name, description, horse power, model name, model year, purchase price, fuel type, and a created_at datetime.

Tools: Flask, SQLAlchemy, SQLite, PyTest, cURL

## Installation

1. Clone the project

```bash
  git clone https://github.com/channacy/Apollo-Engineering-Coding-Exercise.git
```

2. Create Virtual Environment

Instructions for creating and then activating virtual environment:

Mac/Linux
```bash
python3 -m venv .venv
source ./.venv/bin/activate
```

Windows
```bash 
py -m venv venv
source ./.venv/bin/activate
```
    
To deactivate a virtual environment:
```bash
deactivate
```

3. Install requirements

```bash
pip install -r requirements.txt
```

4. Run the app
```bash
python app.py
```

## API Reference

#### GET

```http
curl http://127.0.0.1:5000/vehicle/<optional-id-for-one-vehicle>
```

| Method | Response Status | Description                |
| :-------- | :------- | :------------------------- |
| `GET` | `200 OK` | Gets all the vehicles |

#### POST

```http
  curl -X POST http://127.0.0.1:5000/vehicle \-H "Content-Type: application/json" \-d '{"vin": 123456, "description": "Sedan with sunroof", "manufacturer":"Tesla","horse_power": 180, "model_name": "Honda Civic", "model_year": 2022, "purchase_price": 25000.50, "fuel_type": "Gasoline"}'
```

| Method | Response Status     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `POST`      | `201 Created` | **Required**. Id of item to fetch |


#### DELETE

```http
curl -X DELETE http://127.0.0.1:5000/vehicle/123456
```

| Method | Response Status | Description                |
| :-------- | :------- | :------------------------- |
| `DELETE` | `204 No Content` | Deletes a vehicle |

#### UPDATE

```http
curl -X PUT -H "Content-Type: application/json" -d '{"description":"updated!"}' http://127.0.0.1:5000/vehicle/123456
```

| Method | Response Status | Description                |
| :-------- | :------- | :------------------------- |
| `PUT` | `200 OK` | Updates a vehicle |

## Running Tests

To run tests, run the following command

```bash
cd app/tests
pytest
```

## Example Usage
<img width="853" alt="Screenshot 2024-12-04 at 12 30 16 PM" src="https://github.com/user-attachments/assets/61888397-22d5-46af-8987-774ac6dfa273">
<img width="1030" alt="Screenshot 2024-12-04 at 12 58 41 PM" src="https://github.com/user-attachments/assets/d86908d3-0d94-4656-90c7-0ce82d7609ea">
<img width="1045" alt="Screenshot 2024-12-04 at 12 30 35 PM" src="https://github.com/user-attachments/assets/ba6aaafa-f7a4-415e-8d17-02ca45a0f61b">
<img width="1023" alt="Screenshot 2024-12-04 at 12 56 22 PM" src="https://github.com/user-attachments/assets/53d797d5-21c5-4f22-bb81-c367bcca9783">

## Resources

[Test Your Python Project](https://openclassrooms.com/en/courses/7747411-test-your-python-project/7894396-create-tests-for-the-flask-framework-using-pytest-flask)
[Testing a Flask framework with Pytest](https://circleci.com/blog/testing-flask-framework-with-pytest/)