# 📘 README – HBNB RESTful API Project

This project is a simple web backend built with Python. It uses a modular architecture to organize code clearly and make it easier to maintain and extend later. The app provides RESTful API endpoints for a simplified version of the HBNB platform.

---

## 🚀 How to Run the Project

1. Clone the project.`git clone https://github.com/JeffToken31/hbnb.git`

2. (Optional) Create a virtual environment.`python -m venv venv`

    2.2 To activate on Linux/Mac: `source venv/bin/activate`

    2.3 To activate on Windows: `venv\Scripts\activate`

3. Install the dependencies with `pip install -r requirements.txt`.

4. Run the app using `python run.py`.

    By default, the server starts at `http://localhost:5000`.

---

## 🗂️ Project Structure and File Descriptions

### 👁️ Overview

You can look at the project tree with command `tree`:

```txt
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
    │   │   ├── place.py
    │   │   ├── review.py
    │   │   └── users.py
    │   ├── persistence
    │   │   ├── __init__.py
    │   │   └── repository.py
    │   └── services
    │       ├── __init__.py
    │       └── facade.py
    ├── config.py
    ├── requirements.txt
    └── run.py
```

### 📄 `README.md`

- This file.
 It explains how the project is structured and how to run it.

### 📄 `run.py`

- This is the **main script**.
You run this file to start the application.
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

---

### 📁 `app/models/` – The Data Models (Python classes)

This is where you write your **Python classes** for each type of object in the app (called “models”).

Each file defines a class with attributes (like name, description, etc.) and methods (functions that the object can do).

Files inside:

- `amenities.py`: defines the Amenity model (e.g. gym, Wi-Fi).
- `place.py`: defines the Place model (e.g. a house with location, price, etc.).
- `review.py`: defines the Review model (e.g. rating, comment).
- `users.py`: defines the User model (name, email, etc.).
- `__init__.py`: makes this folder a Python package.

👉 You will **add methods** in these files (like `to_dict()`, `update()`, etc.) to define what each model can do.

---

### 📁 `app/persistence/` – Saving and Loading Data

This folder is for the **persistence layer**, meaning how data is stored and retrieved.

Files inside:

- `repository.py`: defines a `Repository` class with functions like `save()`, `get_by_id()`, `delete()`, etc.
- `__init__.py`: just makes the folder a package.

🧠 This layer helps you keep the storage logic **separate** from your business logic and routes.

---

### 📁 `app/services/` – Application Logic (The Facade)

This is where the **main logic** of the app lives, between the API and the database.

Files inside:

- `facade.py`: this is the **central manager** of the app logic.  
  ➕ It is implemented as a **singleton**, which means there is only **one shared instance** used throughout the app.  
  This helps keep everything consistent (like handling all business rules in one place).

- `__init__.py`: makes the folder a Python package.

The facade uses the repository to interact with the data, and it's used by the routes to perform actions.

---

## 🧠 Additional Notes

- All endpoints are under the `/api/v1` path.
- The code follows the structure:  
  `routes (api)` → `facade (services)` → `repository (persistence)` → `models`.
- The facade is **singleton-based**: only one instance exists to handle logic, which helps avoid bugs and confusion.
- You can easily extend the project by adding new models, routes, or features.

---
