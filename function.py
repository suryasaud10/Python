def sum(a, b):
    sum=a + b
    print(sum)
    return sum

sum(3, 4)

sum(5, 6)


# average of three function

def avg(a,b,c):
    avg=(a+b+c)/3
    print(avg)
    return avg

avg(1,2,3)

# print the length of list
cities = ["ktm", "dhn", "mnr"]
def lenh(length):
    print(len(length))
lenh(cities)


# Factorial


def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    print(fact)
    return fact

calc_fact(5)



