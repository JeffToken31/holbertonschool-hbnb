from app.models.amenities import Amenity
"""
This module test simple creatioon of amenity
"""

def test_amenity_creation():
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("Amenity creation test passed!")
    print("Amenity: {}".format(amenity.name))
    print("At: {}".format(amenity.created_at))

test_amenity_creation()