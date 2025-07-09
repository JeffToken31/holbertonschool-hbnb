-- Creation of table USER
CREATE TABLE IF NOT EXISTS users (
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL,
    _password VARCHAR(128) NOT NULL,
    is_admin BOOLEAN,
    id VARCHAR(36) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME,
    PRIMARY KEY (id),
    UNIQUE (email)
);

-- Creation of place table
CREATE TABLE IF NOT EXISTS places (
    title VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    owner_id VARCHAR(36) NOT NULL,
    description VARCHAR(516),
    id VARCHAR(36) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY(owner_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Creation of amenity table
CREATE TABLE IF NOT EXISTS amenities(
    name VARCHAR(100) NOT NULL,
    id VARCHAR(36) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME,
    PRIMARY KEY (id)
);

-- Creation of place_amenity table relation many to many
CREATE TABLE IF NOT EXISTS place_amenity (
    place_id VARCHAR(36) NOT NULL,
    amenity_id VARCHAR(36) NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY(place_id) REFERENCES places (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(amenity_id) REFERENCES amenities (id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Creation of review table
CREATE TABLE IF NOT EXISTS reviews (
    text VARCHAR(516) NOT NULL,
    rating SMALLINT NOT NULL CHECK (
        rating BETWEEN 1
        AND 5
    ),
    place_id VARCHAR(128) NOT NULL,
    user_id VARCHAR(128) NOT NULL,
    id VARCHAR(36) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY(place_id) REFERENCES places (id) ON DELETE CASCADE,
    FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
);
