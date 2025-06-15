from app.models.baseModel import BaseModel
'''
Place class inherite of base model and is linked to one place_owner
'''
class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.rating = rating
        self.text = text
        self.place = place  #review is linked to one place
        self.user = user    #review is linked to one user

    def __str__(self):
        return "{}".format(self.text)