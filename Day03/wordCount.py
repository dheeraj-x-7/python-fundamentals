# counts the number of word in a string
text = input("Enter the text -> ")
text = text.lstrip()
if(text == ""):
    print("Zero words in text")
else:
    words =1
    prev = ""
    for i in text:
        if(i==" " and prev!=" "):
            words +=1
    print(f"total words -> {words}")