from app.models.baseModel import BaseModel
from app.models.users import User
from app.persistence.repository import InMemoryRepository

'''
Place class inherite of base model and has amentity and review intance
'''
class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        """
        Initialize a place by multiple parameters given
        args:
            title(str max=100): to define title of the place
            description(str max=50): to define description of the place
            price(float min > 0): define price of the place
            latitude(float min=-90 max=90): define latitude of the place
            longitude(float min=-180 max=180): define longitude of the place
            owner(User exist=True): define owner of the place
        raises:
            TypeError: if attributes have correct type
            ValueError: if attribute respect exigence
        """
        super().__init__()

        if not isinstance(title, str):
            raise TypeError("title must be a string")
        elif len(title) > 100:
            raise ValueError("title must be 100 charaters max")
        else:
            self.title = title

        if not isinstance(description, str):
            raise TypeError("description must be a string")
        else:
            self.description = description

        if not isinstance(price, float):
            raise TypeError("price must be a float")
        elif price <= 0:
            raise ValueError("price must be superior to 0")
        else:
            self.price = price

        if not isinstance(latitude, float):
            raise TypeError("latitude must be a float")
        elif latitude < -90 or latitude > 90:
            raise ValueError("latitude must be between -90 and 90")
        else:
            self.latitude = latitude

        if not isinstance(longitude, float):
            raise TypeError("longitude must be a float")
        elif longitude < -180 or longitude > 180:
            raise ValueError("longitude must be between -90 and 90")
        else:
            self.longitude = longitude

        if not isinstance(owner, User):
            raise TypeError("owner must be an instance of User")
        else:
            self.owner = owner
        """
        elif InMemoryRepository.get_by_attribute("id", owner.id) is None: #a deplacer dans la facade ?
            raise ValueError("owner must be exist")
        """

        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def __str__(self):
        return "{}- {} ({}€)".format(self.title, self.description, self.price)