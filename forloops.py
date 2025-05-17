list = [1,2,3,4,5]
for n in list:
    print(n)

fruits = ["apple","banana","watermelon","orange","mango"]
for eat in fruits:
    print(eat)


str =("Suryasaud")
for t in str:
    if(t=="y"):
        print("y is found")
        break
    print(t)
else:
    print("Not found")

num = [1,4,9,16,25,36,49,64,81,100]
x=36
i=0
for n in num:
    if(n==x):
        print("number found at index",i)
    i+=1

# Range
for i in range(1,10,2):
    print(i)


# print 1- 100

for i in range(1,101):
    print(i)

# print 100-1
for r in range(100,0,-1):
    print(r)

# multiplication table
R=int(input("Enter the number:"))
for s in range(1,11):
    print(R*s)


Pass Statement

for q in range(4):
    pass
# pass is used for  doing nothing or skip
print("Hello engineers")

# sum of n numbers

n=7
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

p =7
i=1
sum=0
while i <= p:
    sum += i
print("total sum is:",sum)

# factorial
n=int(input("Enter the number:"))
fact=1
i=1
while i<=n:
    fact *=i
    i +=1
print(fact)



fact=1
for n in range(1,6):
    fact*=n
print(fact)