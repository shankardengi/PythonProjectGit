if __name__=="__main__":
    try:
        num = int(input("Enter size of fibnoci:"))
        a,b=0,1
        count = 1
        if(num<=0):
            print("Enter Possitive number")
        elif num == 1:
            print("Fibonacii serious upto {} is : {}".format((num)))
        else :
            print("Fibonaci serious upto {} is ".format(num))
            while(count<=num):
                print(a)
                c = a+b
                a = b
                b = c
                count +=1
    except ValueError as error:
        print("Error found ",error)
