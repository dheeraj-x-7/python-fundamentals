# cheking a number is armstrong or not
num = int(input("Enter a number : "))
dummy = num
digit = len(str(num))
armStrong = 0
for i in range(digit):
    rem = num % 10
    num = int(num/10)
    armStrong += rem**digit
else : 
    print(armStrong)
    if(dummy == armStrong):
        print("The number is armstrong")
    else:
        print("the number is not an armstrong number")