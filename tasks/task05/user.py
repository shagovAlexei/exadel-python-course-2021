# Shagov Aleksei

# run
# python -m pytest user.py -v

def create_user(name, surname, age=42, **extra):
    user, extra_dict = {}, {}
    user['name'] = name
    user['surname'] = surname
    user['age'] = age
    # print(user)
    for extra_key, extra_value in extra.items():
        extra_dict[extra_key] = extra_value
        # print(extra_value)
    user['extra'] = extra_dict
    return user

# user = create_user("Bill", "Gates", age=65)
# print(user)


def test_two_params():
    assert create_user("John", "Doe") == \
        {
        "name": "John",
        "surname": "Doe",
        "age": 42,
        "extra": {}
    }

def test_tree_params():
    assert create_user("Bill", "Gates", age=65) == \
        {
        "name": "Bill",
        "surname": "Gates",
        "age": 65,
        "extra": {}
    }
