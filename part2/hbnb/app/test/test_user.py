from app.models.users import User

def test_user_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.is_admin is False  # Default value
    print("Bonjour {}, your id will be: {}".format(user.first_name, user.id))
    print("Your profile has been upgraded at: {}".format(user.created_at))
    print("User creation test passed!")
    print(user)

    user2 = User(first_name="Jane", last_name="Poe", email="jane.poe@example.com")
    assert user2.first_name == "Jane"
    assert user2.last_name == "Poe"
    assert user2.email == "jane.poe@example.com"
    assert user2.is_admin is False  # Default value
    print("Bonjour {}, your id will be: {}".format(user2.first_name, user2.id))
    print("Your profile has been upgraded at: {}".format(user2.created_at))
    print("User creation test passed!")
    print(user2)

test_user_creation()
