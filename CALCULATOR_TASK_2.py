# Python program for simple calculator

def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2


def divide(num1, num2):
	return num1 / num2



# Take input from the user
select = int(input("press 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division :"))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if select == 1:
	print(a, "+", b, "=", add(a, b))

elif select == 2:
	print(a, "-", b, "=",subtract(a, b))

elif select == 3:
	print(a, "*", b, "=",multiply(a, b))

elif select == 4:
	print(a, "/", b, "=",divide(a, b))
else:
	print("Invalid input")
