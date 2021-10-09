class Student(object):

    def __init__(self, name, age,grades=None):
        self.name=name,
        self.age=age,
        self.grades=grades or {}
    
    def studentName(self):
        print(self.name)

john = Student("John", 12,{"math":3.3})


john.studentName()
