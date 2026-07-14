
# checking the string is palindrome or not
x = lambda str: 'Palindrome' if str == str[::-1] else ' not palindrome'
strr = input("Enter the text : ")
print(x(strr))