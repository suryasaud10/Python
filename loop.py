# While loops
i = 0
while i<=15:
    print("hello",i)
    i = i+1
    print(i)

# number from 1 to 5
a=1
while a<=5:
    print(a)
    a=a+1

# 1-100

s=1
while s<=100:
    print(s)
    s+=1

# 100 t0 1
t = 100
while t>=1:
    print(t)
    t-=1

#  multiplication table of number n

n=int(input("Enter the number"))
i=1
while i<=10:
    print(n*i)
    i+=1

# squre of 1-10

r=1
while r<=10:
    print(r**2)
    r+=1


num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,36]
x=36

i=0 
while i <= len(num):
    if(num[i] == x): 
        print("index is:",i)
    else:
        print("finding.......")
    print(i)
    print(num[i])
    i+=1