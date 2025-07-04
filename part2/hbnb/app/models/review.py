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
        elif len(text) == 0:
            raise ValueError("text must be not empty")
        else:
            self._text = text

        if not isinstance(rating, int):
            raise TypeError("rating must be a int")
        elif rating < 1 or rating > 5:
            raise ValueError("rating must be between 1 and 5")
        else:
            self._rating = rating

        if not isinstance(place, Place):
            raise TypeError("place must be an instance of Place")
        else:
            self._place = place

        if not isinstance(user, User):
            raise TypeError("user must be an instance of User")
        else:
            self._user = user

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        else:
            self._text = text

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if not isinstance(rating, int):
            raise TypeError("rating must be a int")
        elif rating < 1 or rating > 5:
            raise ValueError("rating must be between 1 and 5")
        else:
            self._rating = rating

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, place):
        if not isinstance(place, Place):
            raise TypeError("place must be an instance of Place")
        else:
            self._place = place

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        if not isinstance(user, User):
            raise TypeError("user must be an instance of User")
        else:
            self._user = user

    def to_dict(self):
        return {
            'id': self.id,
            'text': self._text,
            'rating': self._rating,
            'place': self._place.id,
            'user': self._user.id
        }

    def __str__(self):
        return "{}".format(self.text)
