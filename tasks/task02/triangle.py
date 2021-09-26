# Shagov Aleksei

import math


def check_positive(s):
    try:
        f = int(s)
        if (f > 0):
            return True
        # Otherwise return false
        return False
    except ValueError:
        return False


def calculate_are_by_base_and_height():
    str = input("Enter your base and height (example: 5 6): ")
    print_error = "Invalid input data! Enter two positive number"
    parts = str.split(" ")
    if len(parts) == 2 and check_positive(parts[0]) and check_positive(parts[1]):
        base = int(parts[0])
        height = int(parts[1])
        area = (0.5 * base * height)
        return print(f"Area is: {area:.0f} ")
    else:
        print(print_error)


def calculate_are_by_sides_and_angle():
    str = input("Enter 2 sides and angle between them (example: 15 8 30): ")
    print_error = "Invalid input data! Enter two positive number and angle >= 180"
    parts = str.split(" ")
    if len(parts) == 3 and check_positive(parts[0]) and check_positive(parts[1]) and check_positive(parts[2]):
        side_a = float(parts[0])
        side_b = float(parts[1])
        angle = float(parts[2])
        area = 0.5 * side_a * side_b * math.sin(math.radians(angle))
        return print(f"Area is: {area:.0f}")
    else:
        print(print_error)


def main():
    menu_number = True
    menu = '''\nMenu: \n1. Calculate triangle area by base and height \n2. Calculate triangle area by 2 sides and angle between them \n3. Exit\n'''
    print(menu)
    while menu_number != 3:
        menu_number = int(input("Enter menu item number: "))
        if menu_number == 1:
            calculate_are_by_base_and_height()
            print(menu)
        elif menu_number == 2:
            calculate_are_by_sides_and_angle()
            print(menu)
        elif menu_number == 3:
            print("Goodbye!")
        else:
            print("Invalid input data! Enter 1, 2 or 3!")


if __name__ == "__main__":
    main()
