if __name__=="__main__":
    fact = 1
    try:
        num = int((input("Enter Number for factorial:")))
        if num ==0:
            print("factorial of 0 is 1")
        else:
            for i in range(1,num+1):
                fact = fact *i
            else:
                print("factorial of {} is {}".format(num,fact))
    except ValueError as error:
        print("Error found ",error)