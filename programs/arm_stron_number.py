#Python Program to Check Armstrong Number

if __name__ == "__main__":
    try:
        num = int(input("Enter number to check Armstrog:"))
        temp = num
        sum=0
        while(temp>0):
            #global sum
            digit = temp%10
            sum = sum + digit ** 3
            temp //=10

        print("{} and {}".format(sum,num))
        print("{} is ArmStrong Number ".format(num)) if sum ==num else print("{}number is not arm Strong".format(num))

    except ValueError as error:
        print("invalid input",error)
