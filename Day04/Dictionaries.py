#count frequency of characters in a string 
txt = input("Enter a string -> ")
txt = txt.strip()
freq = {}
for i in txt:
    if i in freq.keys():
        freq[i] = freq[i]+1
    else:
        freq[i] = 1

for key,values in freq.items():
    print(f"{key} --> {values}")