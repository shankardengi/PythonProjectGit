if __name__ == "__main__":
    try:
        num = int(input("Enter Number for power of sequence:"))
        data = list(map(lambda x:2 ** x ,range(0,num)))
        print(type(data))
        print("Square of sequence :")
        for i in range(num):
            print("2 raise power of {} is {}".format(i,data[i]))
    except ValueError as error:
        print("error found ",error)
    except IndexError as error:
        print("Index error ",error)