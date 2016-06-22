__author__ = 'Anubhav'


class Student:
    student_count = 0

    def __init__(self,name):
        self.name = name;
        Student.student_count += 1

    def getName(self):
        return self.name


#s = Student("anubhav")

#print s.getName()

s = Student("anubh")
Student.__init__(s,'a')

print s.getName()

