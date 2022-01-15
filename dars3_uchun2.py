

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def login(self):
        return f"{self.username} login"
    
    def logout(self):
        return f"{self.username} logout"
    
class Student(User):
    def __init__(self, username, email, password, direction, course):
        super().__init__(username, email, password)
        self.direction = direction
        self.course = course
        
    def task_read(self):
        return f"{self.username} task read"
    
    def task_send(self):
        return f"{self.username} send task"

    def about(self):
        return f"{self.direction} da {self.course} kurs talabasi"
    
class Teacher(User):
    def __init__(self, username, email, password, specalist, degree):
        super().__init__(username, email, password)
        self.specialist = specalist
        self.degree = degree
    
    def task_check(self):
        return f"{self.username} task check"

    def about(self):
        return f"Mutaxasisligi: {self.specialist} Darajasi: {self.degree}"

class Assient(Teacher):
    def __init__(self, username, email, password, specalist, degree):
        super().__init__(username, email, password, specalist, degree)

    def about(self):
        return f"Mutaxasisligi: {self.specialist} Assient bu Faqat Amaliyotdan dars bera oladi"


class Professor(Teacher):
    def __init__(self, username, email, password, specalist, degree):
        super().__init__(username, email, password, specalist, degree)

    def about(self):
        return f"BU {self.username} faqat Maruzadan dars beradi!"


student1 = Student("student1", "student1@gmail.com", "*********", "DAs injiniring", 2)
teacher1 = Teacher("teacher1", "teacher@hmail.com", "******", "Dev", "Doctor")
ass = Assient("assient1", "ass@gmail.com", "12345678", "Dev", "Assient")
pro = Professor("Pro1", "pro@gmail.com", "123", "Matematik", "Professor")
print(student1.login())
print(student1.task_read())
print(student1.task_send())
print(student1.logout())
print(student1.about())

print(teacher1.login())
print(teacher1.task_check())
print(teacher1.logout())
print(teacher1.about())

print(ass.about())
print(pro.about())
