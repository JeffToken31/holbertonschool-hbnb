from app.models.review import Review
from app.models.place import Place
from app.models.users import User
from app.models.amenities import Amenity
"""
This module test Objects and their relations
"""

def main():
    """
    This Function call all possibilities
    to check models and theire relation
    """
    # Creation of users
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.password == "password"
    assert user.is_admin is False
    print("{} created !!!\n".format(user))

    owner = User(first_name="Jane", last_name="Poe", email="jane.poe@example.com", password="password2")
    print("{} created !!!\n".format(owner))

    # Creation of places by owner
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=100.00, latitude=37.7749, longitude=-122.4194, owner=owner)
    print("Place created: {}".format(place))
    print("At: {}€ by night\n".format(place.created_at))

    place2 = Place(title="Family's home", description="A nice place for family", price=200.00, latitude=35.7749, longitude=-54.4194, owner=owner)
    print("Place created: {}".format(place2))
    print("At: {}€ by night\n".format(place2.created_at))

    # Creations of ammenities
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("Amenity creation test passed!")
    print("Amenity: {}".format(amenity.name))
    print("At: {}\n".format(amenity.created_at))

    amenity2 = Amenity(name="Swimming pool")
    assert amenity2.name == "Swimming pool"
    print("Amenity creation test passed!")
    print("Amenity: {}".format(amenity2.name))
    print("At: {}\n".format(amenity2.created_at))

    # Creation of reviews
    review = Review(text="Great stay!", rating=5, place=place, user=user)
    assert review.text == "Great stay!"
    assert review.rating == 5
    assert review.place == place
    assert review.user == user
    print("review creation test passed!")
    print("review: {}".format(review))
    print("At: {}".format(review.created_at))
    print("writer of this review: {}".format(review.user))
    print("commenting {}".format(review.place))
    print("rating: {} stars".format(review.rating))
    print("comment: {}".format(review.text))

    review2 = Review(text="Perfect for family !", rating=4, place=place2, user=user)
    assert review2.text == "Perfect for family !"
    assert review2.rating == 4
    assert review2.place == place2
    assert review2.user == user
    print("review creation test passed!")
    print("review: {}".format(review2))
    print("At: {}".format(review2.created_at))
    print("writer of this review: {}".format(review2.user))
    print("commenting {}".format(review2.place))
    print("rating: {} stars".format(review2.rating))
    print("comment: {}".format(review2.text))
    
    # Check relation user/place, user/review

    owner.add_place(place)
    print("{} have:\n{}".format(owner, owner.places[0]))

    owner.add_place(place2)
    print("{} have:\n{}".format(owner, owner.places[1]))

    print("So, {} have:".format(owner))
    for plc in owner.places:
        print(plc)


    user.add_review(review)
    print("{} have writed:\n{}".format(user, user.reviews[0]))

    user.add_review(review2)
    print("{} have writed:\n{}".format(user, user.reviews[1]))

    print("So, {} have posted:".format(user))
    for rev in user.reviews:
        print(rev)
    

    # Check relation place/review, place/amenities

    place.add_review(review)
    print("{} has receveid:\n{}".format(place, place.reviews[0]))

    place.add_review(review2)
    print("{} has receveid:\n{}".format(owner, place.reviews[1]))

    print("So, {} has receveid:".format(owner))
    for rev in place.reviews:
        print(plc)


    place.add_amenity(amenity)
    print("{} purpose:\n{}".format(place, place.amenities[0]))

    place.add_amenity(amenity2)
    print("{} purpose:\n{}".format(owner, place.amenities[1]))

    print("So, {} purpose:".format(owner))
    for ame in place.amenities:
        print(ame)
main()