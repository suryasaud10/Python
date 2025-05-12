# # # # if statement
age = 13
if( age>=18):
    print("can vote and apply for license")
else:
    print("cant vote and drive")



# # # # # grade student
marks=int(input("Enter the marks of student:"))
if(marks>=90):
    grade="A"
elif(marks<90 and marks>=80):
    grade="B"
elif(marks<80 and marks>=70):
    grade="C"
elif(marks<70 and marks>=40):
    grade="D"
else:
    grade="fail"


print("The grade of student is:",grade)



# # # # SOME OTHER QUESTION

# 1. odd even 
n=int(input("Enter a Number:"))
if(n%2==0):
    print("even")

else:
    print("odd")


# # # 2. Gratest among Three
a=7
b=6
c=5
if(a>b and a>c):
    print("A is the gratest")

elif(b>a and b>c):
    print("B is greatest")

else:
    print("c is greatest")

# 2. Multiple of 7 or not
s=20
if(s % 7 ==0):
    print("s is multiple of 7")

else:
    print("s is not")