if __name__=="__main__":
    try:
        number = int(input("Enter Number to check prime:"))
    except ValueError as error:
        print("Error found ",error)

    for i in range(2,number):
        if number%i==0:
            print("Number is not Prime")
            break
    else:
        print("{} Number is prime".format(number))