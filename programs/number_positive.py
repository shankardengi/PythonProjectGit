if __name__=="__main__":
    try:
        number = int(input("Enter Number to testive:"))
        if(number>0):
            print("Number is positive")
        else:
            print("Number is not positive")
    except ValueError as error:
        print("error found",error)
