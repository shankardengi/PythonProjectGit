def read_set_elements(size_set1):
    temp_set = set()
    for i in range(1,size_set1+1):
        set1 = int(input("Enter {} th Element in Set1:".format(i)))
        temp_set.add(set1)
    return temp_set




if __name__ =="__main__":
    size_set1 = int(input("Enter size of Set 1:"))
    set1 = read_set_elements(size_set1)
    size_set2 = int(input("Enter size of Set 2:"))
    set2 = read_set_elements(size_set2)
    while(1):
        print("Enter 1 union ")
        print("Enter 2 Intersection")
        print("Enter 3 Subtraction")
        print("Enter 0 Exit")
        ch = int(input("Enter your choice:"))
        if ch ==1:
            result_set = set1 | set2
            print(result_set)

        elif ch ==2:
            result_set = set1 & set2
            print(result_set)

        elif ch ==3:
            result_set = set1 - set2
            print(result_set)
        elif ch == 0:
            break
        else:
            print("invalid input")
            continue