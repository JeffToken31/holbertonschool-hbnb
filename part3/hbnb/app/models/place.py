from app.models.baseModel import BaseModel
from sqlalchemy.orm import validates, relationship
from extensions import db
"""
Represents a place in HBnB, with title, location,
price, owner, amenities, and reviews.
"""


class Place(BaseModel):
    """
    Define Place class
    """
    __tablename__ = 'place'

    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    latitude = db.Column(db.Float(precision=6), nullable=False)
    longitude = db.Column(db.Float(precision=6), nullable=False)
    owner = db.Column(db.String(128), db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(516), nullable=True)


    def __init__(self, title, price, latitude, longitude, owner, description="", amenities=[], reviews={}):
        """Initialize multiple parametres"""

        super().__init__()

        self.title = title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.description = description
        """ self.amenities = []
        self.reviews = [{}]"""

    @validates("title")
    def validate_title(self, _, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) > 100:
            raise ValueError("Title must be max 100 characters")
        return title
    
    @validates("description")
    def validate_descrition(self, _, description):
        if description is not None and not isinstance(description, str):
            raise TypeError("Description must be a string")
        return description

    @validates("price")
    def validate_price(self, _, price):
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        elif price <= 0:
            raise ValueError("Price must be superior to 0")
        return price

    @validates("latitude")
    def validate_latitude(self, _, latitude):
        if not isinstance(latitude, float):
            raise TypeError("Latitude must be a float")
        elif latitude < -90 or latitude > 90:
            raise ValueError("Latitude must be between -90 and 90")
        return latitude

    @validates("longitude")
    def validate_longitude(self, _, longitude):
        if not isinstance(longitude, float):
            raise TypeError("Longitude must be a float")
        elif longitude < -180 or longitude > 180:
            raise ValueError("Longitude must be between -180 and 180")
        return longitude

    @validates("owner")
    def validate_owner(self, _, owner):
        if not hasattr(owner, 'id'):
            raise ValueError("Invalid owner")
        return owner

    def add_review(self, review):
        """Add a review to the place"""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place"""
        self.amenities.append(amenity)

    def __str__(self):
        return "{}- {} ({}€)".format(self.title, self.description, self.price)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': {
                'id': self.owner.id,
                'first_name': self.owner.first_name,
                'last_name': self.owner.last_name,
                'email': self.owner.email
            } if self.owner else None,
            'amenities': [
                {
                    'id': amenity.id,
                    'name': amenity.name
                } for amenity in self.amenities
            ]
        }

    def to_bibl(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner.id
        }
