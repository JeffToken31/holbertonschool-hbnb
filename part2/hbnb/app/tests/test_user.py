import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)
    
    def test_list_all_users(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
    
    def test_list_users_by_id(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jan",
            "last_name": "Goe",
            "email": "jan.goe@example.com"
        })
        self.assertEqual(user.status_code, 201)
        user_uniq = user.get_json()
        user_id = user_uniq['id']
        response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_list_user_by_invalid_id(self):
        response = self.client.get('/api/v1/users/abcdef')
        self.assertEqual(response.status_code, 404)

    def test_update_user(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Kan",
            "last_name": "Poe",
            "email": "kan.poe@example.com"
        })
        self.assertEqual(user.status_code, 201)
        user_uniq = user.get_json()
        user_id = user_uniq['id']
        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "Van",
            "last_name": "Poe",
            "email": "Van.poe@example.com"
        })
        self.assertEqual(response.status_code, 200)

    def test_update_user_not_found(self):
        response = self.client.put('/api/v1/users/user_id', json={
            "first_name": "Van",
            "last_name": "Poe",
            "email": "Van.poe@example.com"
        })
        self.assertEqual(response.status_code, 404)
    
    def test_update_user_invalide_data(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Pan",
            "last_name": "Moe",
            "email": "pan.moe@example.com"
        })
        self.assertEqual(user.status_code, 201)
        user_uniq = user.get_json()
        user_id = user_uniq['id']
        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "",
            "last_name": "zoe",
            "email": "example.com"
        })
        self.assertEqual(response.status_code, 400)

