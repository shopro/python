class SchoolMember:
    def __init__(self,name,age): 
        self.Name = name
        self.Age = age
        print("Initialized SchoolMember: " + self.Name)
        
    def Output(self): 
        print("Name:"  + self.Name+"   "+"Age:" + self.Age)

class Teacher(SchoolMember): 
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.Salary=salary
        print("Initialized Teacher: " + self.Name)

    def Output(self):
        SchoolMember.Output(self)
        print("Salary: " + self.Salary)

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.Marks=marks
        print("Initialized Student: " + self.Name)

    def Output(self):
        SchoolMember.Output(self)
        print("Marks: " + self.Marks)


t = Teacher("kwon","25","50000000")
s = Student("Tae","15","75")

t.Output()
s.Output()





