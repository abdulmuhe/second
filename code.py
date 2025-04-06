# print(a,b)
class Student:
    # Constructor (__init__)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print("Constructor called! Object created.")
    
    # Method (regular function)
    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

# Creating an object (constructor is called automatically)
s1 = Student("Abdul", 21)

# Calling the method manually
s1.display()