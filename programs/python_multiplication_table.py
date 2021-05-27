#Python Program to Display the multiplication Table
if __name__=="__main__":
    try:
        num = int(input("Enter Required Table:"))
        if(num>=1):
            for i in range(1,11):
                print("{} X {} = {}".format(num,i,num*i))
        else:
            print("Enter Possitive numbers")
    except ValueError as error:
        print("Error found ",error)