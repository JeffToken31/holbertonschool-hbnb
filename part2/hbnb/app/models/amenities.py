from app.models.baseModel import BaseModel
'''
Ammenity class inherite of base model and is linked to one place
'''
class Amenity(BaseModel):
    def __init__(self, name=""):
        super().__init__()
        self.name = name

    def __str__(self):
        return "{}".format(self.name)