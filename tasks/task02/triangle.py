# Shagov Aleksei
'''Menu:
1. Calculate triangle area by base and height
2. Calculate triangle area by 2 sides and angle between them
3. Exit
Enter menu item number: 1
Enter base and height: 5 6
Area is: 15

Menu:
1. Calculate triangle area by base and height
2. Calculate triangle area by 2 sides and angle between them
3. Exit
Enter menu item number: 2
Enter 2 sides and angle(degrees) between them: 15 8 30
Area is: 30

Menu:
1. Calculate triangle area by base and height
2. Calculate triangle area by 2 sides and angle between them
3. Exit
Enter menu item number: 3
Goodbye!
'''
import math

def input_validation(input_string, item):
    try:
        value = abs(float(input_string.split()[item]))
        if value == 0:
            print("\nInvalid input data!")
            main()
        return value
    except:
        print("\nInvalid input data!")
        main()
        
def calculate_are_by_base_and_height():
    str = input("Enter your base and height (example: 5 6): ")
    base = input_validation(str, 0)
    height = input_validation(str, 1)
    # print("base", type(base))
    # print("height", type(height))
    # print(base, height)
    area = (0.5 * base * height)
    return print(f"Area is: {area:.0f} ")

def calculate_are_by_sides_and_angle():
    str = input("Enter 2 sides and angle between them (example: 15 8 30): ")
    side_a = input_validation(str, 0)
    side_b = input_validation(str, 1)
    angle = input_validation(str, 2)
    # print(side_a, side_b, angle)
    area = 0.5 * side_a * side_b * math.sin(math.radians(angle))
    return print(f"Area is: {area:.0f}")

def main():
    menu_number = 0
    print("Welcome to the triangle area calculation tool.")
    while menu_number != 3:
        menu_number = input('''
What would you like to do?\n 
1. Calculate triangle area by base and height\n 
2. Calculate triangle area by 2 sides and angle between them\n 
3. Exit\n
Enter menu item number: ''')
        if menu_number == "1":
            calculate_are_by_base_and_height()
        elif menu_number == "2":
            calculate_are_by_sides_and_angle()
        elif menu_number == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
