from uuid import uuid4


class Student:
    """ Student klasi """
    __student_count = 0

    def __init__(self, first_name, last_name, age, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__phone = phone
        self.__id = uuid4()
        Student.__student_count += 1

    def __str__(self):
        """Student haqida ma'lumot qaytaradi! """
        return f"{self.first_name} {self.last_name}"

    def get_id(self):
        return self.__id

    def get_phone(self):
        return self.__phone

    def phone_update(self, phone):
        self.__phone = phone

    @classmethod
    def get_student_count(cls):
        return cls.__student_count


student1 = Student("Bobur", "Amirov", 26, "977775566")
print(student1)

student2 = Student("Ali", "Aliyev", 20, "977775566")
student3 = Student("Vali", "Valiyev", 20, "977775566")
student4 = Student("Ali", "Valiyev", 20, "901234567")
print(Student.get_student_count())

# print(f"ID {student1.get_phone()}")

student1.phone_update("901112233")
# print(f"ID {student1.get_phone()}")
