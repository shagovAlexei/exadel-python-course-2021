# Shagov Aleksei

def create_user(name, surname, age=42, **extra):
    user, extra_dict = {}, {}
    user['name'] = name
    user['surname'] = surname
    user['age'] = age
    
