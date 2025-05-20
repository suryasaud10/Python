class Student:
    collage = "NAST"
    # class attribute
    name="Yuvraj" 

    def __init__(self, name, marks):
        # obj attribute
        self.name = name
        self.marks = marks

s1=Student("Kiran", 87)
print(s1.name, s1.marks)

        