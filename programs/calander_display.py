import calendar
if __name__=="__main__":
    try:
        x,y = tuple(input("Enter month and year to display calander").split((',')))
        print(calendar.month(int(x),int(y)))
    except ValueError as error:
        print("found error",error)
