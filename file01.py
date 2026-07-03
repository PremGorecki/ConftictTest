

class user():
    def __init__(self, name, age):
        self.name = name + 'Prem'
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")



class admin(user):
    def __init__(self, name, age, admin_level):
        super().__init__(name, age)
        self.admin_level = admin_level

    def display_info(self):
        super().display_info()
        print(f"Adminek Level: {self.admin_level}")
