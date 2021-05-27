#Python Program to Find the Sum of Natural Numbers
if __name__=="__main__":
    try:
        num = int(input("Enter Number to find natural number:"))
        sum = 0
        #using genrator
        num = (num for num in range(num,0,-1))
        while(True):
            try:
                sum +=next(num)
            except StopIteration:
                break
        #using while loop
        # while(num>0):
        #     sum = sum + num
        #     num -=1
        #using for loop
        # for i in range(num+1,0,-1):
        #     sum = sum + num
        #     num -=1

        print("sum of natural number is {} ".format(sum))
    except ValueError as error:
        print("error found",error)

