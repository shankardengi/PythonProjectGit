if __name__ == "__main__":

    rows = int(input("Enter Number of rows:"))
    count = 0
    for i in range(0,rows):
        for n in range(rows-2,i,-1):
            print("-",end=" ")
        print()



