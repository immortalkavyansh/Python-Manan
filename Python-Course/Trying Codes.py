"""
print("Enter the word(Among Set, Append, Mutable, Immutable, String): ")
myWord = input()
meaning = {"Set" : "Well defined set of objects",
           "Append" :"add (something) to the end of a written document",
           "Mutable": "liable to change",
           "Immutable" : "unchanging over time or unable to be changed",
           "String" : "material consisting of threads of cotton, hemp, or other material twisted together to form a thin length"}
print(meaning[myWord])



age = int(input("Enter your age: "))
if age > 18 and age < 101:
    print("you can drive")
elif age > 7 and age < 18:
    print("you can't drive")
elif age == 18:
    print("come for physical test")
else:
    print("not a valid age")

print("enter your name plz ")
input()
print("nice name ")
print("now enter your age plz")
var1 = 18
var2 = int(input())
if var2>var1:
 	print("yes you are a perfect driver")
elif var2==var1:
 		print("we cannot say that you have to.come for driving test")
else:
 		print("you have to wait for some years")




# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")

This is a faulty calculator program for a Exercise given by Harry from Code with Harry Youtube Channel
Coder - Praveen Singh Chauhan :)
45 * 3 = 555, 56+9=77, 56/6=4 faulty calculate have to calculate this else right calculation

ope_cal = ""
num1, num2 = 0, 0

while ope_cal != "exit":
    print("=" * 50)
    print("type 'exit' to end program or math operator like + - * / **")
    ope_cal = input("What do you want to do > ").lower()
    if ope_cal == "exit":
        print("OK... we are ending this Calculator Program ......")
        break
    elif ope_cal == "+" or ope_cal == "-" or ope_cal == "*" or ope_cal == "/" or ope_cal == "%" or ope_cal == "**":
        num1 = int(input(" First Number >  "))
        num2 = int(input("Second Number >  "))
    else:
        print("you are doing mistake")
        print("its a '[Calculator]' so type operator i.e. + - * / ** %")
        print("*" * 50)

    if num1 == 45 and num2 == 3 and ope_cal == "*":
        print("Result is '[555]' ")
    elif num1 == 56 and num2 == 9 and ope_cal == "+":
        print("Result is '[77]' ")
    elif num1 == 56 and num2 == 6 and ope_cal == "/":
        print("Result is '[4]' ")
    elif ope_cal == "exit":
        break
    else:
        if ope_cal == "*":
            print(f'Result is "[{num1}*{num2}]"')
        elif ope_cal == "-":
            print(num1-num2)
        elif ope_cal == "+":
            print(num1 + num2)
        elif ope_cal == "*":
            print(num1 * num2)
        elif ope_cal == "/":
            print(num1 / num2)
        elif ope_cal == "**":
            print(num1 ** num2)
        elif ope_cal == "%":
            print(num1 / num2)

# End of the program

import random
v1 = random.randint(1, 15)
print(v1)

print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()
"""
# l = 6#Global variable
# def funktion1(n):
#     l = 50#Local Variable
#     m = 60#Local Variable
#     print(l, m)
#     print(n, "I have Printed")
# funktion1("This is me")
# print(l, m)








