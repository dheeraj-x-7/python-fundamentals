# finding the second large number in a list --
size = int(input("Enter the number of elements that you want to insert "))
l =[]
for i in range(size):
    e = int(input(f"Enter the {i+1}th number -> "))
    l.append(e)
largest = max(l)
second_large = l[0]
for i in l:
    if(i<largest and i>second_large) :
        second_large = i
    else :
        pass
print(f"Your second largest number is -> {second_large}")