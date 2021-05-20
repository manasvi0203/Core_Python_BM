# lists are stored

student_info = ["Ajay", 23, 12, 1234]

file = open("student_info.dat","w")
a = str(student_info)
file.write(a)
file.close()



