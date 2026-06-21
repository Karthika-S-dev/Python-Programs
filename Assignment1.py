#Taking two inputs from user
Number1 = int(input("Enter the First Number: "))
Number2 = int(input("Enter the Second Number: "))
#Finding the sum of two numbers
SumResult= Number1+Number2
#Finding the difference of two numbers
DifferenceResult= abs(Number1 - Number2)
#Finding the product of two numbers
MultiplicationResult = Number1 * Number2

#Finding the Exponential result of two numbers
ExpResult = Number1 ** Number2

print("Sum of two numbers is : " , SumResult)
print("Difference between two numbers is : " , DifferenceResult)
print("Product of two numbers is : " , MultiplicationResult)
#Finding the quotient of two numbers
if Number2 != 0:
    DivisionResult= Number1/Number2
    print("Division result of two numbers is : " , DivisionResult)
else:
    print("Division by zero is not possible")
    #Finding the modulus of two numbers
if Number2 != 0:
    ModResult = Number1%Number2
    print("Modulus of two numbers is : " ,ModResult)
else:
    print("Modulus by zero is not possible")
#Finding the floordivision of two numbers
if Number2 != 0:
    FloorDivResult= Number1//Number2
    print("Division result of two numbers is : " , FloorDivResult)
else:
    print("Floor Division by zero is not possible")

print("Exponential result of two numbers is : " , ExpResult)
print('Concatenated Numbers',int(str(Number1) + str(Number2)))
String1 = input("Enter the First String: ")
String2 = input("Enter the Second String: ")
print(String1 + ' ' + String2)