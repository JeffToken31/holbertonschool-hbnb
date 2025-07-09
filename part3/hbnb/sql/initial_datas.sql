-- Users creating (2)
INSERT INTO
    users (
        id,
        email,
        first_name,
        last_name,
        _password,
        is_admin,
        created_at,
        updated_at
    )
VALUES
    (
        '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
        'admin@hbnb.io',
        'Admin',
        'HBnB',
        '$2b$12$bDjkGHH7ffX.Ele.D/wsPuCZbpeteefipz7kngkJeX.efm5jTX1R2',
        TRUE,
        DATETIME('now'),
        DATETIME('now')
    ),
    (
        'ffe137ae-a992-4e47-9a2f-6ee8968eda33',
        'user@hbnb.io',
        'User',
        'HBnB',
        '$2b$12$R9WoSyaJrjoRYKvfms0CauZj/EsO/fOmzcK3OyKHhBJZXCFzb7YgG',
        False,
        DATETIME('now'),
        DATETIME('now')
    );

-- Amenities creating (3)
INSERT INTO
    amenities (id, name, created_at, updated_at)
VALUES
    (
        '34d0737f-c971-4cd7-8293-4675c4964d22',
        'WiFi',
        DATETIME('now'),
        DATETIME('now')
    ),
    (
        'd71dd64e-1a48-47c4-975a-3b7da1b5f641',
        'Swimming Pool',
        DATETIME('now'),
        DATETIME('now')
    ),
    (
        'a4953492-8ed2-46a8-a0ef-b0554bca2287',
        'Air Conditioning',
        DATETIME('now'),
        DATETIME('now')
    );

-- Places creating (2)
INSERT INTO
    places (
        id,
        title,
        description,
        price,
        latitude,
        longitude,
        owner_id,
        created_at,
        updated_at
    )
VALUES
    (
        '1fa1aed0-cc09-44ac-b14d-d1fd3e3b43cc',
        'Charming Loft in Paris',
        'A beautiful loft near Effel tower.',
        120.00,
        48.8867,
        2.3431,
        'ffe137ae-a992-4e47-9a2f-6ee8968eda33',
        DATETIME('now'),
        DATETIME('now')
    ),
    (
        '815bed53-0b21-4cdc-aa60-3e1712410832',
        'Rustik house',
        'A beautiful house in montain.',
        50.00,
        4.8756,
        56.5631,
        '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
        DATETIME('now'),
        DATETIME('now')
    );

-- place_amenity creating (2*2)
INSERT INTO
    place_amenity (place_id, amenity_id)
VALUES
    (
        '1fa1aed0-cc09-44ac-b14d-d1fd3e3b43cc',
        '34d0737f-c971-4cd7-8293-4675c4964d22'
    ),
    (
        '1fa1aed0-cc09-44ac-b14d-d1fd3e3b43cc',
        'a4953492-8ed2-46a8-a0ef-b0554bca2287'
    ),
    (
        '815bed53-0b21-4cdc-aa60-3e1712410832',
        '34d0737f-c971-4cd7-8293-4675c4964d22'
    ),
    (
        '815bed53-0b21-4cdc-aa60-3e1712410832',
        'd71dd64e-1a48-47c4-975a-3b7da1b5f641'
    );

-- Review creating (2)
INSERT INTO
    reviews (
        id,
        text,
        rating,
        user_id,
        place_id,
        created_at,
        updated_at
    )
VALUES
    (
        '49dc5e18-a8a6-4350-8d3a-c5119fcefd51',
        'Superb',
        5,
        '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
        '1fa1aed0-cc09-44ac-b14d-d1fd3e3b43cc',
        DATETIME('now'),
        DATETIME('now')
    ),
    (
        '4314ae23-aba4-4851-b4f4-c8cec4d720e2',
        'Just cool',
        3,
        'ffe137ae-a992-4e47-9a2f-6ee8968eda33',
        '815bed53-0b21-4cdc-aa60-3e1712410832',
        DATETIME('now'),
        DATETIME('now')
    );
