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
        print(user)
        return {
        "message": "User added",
        "user": self.user_repo.get(user.id)
        
    }, 201

    def update_user(self, user_data):
        '''
        This function checks by uuid if user exist,
        return message and data of user
        '''
        user_id = user_data.get("id")
        user_exist = self.user_repo.get(user_id)
        if user_exist == None :
            return {"error": "User don't exist"}, 401
        self.user_repo.update(user_id, **user_data)
        return {
            "message": "User updated",
            "user": self.user_repo.get(user_id)
        }, 201
    
    def delete_user(self, user_data):
        '''
        This function search user by id
        and delet it
        '''
        user_id = user_data.get("id")
        user_exist = self.user_repo.get(user_id)
        if user_exist == None :
            return {"error": "User don't exist"}, 401
        self.user_repo.delete(user_id)
        return {
            "message": "User deleted",
            "user": user_id
        }
    
    def list_user(self):
        list_users = self.user_repo.get_all()
        return {
            "message": "List of users",
            "User": list_users
        }
    
    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass