-- Basics SELECT from tables on database development
SELECT
    first_name,
    email,
    _password
FROM
    users
WHERE
    is_admin = TRUE;

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
UPDATE
    users
SET
    email = 'new@email.test'
WHERE
    first_name = 'User';

SELECT
    email
FROM
    users
WHERE
    first_name = 'User';

UPDATE
    places
SET
    price = 400
WHERE
    title = 'Rustik house';

SELECT
    price
FROM
    places
WHERE
    title = 'Rustik house';

UPDATE
    amenities
SET
    name = 'Jacuzzi'
WHERE
    name = 'Swimming Pool';

SELECT
    name,
    place_id,
    title
FROM
    amenities
    JOIN place_amenity ON places.id = place_amenity.place_id
    JOIN places ON places.id = place_amenity.place_id
WHERE
    name = 'Jacuzzi'
GROUP BY
    places.title;

-- DELETE from tables on database development
DELETE FROM
    reviews
WHERE
    id = '4314ae23-aba4-4851-b4f4-c8cec4d720e2';

SELECT
    *
FROM
    reviews;

DELETE FROM
    users
WHERE
    first_name = 'User';

SELECT
    first_name,
    title
FROM
    users
    JOIN places ON places.owner_id = users.id;