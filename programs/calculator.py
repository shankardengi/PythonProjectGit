def calc_menu():
    print("---------------")
    print("Enter 1 for Add")
    print("Enter 2 for Subtract")
    print("Enter 3 for Mul")
    print("Enter 4 for Division")
    print("To Exit Enter X")
    print("----------------")
    return input("Please Enter your choice:")
def accept_input():
    try:
        num1 = int(input("Enter First Operand:"))
        num2 = int(input("Enter Second Operand:"))
    except ValueError as error:
        print("invalid input", error)
    return (num1,num2)

if __name__=="__main__":
    ch = ''
    while(ch!="x"):
        print(ch)
        ch = calc_menu()
        if ch=='1':
            num1,num2=accept_input()
            print("Sum of {a} and {b} is {c}".format(a=num1,b=num2,c=num1+num2))
        elif ch=='2':
            num1, num2 = accept_input()
            print("Subraction of {a} and {b} is {c}".format(a=num1,b=num2,c=num1-num2))
        elif ch=='3':
            num1, num2 = accept_input()
            print("Multiplication of {a} and {b} is {c}".format(a=num1,b=num2,c=num1*num2))
        elif ch=='4':
            num1, num2 = accept_input()
            print("Division of {a} and {b} is {c}".format(a=num1, b=num2, c=num1 / num2))




