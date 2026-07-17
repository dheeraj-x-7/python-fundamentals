# cheking a number is strong or not
num =int(input("Enter the number : "))
dummy = num
f = 0
def fact(x):
    """This funtion calculate the factorial of a positive number
    Input - positive Integer
    Output - positive Integer"""
    if(x< 0 ):
        return None
    elif(x == 0):
        return 1
    else:
        fact = 1
        for i in range(1,x+1):
            fact *=i
        return fact



for i in range(len(str(dummy))):
    digit = num%10
    f += fact(digit)
    num = int(num/10)
if(dummy==f) :
    print("this is a strong number ")
else:
    print("Not a strong number")



