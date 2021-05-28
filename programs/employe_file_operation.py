class employee:
    def __init__(self,name,id,location,salary):
        self.name = name
        self.id = id
        self.location = location
        self.salary = salary
        self.hra = salary * 100

    def __str__(self):
        return "employe name:{},employe id :{},employe location:{},employe salary :{},employe hra :{}".format(self.name,self.id,self.location,self.salary,self.hra)

    def write_to_file(self):
        with open("student.txt",'a') as file:
            file.write(self.__str__()+"\n")

def search_from_file(id):
    try:
        file = open("student.txt",'r')
        while 1:
            data = file.readline()
            if id in data:
                return (1,data)
            elif data =='':
                break
        return((0,None))
    except:
        print("exception found while reading file")
def read_emp():
    name = input("Enter name:")
    id = input("Enter id:")
    salary = input("Enter Salary:")
    location = input("Enter location:")
    return (name,id,salary,location)

def read_from_file():
    try:
        file = open("student.txt",'r')
        data = file.read()
        print(data)
    except:
        print("exception found")

if __name__ == "__main__":
    print("Enter Choice")
    ch = 1
    while ch!=0:
        ch = int(input("1:Read Emp and Write to file \n2:Read Emp record from file\n:"))
        if ch==1:
            a,b,c,d=read_emp()
            emp = employee(a,b,c,d)
            emp.write_to_file()
        elif ch==2:
            read_from_file()
        elif ch==3:
            flag,data = search_from_file("123")
            if flag == 1:
                print("result found and data is {}".format(data))





