if __name__ =="__main__":
    try:
        a = int(input("Enter Number A :"))
        b = int(input("Enter Number B :"))
    except ValueError as error:
        print("Error found:",error)
    else:
        #a = a+b
        a = a*b
        b = a/b
        a = a/b
       # b = a-b
        #a = a-b
        print("Swaped data a :{} b:{}".format(a,b))
