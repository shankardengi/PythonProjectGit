if __name__=="__main__":
    try:
        num1 = int(input("Enter Number 1:"))
        num2 = int(input("Enter Number 2:"))
        num3 = int(input("Enter Number 3:"))

    except ValueError as error:
        print("Error found :",error)

    if (num1>num2) and (num1>num3):
        print("{} is greater".format(num1))
    elif(num2>num3):
        print("{} is greater".format(num2))
    else:
        print("{} is greater".format(num3))