text = input("Enter the String : ")

# revese the string
print(text[::-1]) 

# count the vowels 
text = text.lower()
vowels = ['a','e','i','o','u']
count = 0
for i in text :
    if (i in vowels):
        count = count + 1

print(f"{count} Vowles present in the String ")