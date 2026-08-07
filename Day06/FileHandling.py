# file creation and writing text in file 
with open('sample.txt','w') as f:
    f.write("This is a sample file \n hello how are you?")
    
# appending the text in file 
with open('sample.txt','a') as f:
      f.writelines("This file don't contain any useful information\n")
      f.writelines("It created for learn the topic file handling in python")

#  reading file 

with open('sample.txt','r') as f:
       # reading whole file once
             data = f.read()
             print(data,"\n")


with open('sample.txt','r') as f:
    # reading file line by line
    while(True):
        line = f.readline()
        if not line:
            break
        print(line,"\t")

search = input("Enter the word that you want to search in file ")
with open('sample.txt','r') as f:
      count = 1
      while(True):
            line = f.readline()
            if not line:
                  break
            if search in line:
                print(f"your word ({search}) found in line number {count}")
            count +=1


# replace a word in file 
word = input("Enter the word that you want to replace with new word -> ")
replace = input("Enter that new word -> ")
with open('sample.txt','r+') as f:
      data = f.read()
      f.seek(0)
      if word in data:
            data = data.replace(word,replace)
            
            f.write(data)
            f.truncate(f.tell())
            f.seek(0)

            print(f.read())
      else:
            print("word not found")



      
# for binary files use rb,wb,ab