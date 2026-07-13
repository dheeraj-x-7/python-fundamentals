size  = int(input("Define the size of list"))
my_list = []
for i in range(size):
    ele = input(f"Enter {i}th element in a list: ")
    my_list.append(ele)
cln_list = [] 
dupp = set()
for i in my_list:
    if(i in cln_list):
        dupp.add(i)
    else:
        cln_list.append(i)

print("duplicated elements : ",dupp)