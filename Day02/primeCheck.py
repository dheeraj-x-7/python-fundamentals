# cheking a number is prime or  not 
def prime(x):
    half = int(x/2)
    for i in range(2,half):
        if x%i == 0 : return False
    return True
x = int(input("Enter a number : "))
result = lambda x: 'prime' if prime(x) else 'not prime'
print(result(x))