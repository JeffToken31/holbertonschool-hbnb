-- Basics SELECT from tables on database development
SELECT
    first_name,
    email
FROM
    users
ORDER BY
    first_name;

SELECT
    title,
    price
FROM
    places
WHERE
    price < 120;

SELECT
    name
FROM
    amenities;

SELECT
    place_id
FROM
    place_amenity;

SELECT
    text,
    rating
FROM
    reviews;

-- Advanced SELECT with JOIN from tables on database development
SELECT
    first_name,
    last_name,
    title,
    price
FROM
    users
    JOIN places ON users.id = places.owner_id;

SELECT
    first_name,
    last_name,
    rating,
    text
FROM
    users
    JOIN reviews ON users.id = reviews.user_id;

SELECT
    first_name,
    title,
    rating,
    text
FROM
    users
    JOIN places ON users.id = places.owner_id
    JOIN reviews ON users.id = reviews.user_id;

SELECT
    title,
    name
FROM
    places
    JOIN place_amenity ON places.id = place_amenity.place_id
    JOIN amenities ON amenities.id = place_amenity.amenity_id
ORDER BY
    places.title;

-- UPDATE from tables on database development