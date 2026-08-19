def add(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

def multiply(*nums):
    mul = 1
    for i in nums:
        mul *= i
    return mul

def subtract(a,b):
    return a-b

def div(a,b):
    return a/b