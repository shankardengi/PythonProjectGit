import  mysql.connector as mysqls
import os
from logger_employee import logger_employee

logger_object = logger_employee("employee.log","employe_log")
logging = logger_object.logger

class mysql:
    def __init__(self):
        self.con = mysqls.connect(host="localhost",user="root",password="shankar@123",database='emp')
        self.cursor = self.con.cursor()
    @property
    def cursor(self):
        return self.__cursor
    @cursor.setter
    def cursor(self,cursor):
        self.__cursor =cursor

    def insert(self,emp):
        querry = f"insert into employee values('{emp.name}',{emp.id},' {emp.location}')"
        #querry = "insert into employee (emp_name,emp_id,emp_location) values(?,?,?);"
        self.cursor.execute(querry)
        self.con.commit()
        print("1 record inserted")
        logging.info("1 record inserted")

    def select(self):
        querry = "select * from employee"
        self.cursor.execute(querry)
        data = self.cursor.fetchall()
        if len(data)>0:
            print("Table Records is:")
            logging.info("Table Records is:")
            for i in data:
                print(i)
                logging.info(i)
        else:
            print("Table does not have record not found")
            logging.info("Table does not have record not found")

    def delete_row(self,id):
        querry = "DELETE FROM employee WHERE emp_id={id}"
        print("1 record deleted")
        logging.info("1 record deleted")

    def update_record(self,name,id):
        querry = f"UPDATE employee SET emp_name = '{name}' WHERE emp_id = {id}"
        self.cursor.execute(querry)
        print("1 record updated")
        logging.info("1 record updated")

    def display_record(self,id):
        querry = f"select * from employee where emp_id={id}"
        self.cursor.execute(querry)
        data = self.cursor.fetchall()
        if len(data)>0:
            print(data)
            logging.info(f"Displaying recording {data}")
            return 1
        else:
            print("Data With above id is not present")
            logging.info("Data With above id is not present")
            return 0

class employe:
    def __init__(self):
        self.mysql = mysql()
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        print("setting name")
        self._name = name
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        self._id = id
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self,location):
        self._location = location
    def __str__(self):
        return f"Name of employe {self.name} and id is {self.id} and he is staying in {self.location}"

    def read_emp(self):
        self.name = input("Enter Employee Name:")
        self.id = int(input("Enter Employee Id:"))
        self.location = input("Enter location:")

if __name__ == "__main__":
    while True:
        emp = employe()
        db = mysql()
        print("\n")
        print("1)Do you want to insert student Record:")
        print("2)Do you want to Modify student Record:")
        print("3)Do you want to Delete the student Record")
        print("4)Do you want to Search student Recored")
        print("5)Do you want to display students")
        print("6)Exit")
        ch = int(input("Enter choice:"))
        print("\n")
        if ch == 1:
            emp.read_emp()
            db.insert(emp)
        elif ch == 2:
            id = int(input("Enter Id to modify"))
            if db.display_record(id):
                name = input("Enter Employee Name for modification:")
                db.update_record(name, id)
                print("after modification data is")
                logging.info("after modification data is")
                db.display_record(id)

            # db.delete_row(id)
        elif ch == 3:
            id = int(input("Enter Id to Delete:"))
            if db.display_record(id):
                db.delete_row(id)
        elif ch == 4:
            id = int(input("Enter Id to Search:"))
            if db.display_record(id):
                print("Record found")
                logging.info("Record found")
        elif ch == 5:
            db.select()
        elif ch == 6:
            break




