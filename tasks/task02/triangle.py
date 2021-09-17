# Shagov Aleksei
import math

def Submenu_Base_Height():
	s = input("Enter your base and height: ")
	parts = s.split(" ")
	base = int(parts[0])
	height = parts[1]
	print(base, height)
	area = 0.5 * float(base) * float(height)
	return print("Area is: ", area)

def Submenu_Sides_Angle():
	s = input("Enter your side A and side B and angle between them: ")
	parts = s.split(" ")
	side_a = int(parts[0])
	side_b = parts[1]
	angle = parts[2]
	print(side_a, side_b, angle)
	area = 0.5 * float(side_a) * float(side_b) * \
            float(math.sin(math.radians(int(angle))))
	return print("Area is: ", area)


def main():
	print("Welcome to the triangle area calculation tool.")
	while True:
		playermenumain = input('''
What would you like to do?\n 
1. Calculate triangle area by base and height\n 
2. Calculate triangle area by 2 sides and angle between them\n 
3. Exit\n
Enter menu item number: ''')

		if playermenumain == "1":
			try:
				Submenu_Base_Height()
			except:
				print("Error!!! Something went wrong. You may not have entered all the variables.")
		elif playermenumain == "2":
			try:
				Submenu_Sides_Angle()
			except:
				print("Error!!! Something went wrong. You may not have entered all the variables.")
		elif playermenumain == "3":
			print("Goodbye!")
			break

if __name__ == "__main__":
	try:
		main()
	except:
		print("Error!!! Something went wrong.")
