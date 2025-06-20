import unittest
from app import create_app


class TestReviewEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_review(self):
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
        data_place = place.get_json()
        place_id = data_place['id']

        review = self.client.post('/api/v1/reviews/', json={
            "text": "sifrng",
            "rating": 3,
            "user": user_id,
            "place": place_id
            })
        self.assertEqual(review.status_code, 201)

    def test_create_review_invalid_data(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.poe@example.com"
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

        review = self.client.post('/api/v1/reviews/', json={
            "text": "",
            "rating": 0,
            "user": user_id,
            "place": place_id
            })
        self.assertEqual(review.status_code, 400)

    def test_list_all_review(self):
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)

    def test_list_review_by_id(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@exaiugmple.com"
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

        review = self.client.post('/api/v1/reviews/', json={
            "text": "sifrng",
            "rating": 3,
            "user": user_id,
            "place": place_id
            })
        self.assertEqual(review.status_code, 201)

        data_review = review.get_json()
        review_id = data_review['id']
        response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)

    def test_list_review_by_invalid_id(self):
        response = self.client.get(f'/api/v1/reviews/abc')
        self.assertEqual(response.status_code, 404)

    def test_update_review(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@exasqcmple.com"
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

        review = self.client.post('/api/v1/reviews/', json={
            "text": "sifrng",
            "rating": 3,
            "user": user_id,
            "place": place_id
            })
        self.assertEqual(review.status_code, 201)

        data_review = review.get_json()
        review_id = data_review['id']
        response = self.client.put(f'/api/v1/reviews/{review_id}', json={
            "text": "sifdscg",
            "rating": 5,
            "user": user_id,
            "place": place_id
            })
        self.assertEqual(response.status_code, 200)

    def test_update_review_not_found(self):
        response = self.client.put(f'/api/v1/reviews/abc', json={
            "text": "sifdscg",
            "rating": 5,
            "user": "user_id",
            "place": "place_id"
            })
        self.assertEqual(response.status_code, 404)

    def test_update_review_invalid_data(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jadscqdcne.doe@exasqcmple.com"
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

        review = self.client.post('/api/v1/reviews/', json={
            "text": "sifrng",
            "rating": 3,
            "user": user_id,
            "place": place_id
            })
        self.assertEqual(review.status_code, 201)

        data_review = review.get_json()
        review_id = data_review['id']
        response = self.client.put(f'/api/v1/reviews/{review_id}', json={
            "text": "",
            "rating": 0,
            "user": "user_id",
            "place": "place_id"
            })
        self.assertEqual(response.status_code, 400)

    def test_delete_review(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jadscqdcne.doe@exasvdsqcmple.com"
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

        review = self.client.post('/api/v1/reviews/', json={
            "text": "sifrng",
            "rating": 3,
            "user": user_id,
            "place": place_id
            })
        self.assertEqual(review.status_code, 201)
        data_review = review.get_json()
        review_id = data_review['id']
        response = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)

    def test_delete_review_not_found(self):
        response = self.client.delete(f'/api/v1/reviews/123')
        self.assertEqual(response.status_code, 404)

    def test_list_reviews_by_place(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@examkjgkgple.com"
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

        review = self.client.post('/api/v1/reviews/', json={
            "text": "sifrng",
            "rating": 3,
            "user": user_id,
            "place": place_id
            })
        self.assertEqual(review.status_code, 201)

        response = self.client.get(f'/api/v1/reviews/places/{place_id}/reviews')
        self.assertEqual(response.status_code, 200)

    def test_list_reviews_by_place_not_found(self):
        user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jandsq.doe@examkjgkgple.com"
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

        review = self.client.post('/api/v1/reviews/', json={
            "text": "sifrng",
            "rating": 3,
            "user": user_id,
            "place": place_id
            })
        self.assertEqual(review.status_code, 201)
        response = self.client.get(f'/api/v1/reviews/places/place_id/reviews')
        self.assertEqual(response.status_code, 404)
