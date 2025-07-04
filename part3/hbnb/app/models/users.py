from app.models.baseModel import BaseModel
from re import match
from extensions import bcrypt, db

'''
User class inherits from base model and has place and review instances
'''


class User(BaseModel):
    """
    Define user class
    """
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    place = db.relationship("place.id",)

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """
        Initialize a user by multiple parameters given
        args:
            first_name(str max=50): to define first_name of the user
            last_name(str max=50): to define last_name of the user
            email(str content="@"): define email of the user
            password: define and hash password with bcrypt
            is_admin(bool default=False): authorise access for admin
        raises:
            TypeError: if attributes have incorrect type
            ValueError: if attribute doesn't respect constraints
        """
        super().__init__()

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin


    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        elif len(first_name) > 50:
            raise ValueError("first_name must be 50 characters max")
        else:
            self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        elif len(last_name) > 50:
            raise ValueError("last_name must be 50 characters max")
        else:
            self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("email must be a string")
        elif not match(
                        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                        email):
            raise ValueError("enter a valid email")
        else:
            self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        else:
            self._password = self.hash_password(password)

    def add_place(self, place):
        """Add a place to the user."""
        self.places.append(place)

    def add_review(self, review):
        """Add a review to the user."""
        self.reviews.append(review)

    def __str__(self):
        """
        Used to return object as we want
        """
        return "{} {}".format(self.first_name, self.last_name)

    def to_dict(self):
        return {'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email}

    def hash_password(self, password):
        """Hashes the password before storing it."""
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
