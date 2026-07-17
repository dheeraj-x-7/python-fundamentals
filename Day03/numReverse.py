# Reverse the number using loop
num = int(input("Enter the number : "))
dum_num = num
rev_num = 0

for i in range(len(str(dum_num))):
    remainder = num % 10
    print(remainder)
    rev_num = rev_num*10 + remainder
    num = int(num/10)
else :
    print("Reversed number is : ",rev_num) 