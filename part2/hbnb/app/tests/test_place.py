import unittest
from app import create_app

class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_place(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(user.status_code, 201)
        amenity = self.client.post('/api/v1/amenities/', json={"name": "wifi"})
        self.assertEqual(amenity.status_code, 201)

        data_user = user.get_json()
        user_id = data_user['id']

        data_amenity = amenity.get_json()
        amenity_id = data_amenity['id']

        place = self.client.post('/api/v1/places/', json={
            "title": "string",
            "description": "string",
            "price": 10.0,
            "latitude": 10.0,
            "longitude": 10.0,
            "owner_id": user_id,
            "amenities": [amenity_id]
            })
        self.assertEqual(place.status_code, 201)
    
    def test_create_place_invalid_data(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jankkje",
            "last_name": "Doke",
            "email": "je.doe@example.com"
        })
        self.assertEqual(user.status_code, 201)
        amenity = self.client.post('/api/v1/amenities/', json={"name": "wifi"})
        self.assertEqual(amenity.status_code, 201)

        data_user = user.get_json()
        user_id = data_user['id']

        data_amenity = amenity.get_json()
        amenity_id = data_amenity['id']

        place = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "string",
            "price": -110.0,
            "latitude": 110.0,
            "longitude": 1110.0,
            "owner_id": user_id,
            "amenities": [amenity_id]
            })
        self.assertEqual(place.status_code, 400)

    def test_list_all_place(self):
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)
    
    def test_list_place_by_id(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "pane",
            "last_name": "joe",
            "email": "jane.oe@exale.co"
        })
        self.assertEqual(user.status_code, 201)
        amenity = self.client.post('/api/v1/amenities/', json={"name": "wifi"})
        self.assertEqual(amenity.status_code, 201)

        data_user = user.get_json()
        user_id = data_user['id']

        data_amenity = amenity.get_json()
        amenity_id = data_amenity['id']

        place = self.client.post('/api/v1/places/', json={
            "title": "string",
            "description": "string",
            "price": 10.0,
            "latitude": 10.0,
            "longitude": 10.0,
            "owner_id": user_id,
            "amenities": [amenity_id]
            })
        self.assertEqual(place.status_code, 201)

        data_place = place.get_json()
        place_id = data_place['id']
        response = self.client.get(f'/api/v1/places/{place_id}')
        self.assertEqual(response.status_code, 200)

    def test_place_list_by_invalid_id(self):
        response = self.client.get('/api/v1/places/abcdef')
        self.assertEqual(response.status_code, 404)

    def test_update_place(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jankkje",
            "last_name": "Doke",
            "email": "jiuge.doe@examykyyple.com"
        })
        self.assertEqual(user.status_code, 201)
        amenity = self.client.post('/api/v1/amenities/', json={"name": "wifi"})
        self.assertEqual(amenity.status_code, 201)

        data_user = user.get_json()
        user_id = data_user['id']

        data_amenity = amenity.get_json()
        amenity_id = data_amenity['id']

        place = self.client.post('/api/v1/places/', json={
            "title": "string",
            "description": "string",
            "price": 10.0,
            "latitude": 10.0,
            "longitude": 10.0,
            "owner_id": user_id,
            "amenities": [amenity_id]
            })
        self.assertEqual(place.status_code, 201)

        data_place = place.get_json()
        place_id = data_place['id']

        response = self.client.put(f'/api/v1/places/{place_id}', json={
            "title": "coucou",
            "description": "string",
            "price": 10.0,
            "latitude": 50.0,
            "longitude": 10.0,
            "owner_id": user_id,
            "amenities": [amenity_id]
            })
        self.assertEqual(response.status_code, 200)


    def test_update_place_not_found(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jankkopje",
            "last_name": "Doke",
            "email": "jiuge.e@examykyyple.com"
        })
        self.assertEqual(user.status_code, 201)
        amenity = self.client.post('/api/v1/amenities/', json={"name": "wifi"})
        self.assertEqual(amenity.status_code, 201)

        data_user = user.get_json()
        user_id = data_user['id']

        data_amenity = amenity.get_json()
        amenity_id = data_amenity['id']

        place = self.client.post('/api/v1/places/', json={
            "title": "strinug",
            "description": "strging",
            "price": 10.0,
            "latitude": 20.0,
            "longitude": 10.0,
            "owner_id": user_id,
            "amenities": [amenity_id]
            })
        self.assertEqual(place.status_code, 201)

        data_place = place.get_json()
        place_id = data_place['id']
        response = self.client.put(f'/api/v1/places/{place_id}', json={
            "title": "string",
            "description": "string",
            "price": 10.0,
            "latitude": 10.0,
            "longitude": 1110.0,
            "owner_id": user_id,
            "amenities": []
        })
        self.assertEqual(response.status_code, 404)
    
    def test_update_place_invalide_data(self):
        response = self.client.put('/api/v1/places/sdqsd', json={
            "title": "",
            "description": "",
            "price": -100,
            "latitude": 999.9,
            "longitude": "not",
            "owner_id": "invalid",
            "amenities": "not"
        })
        self.assertEqual(response.status_code, 404)