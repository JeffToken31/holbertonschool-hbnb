-- Remplissage initial de la base developpement.db
-- A exécuter avec : sqlite3 developpement.db < seed.sql

-- Vider les tables avant de remplir (pour éviter les doublons)
DELETE FROM reviews;
DELETE FROM place_amenity;
DELETE FROM amenities;
DELETE FROM places;
DELETE FROM users;

-- =========================================
-- 1. Insert users
-- Passwords: admin1234 (admin) / user1234 (regular users)
-- Pre-generated bcrypt hashes
-- =========================================
INSERT INTO users (id, first_name, last_name, email, _password, is_admin, created_at, updated_at) VALUES
('3f1e7d3c-6f91-4ec9-9c88-25c2096379d3', 'Admin', 'User', 'admin@example.com', '$2b$12$Bo8b4ahBSEtRXKJBQmymMuM/PEpL5RU4juP9VHH4awgoWr8VTD1d.', 1, DATETIME('now'), DATETIME('now')),
('4aef7b8d-1f4c-44a4-a936-8a00c156c7a1', 'Alice', 'Dupont', 'alice@example.com', '$2b$12$e1qs5bSZIVgeOum9YTxUhefyGTP1E6CrdVArfETvnX83RRu9JdEU6', 0, DATETIME('now'), DATETIME('now')),
('bbf83025-98d1-4e46-8ca3-7c2730f0922e', 'Bob', 'Martin', 'bob@example.com', '$2b$12$e1qs5bSZIVgeOum9YTxUhefyGTP1E6CrdVArfETvnX83RRu9JdEU6', 0, DATETIME('now'), DATETIME('now')),
('ca03e772-3622-45c8-bac2-b9833496ca4f', 'Claire', 'Moreau', 'claire@example.com', '$2b$12$e1qs5bSZIVgeOum9YTxUhefyGTP1E6CrdVArfETvnX83RRu9JdEU6', 0, DATETIME('now'), DATETIME('now')),
('37a7d3c0-cd0b-4d6f-bb5b-4f3bc2d6d0aa', 'David', 'Lemoine', 'david@example.com', '$2b$12$e1qs5bSZIVgeOum9YTxUhefyGTP1E6CrdVArfETvnX83RRu9JdEU6', 0, DATETIME('now'), DATETIME('now')),
('9b5fc19b-f5d1-4d8f-9e9a-cd688bf128f3', 'Emma', 'Petit', 'emma@example.com', '$2b$12$e1qs5bSZIVgeOum9YTxUhefyGTP1E6CrdVArfETvnX83RRu9JdEU6', 0, DATETIME('now'), DATETIME('now')),
('d2769c2e-bfc6-4d98-b9fc-27a7dfc9a215', 'Franck', 'Roche', 'franck@example.com', '$2b$12$e1qs5bSZIVgeOum9YTxUhefyGTP1E6CrdVArfETvnX83RRu9JdEU6', 0, DATETIME('now'), DATETIME('now')),
('61e78d96-54e0-4184-9bfc-fbc312f278db', 'Isabelle', 'Durand', 'isabelle@example.com', '$2b$12$e1qs5bSZIVgeOum9YTxUhefyGTP1E6CrdVArfETvnX83RRu9JdEU6', 0, DATETIME('now'), DATETIME('now')),
('e07eaf1e-97e2-4b07-b4a8-19e1c63edc87', 'Julien', 'Perrot', 'julien@example.com', '$2b$12$e1qs5bSZIVgeOum9YTxUhefyGTP1E6CrdVArfETvnX83RRu9JdEU6', 0, DATETIME('now'), DATETIME('now')),
('5f8d6f12-09e0-429a-bde1-c86a8e145e3a', 'Karine', 'Blanc', 'karine@example.com', '$2b$12$e1qs5bSZIVgeOum9YTxUhefyGTP1E6CrdVArfETvnX83RRu9JdEU6', 0, DATETIME('now'), DATETIME('now'));

