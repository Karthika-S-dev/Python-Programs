#TASK 1 - CALCULATOR
print("TASK 1 - BASIC CALCULATOR")
#Taking two inputs from user
Number1 = int(input("Enter the First Number: "))
Number2 = int(input("Enter the Second Number: "))

print("Enter the operation to be performed \n 1: Addition(+) \n 2: Subtraction(-) \n 3: Multiplication(*) \n 4: Division(/) \n 5: Modulo(%) \n 6: Floor Division(//) \n 7: Exponentiation(**) ")
option = input("Enter the Option as +, − , *, /, %, //, **  : ")
if(option == '+'):
    #Finding the sum of two numbers
    SumResult= Number1+Number2
    print("Sum of two numbers is : " , SumResult)
elif(option == '-' ):
    #Finding the difference of two numbers
    DifferenceResult= abs(Number1 - Number2)
    print("Difference between two numbers is : " , DifferenceResult)
elif(option == '*'):
    #Finding the product of two numbers
    MultiplicationResult = Number1 * Number2
    print("Product of two numbers is : " , MultiplicationResult)
elif(option == '/'):
    #Finding the quotient of two numbers
    if Number2 != 0:
        DivisionResult= Number1/Number2
        print("Division result of two numbers is : " , DivisionResult)
    else:
        print("Division by zero is not possible")
elif(option == '%'):
    #Finding the modulus of two numbers
    if Number2 != 0:
        ModResult = Number1%Number2
        print("Modulus of two numbers is : " ,ModResult)
    else:
        print("Modulus by zero is not possible")
elif(option == '//'):
    #Finding the Floor division result of two numbers
    if Number2 != 0:
        FloorDivResult= Number1//Number2
        print("Floor Division result of two numbers is : " , FloorDivResult)
    else:
        print("Floor Division by zero is not possible")
elif(option == '**'):
    #Finding the Exponential result of two numbers
    ExpResult = Number1 ** Number2
    print("Exponential result of two numbers is : " , ExpResult)
else:
    print("Invalid Option")

#TASK 2 - PATTERN

#Taking the number of rows from user
print("TAST 2 - PATTERN PROBLEM ")
n=int(input("Enter the number of rows : "))
if n ==0:
    print("Invalid number of rows")
    
#Loop to count the number of rows
for i in range(1,n+1):
    #loop to print the numbers equal to the number of row but in reverse order
    for j in range(i,0,-1):
        print(j,end=" ")
    #Move the next row to next line
    print("\n")
    






