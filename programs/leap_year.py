if __name__=="__main__":
    try:
        year = int(input("Enter Year to check leap or not :"))
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    print("Leap year")
                else:
                    print("Not Leap Year")
            else:
                print("Leap Year")
        else:
            print("Not Leap Year")
    except ValueError as error:
        print("Error found ",error)
