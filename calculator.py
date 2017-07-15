operatie = input("What operation would you like to do(add, subtract, divide, multiply, modulo):")
number1 = float(input("Number 1 = "))
number2 = float(input("Number 2 = "))
if operatie == "add":
    number3 = number1 + number2
elif operatie == "subtract":
    number3 = number1 - number2
elif operatie == "divide":
    number3 = number1 / number2
elif operatie == "multiply":
    number3 = number1 * number2
elif operatie == "modulo":
    number3 = number1 % number2

print ("Rezultatul este = ", str(number3))
