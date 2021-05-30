import logging
import traceback
import os
import pdb

logger = logging.getLogger("student")
logger.setLevel(logging.DEBUG)

format = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

log_file_handler = logging.FileHandler("logs")
log_file_handler.setFormatter(format)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(format)

logger.addHandler(log_file_handler)
logger.addHandler(stream_handler)

class student:
    def __init__(self,name,roll_number,city,college):
        self.name = name
        self.roll_number = roll_number
        self.city = city
        self.college = college
        logger.info("Student instance created")
    def __str__(self):
        return f"{self.name} {self.roll_number} {self.city} {self.college}"
    @staticmethod
    def write(student):
        #pdb.set_trace()
        try:
            file = open(os.path.join(os.getcwd(),"College",student.college)+".txt","a")
            file.write(f"{student.name} {student.roll_number} {student.city} {student.college} \n")
            file.close()
            logger.info(f"{student}record inserted")

        except FileNotFoundError as e:
            logger.error(traceback.print_exc())
        except Exception:
            logger.error(traceback.print_exc())
        finally:
            file.close()

    @staticmethod
    def find(student_name,roll_number):
        college_lists = os.listdir(os.path.join(os.getcwd(), "College"))
        #pdb.set_trace()
        try:
            for college_name in college_lists:
                file = open(os.path.join(os.getcwd(),"College",college_name),"r")
                logger.info("finding student record")
                #data = file.read()
                for row in file.read().split("\n")[0:-1]:
                    name,stud_roll_number,city,college,dot = row.split(" ")
                    if student_name == name and roll_number == stud_roll_number:
                        logger.info(f"student found in {college_name.upper()}")
                        file.close()
                        #pdb.set_trace()
                        return (student(name,stud_roll_number,city,college),college_name)
                else:
                    logger.info(f"Searching done in {college_name.upper()} college student not found")
                    file.close()
        except FileNotFoundError:
            logger.error(traceback.print_exc())
        except Exception:
            logger.error(traceback.print_exc())
        logger.info("student not found")
        return None

if __name__ == "__main__":
    logger.info("student program started")
    while True:
        print("1)insert student record into file")
        print("2)find student record from file")
        print("3)exit")
        ch = int(input("Enter choice:"))
        if ch==1:
            name = input("Enter student name:")
            roll_number = input("Enter student roll number:")
            city = input("Enter city:")
            college = input("Enter college")
            stud = student(name,roll_number,city,college)
            student.write(stud)
        elif ch==2:
            name = input("Enter Name to fine:")
            roll_number = input("Enter roll number search:")
            stud,college = student.find(name,roll_number)
            logger.info(f"{stud} found in {college}")
        elif ch==3:
            break

