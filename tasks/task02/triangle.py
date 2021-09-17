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
		except:
				print("\nInvalid input data!")
		return value
		
def calculate_are_by_base_and_height():
	x = input("Enter your base and height (example: 5 6): ")
	parts = str(map(int, x.split()))
	print(parts)
	print(type(parts))
	# parts = s.split(" ")
	# base = parts[0]
	base = input_validation(x, 0)
	height = input_validation(x, 1)
	print(base, height)
	area = (0.5 * base * height)
	return print(f"Area is: {area:.1f} ")


def calculate_are_by_sides_and_angle():
	s = input("Enter 2 sides and angle between them (example: 15 8 30): ")
	parts = s.split(" ")
	side_a = int(parts[0])
	side_b = parts[1]
	angle = parts[2]
	print(side_a, side_b, angle)
	area = 0.5 * float(side_a) * float(side_b) * \
						float(math.sin(math.radians(int(angle))))
	return print(f"Area is: {area:.1f}")

def main():
	print("Welcome to the triangle area calculation tool.")
	while True:
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
