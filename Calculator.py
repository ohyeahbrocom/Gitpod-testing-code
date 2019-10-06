import os
import time
import math

i = 1

while i:

    os.system('clear')
    time.sleep(0.5)

    op = input("Select a opration to calculator +, -, *, /. \"A\" for more advanced opration: ")
    print("\n")

    if op == "+":
        time.sleep(0.2)
        num1 = input("Enter the first number: ")
        print("\n")
        time.sleep(0.2)
        num2 = input("Enter the second number: ")
        print("\n")
        result = float(num1) + float(num2)

    elif op == "-":
        time.sleep(0.2)
        num1 = input("Enter the first number: ")
        print("\n")
        time.sleep(0.2)
        num2 = input("Enter the second number: ")
        print("\n")
        result = float(num1) - float(num2)

    elif op == "*":
        time.sleep(0.2)
        num1 = input("Enter the first number: ")
        print("\n")
        time.sleep(0.2)
        num2 = input("Enter the second number: ")
        print("\n")
        result = float(num1) * float(num2)

    elif op == "/":
        time.sleep(0.2)
        num1 = input("Enter the first number: ")
        print("\n")
        time.sleep(0.2)
        num2 = input("Enter the second number: ")
        print("\n")
        result = float(num1) / float(num2)

    elif op == "a" or op == "A":
        print("Type 1 for raminder of a division problem.\n")
        time.sleep(1)
        print("Type 2 for Area of a circle.\n")
        time.sleep(1)
        op = input("Select the options: ")
        print("\n")

        if op == "1":
            num1 = input("Enter the first number: ")
            print("\n")
            num2 = input("Enter the second number: ")
            print("\n")
            result = float(num1) % float(num2)

        elif op == "2":
            pi = input("Set the value of π, defult is 3.14   : ")
            print("\n")
            r = input("Type the radius of the circle: ")
            print("\n")
            result = float(pi) * float(r) ** 2

        else:
            print("No letter for that option, please try again.")
            break

    else:
        print("No letter for that option, please try again.")
        break

    print("The answer to the question is " + str(result) + "!\n")

    i = input("Do you want to use the calculator again?  Answer y/n  : ")

    if i == "y" and i == "Y":
        i = 1

    elif i == "n" and i == "N":
        break

    else:
        print("No letter for that option, please try again.")
        break
