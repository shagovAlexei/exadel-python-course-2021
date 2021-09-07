# Shagov Aleksei

import math

def qwe(a, b):
	# qwe(2, 3)
	return print(a+b)

def area_test(b, h):
	a = 0.5 * float(b) * float(h)
	return a

def area_angle(a, b, angle):
	ar = 0.5 * float(a) * float(b) * float(math.sin(math.radians(int(angle))))
	print(ar)
	return ar

def main():
	a = input("Input a: ")
	b = input("Input b: ")
	angle = input("Input alfa: ")
	area_angle(a, b, angle)
if __name__ == "__main__":
    main()
