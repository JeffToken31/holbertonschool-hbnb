from app.persistence.repository import InMemoryRepository
from app.models.users import User
from app.models.amenities import Amenity


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