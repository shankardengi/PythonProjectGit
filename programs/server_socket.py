import socket
import pdb
from student_admission_entry import student,logger

logger.info("starting")
socket_object = socket.socket()
#pdb.set_trace()
host = socket.gethostname()
print(host)
port = 12345
socket_object.bind((host,port))
socket_object.listen(5)
connection, addr = socket_object.accept()
while True:
    data = connection.recv(1024).decode()
    roll_number,name = data.split(" ")
    stud,college =student.find(name,roll_number)
    student = str(stud)
    print(college,student)
    connection.send(student.encode())
    logger.info("succefll")
    #print("Connection established",addr)
    #c.send(bytes("Socket Programming in Python","utf-8 "))
connection.close()