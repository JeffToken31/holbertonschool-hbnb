## Introduction

This project is a mock application designed to manage users, places, amenities, and reviews.  
A class diagram is used to represent the structure of the project, including the different classes, their attributes, methods, and the relationships between them.  
The goal is to establish a clear data model using concepts such as inheritance, aggregation, composition, and association.

---

## Class Documentation

### 👤 User

**Attributes**

- `ID`  
- `firstname`  
- `lastname`  
- `email`  
- `password`  
- `UUID`  
- `date_create`  
- `date_update`  
- `is_admin`  

**Methods**

- `create_user()`  
- `update_user()`  
- `delete_user()`  
- `list()`  

**Relationships**

- A **User** owns one or more **Places**.  
- A **User** writes **Reviews**.  

---

### 📍 Place

**Attributes**

- `ID`
- `title`
- `description`
- `owner`
- `price`
- `latitude`
- `longitude`
- `amenities`
- `reviews`

**Methods**

- `create_place()`
- `update_place()`
- `delete_place()`
- `list()`

**Relationships**

- A **Place** needs a **User** to be created (**aggregation**).
- A **Place** can include multiple **Reviews** (**aggregation**).
- A **Place** can have **Amenities** (**aggregation**).

---

### ⭐ Amenity

**Attributes**

- `ID`
- `name`
- `description`
- `place`
- `date_create`

**Methods**

- `create_amenity()`
- `update_amenity()`
- `delete_amenity()`
- `list()`

**Relationships**

- An **Amenity** needs a **Place** to exist (**composition**).

---

### 📝 Review

**Attributes**

- `ID`
- `place`
- `user`
- `rating`
- `comment`
- `date`

**Methods**

- `create_review()`
- `update_review()`
- `delete_review()`
- `list()`

**Relationships**

- A **Review** is linked to a **Place**.
- A **Review** is written by a **User**.

---

## Class Diagram (Mermaid)

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

## Conclusion

The diagram provides a visual overview of the main entities in the project and the logical connections between them.
This modeling lays the foundation for development by ensuring a consistent and well-structured design.
It represents an important first step before implementing the application's features in code.