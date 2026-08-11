# ZeroDivisionError and TypeError

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return "can't divisible by zero"
    except TypeError as e:
        return 'Invalid inputs'
print(division(0,10))

# IndexError
l = [1,2,3,4,5,6,7,9,10]
for i in range(10):
    try:
        print(l[i])
    except IndexError as e:
        print("index out of bound...")
        break

# KeyError
student = {"name":"Dheeraj","age":20,"class": "3rd year","course":"BCA"}
try:
    print(student["email"])
except KeyError as e:
    print("This attribute (key) not exist")


# FileNotFoundError
try:
    f = open("sample.txt",'r')
except FileNotFoundError as e:
    print("File not found...")
else :
    print(f.read())
    f.close()
try:
    age = -3
    if age<0:
        raise Exception("age can't be negative")
except Exception as e:
    print(e)
