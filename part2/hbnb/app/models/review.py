from app.models.baseModel import BaseModel
from app.persistence.repository import InMemoryRepository
from app.models.users import User
from app.models.place import Place
'''
Place class inherite of base model and is linked to one place_owner
'''
class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        """
        Initialize a review by multiple parameters given
        args:
            text(str min=1): to define text of the review
            rating(int min=1 max=5): define rating of the review
            place(Place exist=True): define place of the review
            user(User exist=True): define user of the review
        raises:
            TypeError: if attributes have correct type
            ValueError: if attribute respect exigence
        """
        super().__init__()
        
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        elif len(text) < 0:
            raise ValueError("text must be not empty")
        else:
            self.text = text
        
        if not isinstance(rating, int):
            raise TypeError("rating must be a int")
        elif rating < 1 or rating > 5:
            raise ValueError("rating must be between 1 and 5")
        else:
            self.rating = rating

        if not isinstance(place, Place):
            raise TypeError("place must be an instance of Place")
        else:
            self.place = place  #review is linked to one place
        """
        elif InMemoryRepository.get_by_attribute("id", place.id) is None: #a deplacer dans la facade ?
            raise ValueError("place must be exist")
        """

        if not isinstance(user, User):
            raise TypeError("user must be an instance of User")
        else:
            self.user = user #review is linked to one user
        """
        elif InMemoryRepository.get_by_attribute("id", user.id) is None: #a deplacer dans la facade ?
            raise ValueError("user must be exist")
        """ 

    def __str__(self):
        return "{}".format(self.text)