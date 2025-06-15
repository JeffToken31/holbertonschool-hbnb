from app.models.review import Review
from app.models.place import Place
from app.models.users import User
"""
This module test simple creatioon of review
"""

def test_review_creation():
    owner = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.7749, longitude=-122.4194, owner=owner)
    user2 = User(first_name="Jane", last_name="Poe", email="jane.poe@example.com", password="password2")

    review = Review(text="Great stay!", rating=5, place=place, user=user2)
    assert review.text == "Great stay!"
    assert review.rating == 5
    assert review.place == place
    assert review.user == user2
    print("review creation test passed!")
    print("review: {}".format(review))
    print("At: {}".format(review.created_at))
    print("writer of this review: {}".format(review.user))
    print("commenting {}".format(review.place))
    print("rating: {} stars".format(review.rating))
    print("comment: {}".format(review.text))


test_review_creation()