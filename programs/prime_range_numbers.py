if __name__=="__main__":
    try:
        lower_number = int(input("Enter Lower Number of prime :"))
        higher_number = int(input("Enter Higher Number of Prime:"))
        for num in range(lower_number,higher_number+1):
            if num>1:
                for i in range(2,lower_number):
                    if num%i == 0:
                        print("{} is not prime number".format(num))
                        break
                else:
                    print("{} is prime number ".format(num))

    except ValueError as error:
        print("Invalid Type Error",error)

