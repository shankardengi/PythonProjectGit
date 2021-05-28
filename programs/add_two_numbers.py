if __name__=="__main__":
    try:
        num1 = int(input("Enter Number 1 for addition:"))
        num2 = int(input("Enter Number 2 for addition:"))
        sum = num1 + num2
    except ValueError as err:
        print("Exception Caughg",err)
    except:
        print("Exception found")
    else:
        print(f"sum of {num1} and {num2} is :{sum}")

