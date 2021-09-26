# Shagov Aleksei

# run
# python -m pytest user.py -v

def create_user(name: str, surname: str, age: int = 42, **kwargs):
    return {
        'name': name,
        'surname': surname,
        'age': age,
        'extra': kwargs
    }


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

def test_many_kwargs():
    assert create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True) == \
        {
        "name": "Marie",
        "surname": "Curie",
        "age": 66,
        "extra": {
            "occupation": "physicist",
            "won_nobel": True
        }
    }
