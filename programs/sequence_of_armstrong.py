def get_armstrong(num,order):
    sum =0
    while(num>0):
        digit = num%10
        sum = sum + digit **order
        num = num//10
    return sum

if __name__=="__main__":
    try:
        lower_num = int(input("Enter lower number for Sequence of armastrong:"))
        upper_num = int(input("Enter upper number for Sequence of armastrong:"))
        for num in range(lower_num,upper_num+1):
            order = len(str(num))
            arm_strong = get_armstrong(num,order)
            #print(num,arm_strong)
            print("{} is armstring".format(num)) if num==arm_strong else None
    except ValueError as error:
        print("error found ",error)



