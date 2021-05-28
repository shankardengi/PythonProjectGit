def accept_list(list_size):
    list = []
    while list_size>len(list):
        data  = input("Enter Elements")
        list.append(data)


if __name__ == "__main__":
    list_size = int(input("Enter Size of list:"))
    list1 = accept_list(list_size)
    list_size = int(input("Enter Size of list:"))
    list2 = accept_list(list_size)
    print("Concated list")
    for i in len(list1.extend(list2)):
        print(list[i])

