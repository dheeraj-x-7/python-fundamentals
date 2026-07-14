def sum(*args):
    """This function return the summition of all input
    Input : int
    Output : int"""
    sum=0
    for i in args:
        sum+=i
    return sum
x = sum(2,3,4,5,6,7,8)
print(x)
