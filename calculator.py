print("Arithmetic operations to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Quotient")
print("5. Remainder")
print("6. Exponential")
print("ENTER TWO NUMBERS : ")

while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    choice = int(input("Enter your choice: "))
    if (choice==1):
        sum = a + b
        print("result of addition is: ", sum)
    elif (choice==2):
        sub = a - b
        print("result of subtraction is: ", sub)
    elif (choice==3):
        prod = a * b
        print("the product is: ", prod)
    elif (choice==4):
        quo = a / b
        print("quotient is: ", quo)
    elif (choice==5):
        rem = a % b
        print("remainder is: ", rem)
    elif (choice==6):
        expo = a ** b
        print("exponential is: ", expo)
    else:
        print("Invalid choice \n Please try again")
    
    ch = input("Do you want to continue?(y/n): ")
    
    if ch=="n":
        print("Thankyou for using")
        break
    


    
 
 
 
 
 