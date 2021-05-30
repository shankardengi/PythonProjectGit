import socket
import pdb
from student_admission_entry import student,logger

socket_object = socket.socket()
host = socket.gethostname()
port = 12345
socket_object.connect((host,port))
name = input("Enter Name to fine:")
roll_number = input("Enter roll number search:")
data = bytes(f"{roll_number} {name}", 'utf-8')
data = socket_object.sendall(data)
data = socket_object.recv(1024).decode()
logger.info("student found succefully")
logger.info(f"student info is :{data}")


#stud,college = socket_object.recv(1024).decode('utf8')
socket_object.close()
