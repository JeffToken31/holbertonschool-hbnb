import unittest
from app import create_app


class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={"name": "wifi"})
        self.assertEqual(response.status_code, 201)

    def test_amenity_invalid_data(self):
        response = self.client.post('/api/v1/amenities/', json={"name": ""})
        self.assertEqual(response.status_code, 400)

    def test_list_all_amenities(self):
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)

    def test_get_amenity_by_id(self):
        amenity = self.client.post('/api/v1/amenities/', json={"name": "jaccuzzi"})
        self.assertEqual(amenity.status_code, 201)
        amen = amenity.get_json()
        amenid = amen['id']
        response = self.client.get(f'/api/v1/amenities/{amenid}')
        self.assertEqual(response.status_code, 200)

    def test_get_amenity_without_id(self):
        response = self.client.get(f'/api/v1/amenities/amenid')
        self.assertEqual(response.status_code, 404)
