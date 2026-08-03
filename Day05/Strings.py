txt = input("Enter a string -> ")
lower_txt = txt.lower()
# Count consonants ->
vowels = 'aeiou'
count = 0
for char in  lower_txt:
    if char not in vowels: count += 1

print(f"total consonants in string -> {count}")

# words in string 
count = 0
for i in txt:
    if(i==" "): count += 1
print(f"word in text -> {count}")

# numbers in string ->
num =[]
for char in txt:
    if char.isdigit(): num.append(int(char))
print(f"numbers in string - > {num}")

# Word Reversal - >
words = txt.split(" ")
words = words[::-1]
rev = ""
for word in words:
    rev += word + " "

print(rev)
