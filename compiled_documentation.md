# 🏠 HBnB – Project Technical Documentation
## 📘 Introduction

This document is the technical guide for the **HBnB project**, which is a clone of the Airbnb platform.
It explains how the app is structured, how the different parts connect, and how it works step-by-step.
This documentation is here to guide the development and make sure everyone working on the project understands the system.

---
## 📦 High-Level Architecture
```mermaid
classDiagram
    %% Présentation
    class PresentationLayer {
        <<Interface>>
        +ServiceAPI
    }
    %% Domaine Métier
    class BusinessLogicLayer {
        +ServicesApp
        +UserService
        +PlaceService
        +ReviewService
        +AmenityService
    }
    %% Accès aux Données
    class PersistenceLayer {
        +DatabaseAccess
    }
    %% Relations
    PresentationLayer --> BusinessLogicLayer : Facade Pattern (via ServicesApp)
    BusinessLogicLayer --> PersistenceLayer : Database Operations
```
The app is organized into 3 main layers:
### 1. Presentation Layer
- This is where the app receives requests, usually through an API.
- It takes care of passing user inputs to the right part of the system.
- Main component: `ServiceAPI`, which talks to `ServicesApp`.
### 2. Business Logic Layer
- This is the brain of the system.
- It contains the rules and logic for users, places, reviews, amenities.
- It’s all managed through a central access point: `ServicesApp`.
- Each type of data (user, place, etc.) has its own service.
### 3. Persistence Layer
- This part communicates with the database.
- It stores and retrieves data through a single component: `DatabaseAccess`.
The whole structure is designed to keep responsibilities clean and separated.
All services go through `ServicesApp`, and only `DatabaseAccess` talks to the database.
---
## 🧠 Business Logic Layer – Class View
```mermaid
classDiagram
    class User {
        +int ID
        +string firstname
        +string lastname
        +string email
        +string password
        +string UUID
        +datetime date_create
        +datetime date_update
        +bool is_admin
        +void create_user()
        +void update_user()
        +void delete_user()
        +list<User> list()
    }
    class Place {
        +int ID
        +string title
        +string description
        +User owner
        +float price
        +float latitude
        +float longitude
        +list<Amenity> amenities
        +list<Review> reviews
        +datetime date_create
        +datetime date_update
        +void create_place()
        +void update_place()
        +void delete_place()
        +list<Place> list()
    }
    class Review {
        +int ID
        +Place place
        +User user
        +float rating
        +string comment
        +datetime date
        +datetime date_update
        +void create_review()
        +void update_review()
        +void delete_review()
        +list<Review> list()
    }
    class Amenity {
        +int ID
        +string name
        +string description
        +Place place
        +datetime date_create
        +void create_amenity()
        +void update_amenity()
        +void delete_amenity()
        +list<Amenity> list()
    }
    Place o-- User : Place needs User to be created (aggregation)
    Place o-- Amenity : Place has many Amenities (aggregation)
    Place o-- Review : Place receives Reviews (aggregation)
    Review --> Place : Review talks about one Place (association)
    Review --> User : Review written by a User (association)
    Amenity --> Place : Amenity linked to one Place (association)
```
### ⚙️ Main Components

- **`ServicesApp`**: Central access point for all services. It's like a control panel.
- **`UserService`**: Manages user registration and login.
- **`PlaceService`**: Handles everything related to places (create, update, list).
- **`ReviewService`**: Manages user reviews for places.
- **`AmenityService`**: Manages optional features like WiFi, kitchen, etc.
Each service handles its own type of data and talks to `DatabaseAccess` to save or get info.
There’s no inheritance or shared model — each service is built independently to keep things simple.
---
## 🔄 API Interaction Flow

Each of the following diagrams shows what happens during a specific API request.
We go step-by-step from user input to the system’s response.

---
### 1. User Registration
```mermaid
sequenceDiagram
participant User
participant API
participant BusinessFacade
participant BusinessLogic
participant Database
User->>API: Register (firstname, lastname, email, password)
API->>BusinessFacade: Forward Registration Request
BusinessFacade->>BusinessLogic: Validate and Process User Data
BusinessLogic->>Database: Insert New User Record
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>BusinessFacade: Return Status
BusinessFacade-->>API: Return Success or Error
API-->>User: Registration Confirmation
```
- The user fills out the registration form.
- The request goes to `ServiceAPI`, which sends it to `UserService` through `ServicesApp`.
- `UserService` processes the info and stores the user using `DatabaseAccess`.
- A response is sent back confirming the user is created.
---
### 2. Create a New Place
```mermaid
sequenceDiagram
participant User
participant API
participant BusinessFacade
participant BusinessLogic
participant Database
User->>API: Create Place (title, description, price, etc.)
API->>BusinessFacade: Forward Place Creation Request
BusinessFacade->>BusinessLogic: Validate and Process Place Data
BusinessLogic->>Database: Insert New Place Record
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>BusinessFacade: Return Status
BusinessFacade-->>API: Return Success or Error
API-->>User: Place Created Confirmation
```
- The user creates a new place by submitting data.
- `ServiceAPI` passes it to `PlaceService` via `ServicesApp`.
- `PlaceService` validates and saves the place.
- The system replies with a confirmation.
---
### 3. Add a Review
```mermaid
sequenceDiagram
participant User
participant API
participant BusinessFacade
participant BusinessLogic
participant Database
User->>API: Submit Review (place_id, rating, comment)
API->>BusinessFacade: Forward Review Submission
BusinessFacade->>BusinessLogic: Validate and Handle Review
BusinessLogic->>Database: Insert Review Record
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>BusinessFacade: Return Status
BusinessFacade-->>API: Return Confirmation
API-->>User: Review Submitted Successfully
```
- The user writes a review for a specific place.
- The API sends the info to `ReviewService`.
- The review is saved using `DatabaseAccess`.
- A response is returned to the user.
---
### 4. List Places
```mermaid
sequenceDiagram
participant User
participant API
participant BusinessFacade
participant BusinessLogic
participant Database
User->>API: Request List of Places (criteria)
API->>BusinessFacade: Forward Filtering Request
BusinessFacade->>BusinessLogic: Handle Filtering and Query
BusinessLogic->>Database: Query Matching Places
Database-->>BusinessLogic: Return Place List
BusinessLogic-->>BusinessFacade: Return Results
BusinessFacade-->>API: Send List
API-->>User: Display List of Places
```
- A user sends a request to search for available places.
- The API calls `PlaceService`.
- It queries the database and sends back a list of places that match the filters.
---
## ✅ Summary

This document gives a full view of how the HBnB project works behind the scenes.
We’ve seen how the system is split into layers, how services are organized, and how common requests are handled.
The idea is to keep the logic clean and modular, so it’s easier to maintain and extend later.
All the diagrams should now be used as a reference during development to stay aligned.
