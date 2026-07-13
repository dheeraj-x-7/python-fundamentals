num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operator = input('''
select operator : + , - , * , /
''')
print("Answer : ")
if(operator == '+'):
    print(num1 + num2)
elif(operator == '-'):
    print(num1 - num2)
elif(operator == '*'):
    print(num1 * num2)
elif(operator == '/'):
    print(num1/num2)
else :
    print("Invalid operator")