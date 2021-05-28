if __name__=="__main__":
    try:
        list_size = int(input("Enter size of list:"))
        number_list = [int(input("Enter Element to list:")) for _ in range(1,list_size)]
        divisible_num = int(input("Enter Divisible Number :"))
        divisible_list = filter(lambda x:x%divisible_num==0,number_list)
        print("Divisble list numbers List")
        for i in divisible_list:
            print(i)
    except ValueError as error:
        print("type format error",error)
    except IndexError as error:
        print("Index error",error)