-- =========================================
-- 2. Insert places (10 total)
-- =========================================
INSERT INTO places (id, title, price, latitude, longitude, owner_id, description, created_at, updated_at) VALUES
('6b2e54d8-8327-4f53-9f40-5b6bc796eb3d', 'Cozy downtown apartment', 75, 48.8566, 2.3522, '4aef7b8d-1f4c-44a4-a936-8a00c156c7a1', 'A comfortable apartment in Paris.', DATETIME('now'), DATETIME('now')),
('b1c38e23-1368-4c63-8f7b-2c7e07c8301b', 'Villa with swimming pool', 200, 43.2965, 5.3698, 'bbf83025-98d1-4e46-8ca3-7c2730f0922e', 'Beautiful villa with private pool.', DATETIME('now'), DATETIME('now')),
('c8a0e4ab-98ab-4d8c-bfb3-06510f6f6f9c', 'Student studio', 40, 45.7640, 4.8357, 'ca03e772-3622-45c8-bac2-b9833496ca4f', 'Small studio ideal for students.', DATETIME('now'), DATETIME('now')),
('fa0dcafd-6912-4c84-810e-7a5e779836b8', 'Family house', 120, 44.8378, -0.5792, '37a7d3c0-cd0b-4d6f-bb5b-4f3bc2d6d0aa', 'House with garden near the center.', DATETIME('now'), DATETIME('now')),
('f034b9b9-4ef0-4793-8bf4-9e6279a3c84d', 'Modern loft', 150, 43.6047, 1.4442, '9b5fc19b-f5d1-4d8f-9e9a-cd688bf128f3', 'Bright and modern loft.', DATETIME('now'), DATETIME('now')),
('010d4e05-c8d3-4b6b-929b-522e03ca7f72', 'Mountain chalet', 180, 45.9237, 6.8694, 'd2769c2e-bfc6-4d98-b9fc-27a7dfc9a215', 'Cozy chalet with a view.', DATETIME('now'), DATETIME('now')),
('7ae780fa-1a16-4a99-a109-3619f5d274a7', 'Rural cottage', 60, 47.2184, -1.5536, '61e78d96-54e0-4184-9bfc-fbc312f278db', 'Charming countryside cottage.', DATETIME('now'), DATETIME('now')),
('43f5e68b-e9b5-48c7-bd39-280178051e6d', 'Beach apartment', 90, 42.6976, 2.8954, 'e07eaf1e-97e2-4b07-b4a8-19e1c63edc87', 'Sea view and beach access.', DATETIME('now'), DATETIME('now')),
('a4c50ebd-37a0-4c70-9d6e-f4f9b721f8a3', 'Tiny house', 50, 44.9334, 4.8924, '5f8d6f12-09e0-429a-bde1-c86a8e145e3a', 'Small eco-friendly house.', DATETIME('now'), DATETIME('now')),
('d32826f8-9edb-4f6c-bb1a-34a2743f8b30', 'Luxury penthouse', 500, 48.1173, -1.6778, 'bbf83025-98d1-4e46-8ca3-7c2730f0922e', 'Penthouse with panoramic view.', DATETIME('now'), DATETIME('now'));
-- =========================================
-- 3. Insertion des amenities
-- =========================================
INSERT INTO amenities (id, name, created_at, updated_at) VALUES
('7bcf1b9a-68b9-4c58-8d0a-3b20a16287bf', 'WiFi', DATETIME('now'), DATETIME('now')),
('e2e3f47a-8e87-4ab7-8e12-658677a73288', 'Swimming pool', DATETIME('now'), DATETIME('now')),
('9e688679-0dc3-423a-bdb2-99a4d08c7ca0', 'Parking', DATETIME('now'), DATETIME('now')),
('251b1b63-52a6-41ca-bd12-fb91d3f7d5f0', 'Air conditioning', DATETIME('now'), DATETIME('now')),
('c345e8c7-bd54-4f89-b0b8-1b458f3d671e', 'Television', DATETIME('now'), DATETIME('now')),
('5eaf90f3-f5a2-4d14-8a0e-bec38a7592aa', 'Equipped kitchen', DATETIME('now'), DATETIME('now'));

-- =========================================
-- 4. Liaisons places - amenities (2-3 par place)
-- =========================================
INSERT INTO place_amenity (place_id, amenity_id) VALUES
('6b2e54d8-8327-4f53-9f40-5b6bc796eb3d', '7bcf1b9a-68b9-4c58-8d0a-3b20a16287bf'), -- WiFi
('6b2e54d8-8327-4f53-9f40-5b6bc796eb3d', 'c345e8c7-bd54-4f89-b0b8-1b458f3d671e'), -- TV

('b1c38e23-1368-4c63-8f7b-2c7e07c8301b', 'e2e3f47a-8e87-4ab7-8e12-658677a73288'), -- Piscine
('b1c38e23-1368-4c63-8f7b-2c7e07c8301b', '9e688679-0dc3-423a-bdb2-99a4d08c7ca0'), -- Parking

('c8a0e4ab-98ab-4d8c-bfb3-06510f6f6f9c', '7bcf1b9a-68b9-4c58-8d0a-3b20a16287bf'), -- WiFi
('c8a0e4ab-98ab-4d8c-bfb3-06510f6f6f9c', '251b1b63-52a6-41ca-bd12-fb91d3f7d5f0'), -- Clim

('fa0dcafd-6912-4c84-810e-7a5e779836b8', '9e688679-0dc3-423a-bdb2-99a4d08c7ca0'), -- Parking
('fa0dcafd-6912-4c84-810e-7a5e779836b8', 'c345e8c7-bd54-4f89-b0b8-1b458f3d671e'), -- TV

('f034b9b9-4ef0-4793-8bf4-9e6279a3c84d', '7bcf1b9a-68b9-4c58-8d0a-3b20a16287bf'), -- WiFi
('f034b9b9-4ef0-4793-8bf4-9e6279a3c84d', '5eaf90f3-f5a2-4d14-8a0e-bec38a7592aa'), -- Cuisine

