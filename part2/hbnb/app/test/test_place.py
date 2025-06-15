from app.models.place import Place
from app.models.users import User
from app.models.review import Review

def test_place_creation():
    owner = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.7749, longitude=-122.4194, owner=owner)

    # Adding a review
    review = Review(text="Great stay!", rating=5, place=place, user=owner)

    owner.add_place(place)
    place.add_review(review)
    owner.add_review(review)

    assert place.title == "Cozy Apartment"
    assert place.price == 100
    assert len(place.reviews) == 1
    assert place.reviews[0].text == "Great stay!"
    print("Place creation and relationship test passed!")
    print("Owner: {} {}".format(owner.last_name, owner.first_name))
    print("ID: {}\nCreated at: {}".format(owner.id, owner.created_at))
    print("Your place:")
    for plc in owner.places:
        print("{}".format(plc))
    print("Your review of this place {}:".format(place.title))
    for rev in owner.reviews:
        print("{}".format(rev))

test_place_creation()