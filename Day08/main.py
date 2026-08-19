import package.calculator as cal
from package.utils import input_num,input_name

num1 = input_num()
num2 = input_num(2,100)
num3 = input_num(0)
num4 = input_num(end=50)
sum = cal.add(num1,num2,num3,num4)

print("sum  -> ",sum)
name = input_name()
print(name)