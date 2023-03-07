
employeeFile = open("employees.txt", "r+")
for i in employeeFile.readlines():
    print(i)


employeeFile.close()