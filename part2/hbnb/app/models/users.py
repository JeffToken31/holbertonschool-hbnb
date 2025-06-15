from app.models.baseModel import BaseModel
'''
Place class inherite of base model and has place and review intance
'''
class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = False
        self.places = []     #List to store related places
        self.reviews = []    #List to store related reviews


    def add_place(self, place):
        """Add a review to the place."""
        self.places.append(place)

    def add_review(self, review):
        """Add a review to the user."""
        self.reviews.append(review)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)