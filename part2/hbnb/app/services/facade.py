from app.persistence.repository import InMemoryRepository
from app.models.users import User
from app.models.amenities import Amenity
from app.models.review import Review
from app.models.place import Place


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        '''
        This function is called by API, it's keep and
        destructurate data with ** into elements "key: value,"
        add In-memory and return data of user
        '''

        user = User(**user_data) # **is to destructurate a dict
        self.user_repo.add(user)
        return user


    def update_user(self, user_id, user_data):
        '''
        This function checks by uuid if user exist,
        return message and data of user
        '''
        user_exist = self.user_repo.get(user_id)
        if not user_exist:
            return None
        for key, value in user_data.items():
            if hasattr(user_exist, key):
                setattr(user_exist, key, value)
        return user_exist
    
    
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()
    
    # Placeholder for logic to create a place
    def create_place(self, place_data):
        price = place_data.get('price')
        latitude = place_data.get('latitude')
        longitude = place_data.get('longitude')

        if price is None or price < 0:
            raise ValueError("Price must be a non-negative float.")
        if latitude is None or not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        if longitude is None or not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180.")

        owner_id = place_data.get('owner_id')
        owner = self.user_repo.get(owner_id)
        if not owner:
            raise ValueError("The specified owner does not exist.")

        amenities_ids = place_data.get('amenities', [])
        amenities = []
        for amenity_id in amenities_ids:
            amenity = self.amenity_repo.get(amenity_id)
            if not amenity:
                raise ValueError(f"Amenity not found: {amenity_id}")
            amenities.append(amenity)

        place = Place(
            title=place_data['title'],
            price=price,
            latitude=latitude,
            longitude=longitude,
            owner=owner,
            description=place_data.get('description', "")
        )
        place.amenities = amenities

        self.place_repo.add(place)
        return place


    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found.")
        return place


    def get_all_places(self):
        return self.place_repo.get_all()


    def update_place(self, place_id, place_data):
        if 'price' in place_data and place_data['price'] < 0:
            raise ValueError("Price must be a non-negative float.")
        if 'latitude' in place_data and not (-90 <= place_data['latitude'] <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        if 'longitude' in place_data and not (-180 <= place_data['longitude'] <= 180):
            raise ValueError("Longitude must be between -180 and 180.")

        if 'owner_id' in place_data:
            owner = self.user_repo.get(place_data['owner_id'])
            if not owner:
                raise ValueError("The specified owner does not exist.")
            place_data['owner'] = owner
            del place_data['owner_id']

        if 'amenities' in place_data:
            amenity_ids = place_data['amenities']
            amenities = []
            for amenity_id in amenity_ids:
                amenity = self.amenity_repo.get(amenity_id)
                if not amenity:
                    raise ValueError(f"Amenity not found: {amenity_id}")
                amenities.append(amenity)
            place_data['amenities'] = amenities

        return self.place_repo.update(place_id, place_data)
    
    
    def create_amenity(self, amenity_data):
    # Placeholder for logic to create an amenity
        amenity = Amenity(**amenity_data) # **is to destructurate a dict
        self.amenity_repo.add(amenity)
        return amenity


    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity_exist = self.amenity_repo.get(amenity_id)
        if not amenity_exist:
            return None
        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity_exist
    
    # Placeholder for review

    def create_review(self, review_data):
        user_id = review_data.get('user')
        place_id = review_data.get('place')
        user = self.user_repo.get(user_id)
        place = self.place_repo.get(place_id)
        if not user:
            raise ValueError("User does not exist.")
        if not place:
            raise ValueError("Place does not exist.")
        text = review_data.get('text')
        rating = review_data.get('rating')
        review = Review(text, rating, place, user)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        # Placeholder for logic to retrieve all reviews
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        all_reviews = self.review_repo.get_all()
        return [review for review in all_reviews if getattr(review, 'place').id == place_id]

    def update_review(self, review_id, review_data):
        # Placeholder for logic to update a review
        review = self.review_repo.get(review_id)
        if not review:
            return None
        if 'text' in review_data:
            review.text = review_data['text']
        if 'rating' in review_data:
            review.rating = review_data['rating']
        if 'place' in review_data:
            place = self.place_repo.get(review_data['place'])
            if not place:
                raise ValueError("Place does not exist.")
            review.place = place
        if 'user' in review_data:
            user = self.user_repo.get(review_data['user'])
            if not user:
                raise ValueError("User does not exist.")
            review.user = user
        return review

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        review_exist = self.review_repo.get(review_id)
        if not review_exist:
            return None
        return self.review_repo.delete(review_id)