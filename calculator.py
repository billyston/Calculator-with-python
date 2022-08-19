# Simple calculator

operation = [1, 2, 3, 4]
num1, num2, total = 0, 0, 0

userChoice = int( input( "Please enter 1, 2, 3 or 4: " ))

def calResult() :

    num1 = int( input("Enter number 1:") )
    num2 = int( input("Enter number 2:") )

    if userChoice == 1:
       return num1 + num2

    elif userChoice == 2:
        return num1 - num2 

    elif userChoice == 3:
        return num1 * num2 

    elif userChoice == 4:
        return num1 / num2 


if userChoice in operation :
    print( calResult() )

else :
    print( "Undifined operation" )