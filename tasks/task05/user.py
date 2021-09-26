# Shagov Aleksei

def create_user(name, surname, age=42, **extra):
    user, extra_dict = {}, {}
    user['name'] = name
    user['surname'] = surname
    user['age'] = age
    print(user)

    for extra_key, extra_value in extra.items():
        extra_dict[extra_key] = extra_value
        print(extra_value)


user = create_user("Bill", "Gates", age=65)
print(user)
