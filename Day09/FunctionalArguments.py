import sys
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0,str(project_root))

from Day08.package import utils as u
# positional arguments
def greet(name,age,/):
    return f"{name} is {age} years old"

name = u.input_name()
age = u.input_num()
print(greet(name,age))

# keyword argument 
def car_model(brand="bmw",model="m5"):
    return f"congratulations you got brand new {brand} {model}"
print(car_model(brand="Mahindra", model="scorpio N"))


# varibale length arguments 
def sum1(*num):
    # *num can take multiple variables and store it in a tuple so here num = (num1,num2,num3...)
    """it take numbers and return their sum"""
    sum=0
    for i in num:
        # iterating the tuple by for loop
        sum+=i
    return sum
print(sum1(80,55,8,9))

# variable length keyword arguments 

def mul1(**num):
    # **num take multiple key value pair and store it in dictonary here -> num = {key1=value1,key2=value2...}
    mul = 1
    for key in num.keys():
        mul *=num[key]
    return mul
print(mul1(n1=2,n2=3,n3=4,n4=5,n5=6,n6=7))

# unpacking list

l1 = [1,2,4,'f',5]
print(l1)
print(*l1)

v1,*v2,v3 = l1
print(v1)
print(v2)
print(v3)

l2 = [10,20,40,50]
combined1 = l1+l1
print(combined1)
combined2 = [*l1 ,*l2]
print(combined2)

print(sum1(*l2))

# unpacking dictonary 
d1 = {'name': 'robert','age':22}

d2 = {'height':167,'weight':72}
combined3 = {**d1, **d2}
print(combined3)

def info(name,age,height,weight):
    print("name -> ",name)
    print("age ->",age)
    print("weight",weight)
    print("height",height)

info(**combined3)

## Scope

# local scope ->
#                a variable that declares in a function it can't access from outside the function
a =10
def local_scope(player):
    game = "cricket" # local  variable
    print(f"{player} plays {game}")
    a = 20
    print("inside -> ",a)
    variables = locals() 
    # locals function return a dictonary of identifiers and their values inside the block of code where it created 
    print(variables)

    print("inside ->",len(globals())) # globals return a dictonary of all identifiers and their values in the script or program 

local_scope("Dhoni")
print("outside -> ",a)
j='' # one more variable  declared the number of items in dictonary tha t global() return is increase by 1
print("outside ->",len(globals()))

# global scope ->
                    # a variable that can access from anywhere in program after declaration.
num2 = 50
def global_scope():
    #num2 += 50 # it raise UnboundLocalError
    global num2
    num2 += 50
    print("inside -> ",num2)
    print("number of variable in global_scope function",len(locals()))

global_scope()
print("outside -> ",num2)

# ENCLOSED scope ->
                    # a variable which is not a local nor a global variable called enclose or non local variable.
def fun_a():
    a=10
    print(a)
    def fun_b():
        nonlocal a
        a=20
        b=100
        print(a)
        print(b)
    fun_b()
    print(a)
fun_a()

# Scope resolution = (LEGB) => Local -> Enclosed -> Global -> Built-in

## Built-in Scope -> these variable or function can be access from anywhere in program 
#                   ex -> print(), len() (these are  built in functions) 
