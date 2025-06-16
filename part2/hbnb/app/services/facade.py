from app.persistence.repository import InMemoryRepository
from app.models.users import User


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


    def update_user(self, user_data):
        '''
        This function checks by uuid if user exist,
        return message and data of user
        '''

        user_id = user_data.get("id")
        user_exist = self.user_repo.get(user_id)
        if user_exist == None :
            return None
        self.user_repo.update(user_id, **user_data)
        return user_exist
    
    
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass