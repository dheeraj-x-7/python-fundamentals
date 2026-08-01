my_list = []
# taking 10 elements from user (integers)
print("Enter the values of list ->")
for i in range(10):
    my_list.append(int(input(f"Enter {i+1}th value -> ")))

# finding largest number in the list
def large_num(nums):
    lg = nums[0]
    for i in nums:
        if i > lg:
            lg = i
    return lg

# finding second largest number
def second_lg_num(nums):
    if len(nums) < 2:
        return None

    largest = large_num(nums)
    second_lg = None

    for i in nums:
        if i != largest and (second_lg is None or i > second_lg):
            second_lg = i

    return second_lg

# reverse a list without reverse method
rev_list = my_list[::-1]

# Display results 
print(f"List -> {my_list}")
print(f"\nLargest number of list -> {large_num(my_list)}")
print(f"\n Second Largest number -> {second_lg_num(my_list)}")
print(f"\n reversed list -> {rev_list}")