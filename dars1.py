#
# user = ["Ali", "Aliyev", 25]
#
# user = {
#     "first_name": "Ali",
#     "last_name": "Aliyev",
#     'age': 25,
#     "full_name": "Ali Aliyev"
# }


# class User:
#     def __init__(self):
#
# user = User()
# user.first_name = "Ali"
# user.last_name = "Aliyev"
#
# print(f"{user.first_name} {user.last_name}")


# class User:
#     def __init__(self):
#         self.first_name = "Ali"
#         self.last_name = "Aliyev"
#
#
# user = User()
# print(f"{user.first_name} {user.last_name}")

# class User:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     @property  # new
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     @property
#     def about(self):
#         return f"Men ismim {self.first_name} familiyam {self.last_name} Yoshim {self.age} da"
#
#     def greet(self, name):
#         return f"{name}: Salom {self.first_name}"
from dataclasses import dataclass


@dataclass(frozen=True) #new
class User:
    first_name: str
    last_name: str
    age: int

    @property  # new
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def about(self):
        return f"Men ismim {self.first_name} familiyam {self.last_name} Yoshim {self.age} da"

    def greet(self, name):
        return f"{name}: Salom {self.first_name}"


user1 = User("Ali", "Aliyev", 25)
user2 = User("Vali", "Valiyev", 22)


print(f"User: {user1.full_name} Age: {user1.age}")
print(f"User: {user2.full_name} Age: {user2.age}")

print(user1.about)
print(user2.about)

print(user1.greet("Alisher"))
print(user2.greet("Alisher"))
