# 📘 HBNB RESTful API Project

This project is a minimalist web backend for a simplified HBNB platform, built using Python and Flask. It follows a modular architecture, making the codebase clean, maintainable, and scalable. The application exposes RESTful API endpoints to manage users, places, reviews, and amenities.

---

## 🚀 How to Run the Project

1. Clone the project.`git clone https://github.com/JeffToken31/holbertonschool-hbnb`

2. (Optional) Create a virtual environment.`python -m venv venv`

    2.2 To activate on Linux/Mac: `source venv/bin/activate`

    2.3 To activate on Windows: `venv\Scripts\activate`

3. Install the dependencies with `pip install -r requirements.txt`.

4. Run the app using `python run.py`.

    By default, the server starts at `http://localhost:5000`.

---

## 🗂️ Project Structure and File Descriptions

### 👁️ Overview

You can view the project structure by running: `tree``:

```
.
└── hbnb
    ├── README.md
    ├── app
    │   ├── __init__.py
    │   ├── api
    │   │   ├── __init__.py
    │   │   └── v1
    │   │       ├── __init__.py
    │   │       ├── amenities.py
    │   │       ├── place.py
    │   │       ├── review.py
    │   │       └── users.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── amenities.py
    │   │   ├── baseModel.py
    │   │   ├── place.py
    │   │   ├── review.py
    │   │   └── users.py
    │   ├── persistence
    │   │   ├── __init__.py
    │   │   └── repository.py
    │   ├── services
    │   │   ├── __init__.py
    │   │   └── facade.py
    │   ├── test_models
    │   │   ├── test_all_models.py
    │   │   ├── test_amenity.py
    │   │   ├── test_place.py
    │   │   ├── test_review.py
    │   │   └── test_user.py
    │   └── tests
    │       ├── test_amenity.py
    │       ├── test_place.py
    │       └── test_user.py
    ├── config.py
    ├── requirements.txt
    └── run.py
```

### 📄 `README.md`

- This file.
 It explains how the project is structured and how to run it.

### 📄 `run.py`

- This is the **entry point** of the application. Run this file to start the server.
- It loads the configuration and launches the web server.

### 📄 `config.py`

- Contains configuration settings (like server port or debug mode).
- You can adjust this file if you want to change how the app runs.

### 📄 `requirements.txt`

- Lists all the Python packages the project needs.
- You install them using `pip install -r requirements.txt`.

---

## 📁 `app/` – Main Application Code

This folder holds all the logic for how the app works.

### 📄 `app/__init__.py`

- Tells Python that `app` is a package.
- Used to initialize things if needed when the app is loaded.

---

### 📁 `app/api/` – The API Routes (What the user can request)

This folder contains the files that define the available API endpoints (URLs the frontend or a user can call).

#### 📄 `app/api/__init__.py`

- Prepares the API module for usage.

#### 📁 `app/api/v1/`

- This is version 1 of the API.

Files inside:

- `amenities.py`: defines routes (GET, POST, etc.) for amenities (e.g. a swimming pool).
- `place.py`: defines routes related to places (e.g. homes or apartments).
- `review.py`: defines routes for handling user reviews.
- `users.py`: defines routes for user actions (create account, list users, etc.).
- `__init__.py`: groups all these files so they can be used together in the app.

### 📝 Snippet code of an API route (app/api/amenities.py)

```
@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload

        try:
            new_amenity = facade.create_amenity(amenity_data)
        except (TypeError, ValueError) as e:
            return {'error': str(e)}, 400
```

This code defines a POST endpoint to create a new amenity. It expects data matching amenity_model and returns appropriate HTTP responses depending on whether the creation succeeds or fails due to invalid data.

---

### 📁 `app/models/` – The Data Models (Python classes)

This is where you write your **Python classes** for each type of object in the app (called “models”).

Each file defines a class with attributes (like name, description, etc.) and methods (functions that the object can do).

Files inside:

- `baseModel.py`: defines the BaseModel class, a foundation for other models that provides unique IDs and timestamp management (creation and update times).
- `amenities.py`: defines the Amenity model (e.g. gym, Wi-Fi).
- `place.py`: defines the Place model (e.g. a house with location, price, etc.).
- `review.py`: defines the Review model (e.g. rating, comment).
- `users.py`: defines the User model (name, email, etc.).
- `__init__.py`: makes this folder a Python package.

### 📝 Snippet code of a data model (app/models/users.py)

````
if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        elif len(first_name) > 50:
            raise ValueError("first_name must be 50 characters max")
        else:
            self._first_name = first_name
````
Here’s a simpler version including the file reference:

This code from users.py checks that first_name is a string and not longer than 50 characters. If it isn’t, it raises an error to keep the data correct.

👉 You will **add methods** in these files (like `to_dict()`, `update()`, etc.) to define what each model can do.

---

### 📁 `app/persistence/` – Saving and Loading Data

This folder is for the **persistence layer**, meaning how data is stored and retrieved.

Files inside:

- `repository.py`: defines a `Repository` class with functions like `save()`, `get_by_id()`, `delete()`, etc.
- `InMemoryRepository` is a simple implementation that uses a Python dictionary to store objects in memory.
- `__init__.py`: just makes the folder a package.

### 📝 Snippet code of a persistence class (app/persistence/repository.py)
````
class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}

    def add(self, obj):
        self._storage[obj.id] = obj
````
This code from repository.py shows how objects are saved in memory using a dictionary. Each object is stored with its id as the key, making it easy to retrieve or update.

👉 This layer helps you keep the storage logic **separate** from your business logic and routes.

---

### 📁 `app/services/` – Application Logic (The Facade)

This is where the **main logic** of the app lives, between the API and the database.

Files inside:

- `facade.py`: this is the **central manager** of the app logic. It is implemented as a **singleton**, which means there is only **one shared instance** used throughout the app.
  This helps keep everything consistent (like handling all business rules in one place).

- `__init__.py`: makes the folder a Python package.

### 📝 Snippet code of a service function (app/services/facade.py)

```
def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found.")
        return place
