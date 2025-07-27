# 📘 HBNB RESTful API Project

HBnB RESTful API is a lightweight Airbnb-like platform built as part of the Holberton School’s techno-level learning curriculum.
It showcases full-stack web development by combining a Flask-RESTx (Python) backend with a static frontend using HTML, CSS, and JavaScript.

The backend handles users, listings, reviews, and amenities through a RESTful API, powered by SQLite for persistent data storage.

The frontend communicates with this API to display places, handle user login, and allow authenticated users to post reviews.

A pre-filled database is provided for instant testing, so the platform is ready to explore as soon as you launch it.

🔗 Learn more about the Back-end: [Readme.md](https://github.com/JeffToken31/holbertonschool-hbnb/blob/main/part4/hbnb_back-end/README.md)

🔗 Learn more about the Front-end: [Readme.md](https://github.com/JeffToken31/holbertonschool-hbnb/blob/jeff/part4/hbnb_front-end/README.md)

## ⭐ Features

- **Homepage (`index.html`)**

  - Displays a **list of available places (listings)**.
  - Allows navigation to each place’s **detail page**.
  - Provides an option to **log in**.

- **Place Details Page (`place.html`)**

  - Shows detailed information about a place (price, host, description, etc.).
  - Displays **existing reviews**.
  - Provides an option to **log in**.
  - If the user is **logged in**, they can **add a review**.
  - If the user is **not logged in**, they are prompted to log in.

- **Login Page (`login.html`)**
  - Allows users to log in.
  - Includes a **logout system** to sign out.

## 🚀 How to Run the Project

1. Clone the project.`git clone https://github.com/JeffToken31/holbertonschool-hbnb`

2. (Optional) Create a virtual environment.`python -m venv venv`

   2.2 To activate on Linux/Mac: `source venv/bin/activate`

   2.3 To activate on Windows: `venv\Scripts\activate`

3. Install the dependencies:

   3.1 Move into `/hbnb_back-end`

   3.2 Run `pip install -r requirements.txt`

4. Initialize or refresh the database

   To creat/recreate the database:

   4.1 run `sqlite3 instance/development.db < sql/tables_creation.sql`

   To inisialize datas:

   4.2 run `sqlite3 instance/development.db < sql/developpedDatas.sql`

5. Run the app:

   5.1 Split terminal:

   5.1.1 Move into `/hbnb_back-end`

   5.1.2 Move into `/hbnb_front-end/`

   5.2 On back-end run `flask run`

   5.3 On front-end run port:3000 `python3 -m http.server 3000`

The back-end is disponible (swagger documentation):

`http://127.0.0.1:5000/api/v1/docs`

The front-end is disponible:

`http://127.0.0.1:3000/`

## 🔍 Available Users for Testing

Below is the list of pre-configured user accounts you can use to test the platform.  
All users (except the admin) share the same password.

- **Admin Account**

  - Email: `admin@hbnb.io`
  - Password: `admin1234`

- **Standard Users (Password: `user1234`)**
  - `alice@hbnb.io`
  - `bob@hbnb.io`
  - `claire@hbnb.io`
  - `david@hbnb.io`
  - `emma@hbnb.io`
  - `franck@hbnb.io`
  - `isabelle@hbnb.io`
  - `julien@hbnb.io`
  - `karine@hbnb.io`

## 👁️ Overview

You can view the project structure by running: `tree`:

```bash
$ tree
.
├── README.md
├── hbnb_back-end
│   ├── README.md
│   ├── app
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   └── v1
│   │   │       ├── __init__.py
│   │   │       ├── admin.py
│   │   │       ├── amenities.py
│   │   │       ├── auth.py
│   │   │       ├── place.py
│   │   │       ├── review.py
│   │   │       └── users.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── amenities.py
│   │   │   ├── baseModel.py
│   │   │   ├── place.py
│   │   │   ├── review.py
│   │   │   └── users.py
│   │   ├── persistence
│   │   │   ├── __init__.py
│   │   │   └── repository.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   └── facade.py
│   │   ├── test_models
│   │   │   ├── test_all_models.py
│   │   │   ├── test_amenity.py
│   │   │   ├── test_place.py
│   │   │   ├── test_review.py
│   │   │   └── test_user.py
│   │   └── tests
│   │       ├── test_amenity.py
│   │       ├── test_place.py
│   │       ├── test_review.py
│   │       └── test_user.py
│   ├── config.py
│   ├── extensions.py
│   ├── instance
│   │   └── development.db
│   ├── requirements.txt
│   ├── run.py
│   └── sql
│       ├── crud.sql
│       ├── developpedDatas.sql
│       ├── initial_datas.sql
│       ├── passwd_hasher.py
│       ├── tables_creation.sql
│       └── uuid_generator.py
└── hbnb_front-end
    ├── add_review.html
    ├── footer.html
    ├── index.html
    ├── js
    │   ├── api.js
    │   ├── footer.js
    │   ├── index.js
    │   ├── login.js
    │   ├── place.js
    │   └── utils.js
    ├── login.html
    ├── place.html
    └── styles.css
```

## 🔧 Technologies & Tools

<div>
    <p>Backend:</p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" />
        <img src="https://img.shields.io/badge/Flask--RESTx-lightgrey?style=for-the-badge&logo=flask&logoColor=white" />
        <img src="https://img.shields.io/badge/REST%20API-005571?style=for-the-badge&logo=api&logoColor=white" />
        <img src="https://img.shields.io/badge/JSON-333333?style=for-the-badge&logo=json&logoColor=white" />
    <p>Front-end:</p>
        <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
        <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
        <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
    <p>tools:</p>

<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white" />
<img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black" />
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"/>
<img src="https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>

</div>

## 🧑‍🏫 Authors

For back-end development:

👨‍💻 Louis Manchon: <https://github.com/LouisManchon>

👨‍💻 Jeffrey Basset: <https://github.com/JeffToken31>

For front-end development:

👨‍💻 Jeffrey Basset: <https://github.com/JeffToken31>
