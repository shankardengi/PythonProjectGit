if __name__ =="__main__":
    try:
        number = int(input("Enter Number to check even or odd :"))
        print("even") if number%2==0 else print("odd")
    except ValueError as error:
        print("Enter number :",error)
    except :
        print("error found")