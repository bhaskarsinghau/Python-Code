file_out = open("student1.pdf","w")
for i in range (5):
    name = input("Enter name of student: ")
    file_out.write(name)
    file_out.write('\n')
file_out.close()    