```
This code from facade.py tries to find a place by its ID. If no place is found, it raises an error to let the system know the place doesn’t exist.

👉 The facade uses the repository to interact with the data, and it's used by the routes to perform actions.

---

## 🌐 API Endpoints

### 👤 Users

| Method | Endpoint                | Description             |
|--------|-------------------------|-------------------------|
| GET    | /api/v1/users           | List all users          |
| POST   | /api/v1/users           | Create a new user       |
| GET    | /api/v1/users/<user_id> | Get user details by ID  |
| PUT    | /api/v1/users/<user_id> | Modify user details     |

---

### 🏠 Places

| Method | Endpoint                 | Description             |
|--------|--------------------------|-------------------------|
| GET    | /api/v1/places           | Get all places          |
| POST   | /api/v1/places           | Add a new place         |
| GET    | /api/v1/places/<place_id>| Get place details by ID |
| PUT    | /api/v1/places/<place_id>| Update place details    |

---

### ⭐ Reviews

| Method | Endpoint                            | Description                        |
|--------|-----------------------------------|----------------------------------|
| GET    | /api/v1/reviews                   | List all reviews                  |
| POST   | /api/v1/reviews                   | Submit a new review               |
| GET    | /api/v1/reviews/<review_id>       | Get review details by ID          |
| PUT    | /api/v1/reviews/<review_id>       | Update review details             |
| DELETE | /api/v1/reviews/<review_id>       | Delete a review                   |
| GET    | /api/v1/places/<place_id>/reviews | List reviews for a specific place|

---

### 🚿 Amenities

| Method | Endpoint                      | Description               |
|--------|-------------------------------|---------------------------|
| GET    | /api/v1/amenities            | List all amenities        |
| POST   | /api/v1/amenities            | Add new amenity           |
| GET    | /api/v1/amenities/<amenity_id> | Get amenity details by ID|
| PUT    | /api/v1/amenities/<amenity_id> | Update amenity details   |

---
## 🔧 Technologies & Tools

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask--RESTx-lightgrey?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/REST%20API-005571?style=for-the-badge&logo=api&logoColor=white" />
  <img src="https://img.shields.io/badge/JSON-333333?style=for-the-badge&logo=json&logoColor=white" />
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white" />
  <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" />
</p>


## 🧪 Testing the Endpoints Using cURL

You can test your API routes using cURL in your terminal.
Here’s how to test user creation with valid data:

📤 Create a User
```
curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com"
}'
```

✅ Expected Response (Status: 200 OK)
```
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}


// 200 OK
```

## 🧪 Testing Invalid Data for a User

You can also test how the API handles invalid input data. Here’s an example where the user data is invalid (empty names and bad email):

📤 Create a User with Invalid Data

```
curl -X POST "http://127.0.0.1:5000/api/v1/users/" \
     -H "Content-Type: application/json" \
     -d '{
           "first_name": "",
           "last_name": "",
           "email": "invalid-email"
         }'
```

❌ Expected Response (Status: 400 Bad Request)

```
{
  "error": "Invalid input data"
}
```

## 📚 Swagger Documentation Access

When you start the server, visiting the base URL:

```
http://127.0.0.1:5000/
```
won’t show the API documentation — this is expected.

To access the Swagger UI, which documents and allows you to test all API endpoints, go to:
```
http://127.0.0.1:5000/api/v1/docs
```

This page is automatically generated by Flask-RESTx based on your API models and helps you explore the API, see request/response details, and try out endpoints interactively.

## 🔍 Running Unit Tests with unittest

You can run your unit tests using Python’s built-in **unittest** module. For example, to run the tests in the **test_amenity.py** file, use this command in your terminal:

```
python3 -m unittest app.tests.test_amenity
```
This will execute all test methods inside the TestAmenityEndpoints class (and any others in the file).

Here’s a sample test file for reference:

```
import unittest
from app import create_app

class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={"name": "wifi"})
        self.assertEqual(response.status_code, 201)

```

If your tests pass, you will see a message like this in the terminal:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.083s

OK
```

This means all tests ran successfully without errors.

## 🧠 Additional Notes

- All endpoints are under the `/api/v1` path.
- The code follows the structure:
  `routes (api)` → `facade (services)` → `repository (persistence)` → `models`.
- The facade is **singleton-based**: only one instance exists to handle logic, which helps avoid bugs and confusion.
- You can easily extend the project by adding new models, routes, or features.

## 🧑‍🏫 Authors

👨‍💻 Louis Manchon: https://github.com/LouisManchon

👨‍💻 Jeffrey Basset: https://github.com/JeffToken31
