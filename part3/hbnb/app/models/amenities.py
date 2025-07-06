from app.models.baseModel import BaseModel
from extensions import db
from sqlalchemy.orm import validates
from app.models.place import place_amenity
'''
Ammenity class inherite of base model and is linked to one place
'''


class Amenity(BaseModel):
    """
    Define amenity class
    """
    __tablename__ = 'amenity'

    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        """
        Initialize a review by name given
        args:
            name(str max=50): to define name of the review
        raises:
            TypeError: if attributes have correct type
            ValueError: if attribute respect exigence
        """
        super().__init__()

        self.name = name

    @validates("name")
    def validate_name(self, _, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        elif len(name) > 50:
            raise ValueError("name must be 50 characters max")
        return name

    def to_dict(self):
        return {'name': self.name,
                'id': self.id}

    def __str__(self):
        return "{}".format(self.name)
