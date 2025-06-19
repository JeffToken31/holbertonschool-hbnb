from app.persistence.repository import InMemoryRepository
from app.models.users import User
from app.models.amenities import Amenity
from app.models.review import Review


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
    # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        # Placeholder for logic to retrieve all reviews
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        # Placeholder for logic to retrieve all reviews for a specific place
        return self.review_repo.get_by_attribute('place', place_id)

    def update_review(self, review_id, review_data):
        # Placeholder for logic to update a review
        review_exist = self.review_repo.get(review_id)
        if not review_exist:
            return None
        self.review_repo.update(review_id, review_data)
        return review_exist

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        review_exist = self.review_repo.get(review_id)
        if not review_exist:
            return None
        return self.review_repo.delete(review_id)