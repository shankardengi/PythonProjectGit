import math

if __name__=="__main__":
    try:
        a = float(input("Enter A:"))
        b = float(input("Enter B:"))
        c = float(input("Enter C:"))
        s = (a+b+c)/2
        area = math.sqrt((s*(s-a) * (s-b) * (s-c)))
    except ValueError as err:
        print(err)


    else:
        print("Area of Triangle is :",area)


