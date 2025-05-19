# class Student:
#     name="Yuvraj"

# s1=Student()
# print(s1)
# print(s1.name)


# class car:
#     color="blue"
#     brand="Roles loyel"

# car1=car()
# print(car1.color)
# print(car1.brand)

class Student:
    # defult constructor
    def __init_subc__(self):
        pass

    # parameterized constructor
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks

s1 = Student("Renu",92)
print(s1.name,s1.marks  )