('010d4e05-c8d3-4b6b-929b-522e03ca7f72', 'e2e3f47a-8e87-4ab7-8e12-658677a73288'), -- Piscine
('010d4e05-c8d3-4b6b-929b-522e03ca7f72', '251b1b63-52a6-41ca-bd12-fb91d3f7d5f0'), -- Clim

('7ae780fa-1a16-4a99-a109-3619f5d274a7', '7bcf1b9a-68b9-4c58-8d0a-3b20a16287bf'), -- WiFi
('7ae780fa-1a16-4a99-a109-3619f5d274a7', '9e688679-0dc3-423a-bdb2-99a4d08c7ca0'), -- Parking

('43f5e68b-e9b5-48c7-bd39-280178051e6d', 'c345e8c7-bd54-4f89-b0b8-1b458f3d671e'), -- TV
('43f5e68b-e9b5-48c7-bd39-280178051e6d', '5eaf90f3-f5a2-4d14-8a0e-bec38a7592aa'), -- Cuisine

('a4c50ebd-37a0-4c70-9d6e-f4f9b721f8a3', '7bcf1b9a-68b9-4c58-8d0a-3b20a16287bf'), -- WiFi
('a4c50ebd-37a0-4c70-9d6e-f4f9b721f8a3', '251b1b63-52a6-41ca-bd12-fb91d3f7d5f0'); -- Clim

-- =========================================
-- 5. Insertion des reviews
-- =========================================
INSERT INTO reviews (id, user_id, place_id, rating, text, created_at, updated_at) VALUES
('52e2c9b6-4ed3-4f10-9d59-8c3c7b1f7760', 'bbf83025-98d1-4e46-8ca3-7c2730f0922e', '6b2e54d8-8327-4f53-9f40-5b6bc796eb3d', 5, 'Great stay, I recommend!', DATETIME('now'), DATETIME('now')),
('0dc939d4-76d2-4f51-b4aa-8cde8a1231a1', 'ca03e772-3622-45c8-bac2-b9833496ca4f', 'b1c38e23-1368-4c63-8f7b-2c7e07c8301b', 4, 'Very beautiful villa, amazing pool.', DATETIME('now'), DATETIME('now')),
('e6e27c7f-0c18-49e7-9b3a-b6a67b182af2', '37a7d3c0-cd0b-4d6f-bb5b-4f3bc2d6d0aa', 'c8a0e4ab-98ab-4d8c-bfb3-06510f6f6f9c', 3, 'Decent studio for the price.', DATETIME('now'), DATETIME('now')),
('a1bc07e7-23d4-4a5e-bb42-d2e3a97a61a5', '9b5fc19b-f5d1-4d8f-9e9a-cd688bf128f3', 'fa0dcafd-6912-4c84-810e-7a5e779836b8', 5, 'Perfect house for the family.', DATETIME('now'), DATETIME('now')),
('42b0b92d-4c5c-4a84-9e64-2984e0f0e5db', 'd2769c2e-bfc6-4d98-b9fc-27a7dfc9a215', 'f034b9b9-4ef0-4793-8bf4-9e6279a3c84d', 4, 'Modern loft, well located.', DATETIME('now'), DATETIME('now')),
('6c50efc0-b6f9-462f-b58d-8a27f78495a4', '61e78d96-54e0-4184-9bfc-fbc312f278db', '010d4e05-c8d3-4b6b-929b-522e03ca7f72', 5, 'Beautiful chalet, very quiet.', DATETIME('now'), DATETIME('now')),
('b42ffb8c-80f8-4f06-a531-8d8bfb384ae1', 'e07eaf1e-97e2-4b07-b4a8-19e1c63edc87', '7ae780fa-1a16-4a99-a109-3619f5d274a7', 3, 'Pleasant cottage but a bit isolated.', DATETIME('now'), DATETIME('now')),
('b3a4e7f1-9b99-4f6d-9c2c-1b462e6e92d0', '5f8d6f12-09e0-429a-bde1-c86a8e145e3a', '43f5e68b-e9b5-48c7-bd39-280178051e6d', 5, 'Apartment with superb view.', DATETIME('now'), DATETIME('now')),
('cde3b5e9-13e1-4b98-b1f8-8364b3c7e7fa', 'bbf83025-98d1-4e46-8ca3-7c2730f0922e', 'a4c50ebd-37a0-4c70-9d6e-f4f9b721f8a3', 4, 'Charming tiny house.', DATETIME('now'), DATETIME('now')),
('a24d5c34-5a1b-44f2-8322-1981c7852ca3', '4aef7b8d-1f4c-44a4-a936-8a00c156c7a1', 'd32826f8-9edb-4f6c-bb1a-34a2743f8b30', 5, 'Luxury penthouse, incredible experience.', DATETIME('now'), DATETIME('now'));
