def fibonacci(x=2):
    l =[0,1]
    for i in range(1,x):
        x= l[i-1] + l[i]
        l.append(x)
    return l

x = int(input("Enter the number of terms : "))
print(fibonacci(x))