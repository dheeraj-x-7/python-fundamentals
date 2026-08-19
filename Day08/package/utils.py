if __name__ == "__main__":
     print("you are in util file ")
def  input_name():
    try:
        name = input("Enter name -> ")
        if not name.isalpha():
            raise Exception("Enter valid name  ") 
    except Exception as e:
        print(e)
        return input_name()
    else:
        return name

def input_num(start=None,end=None):
    try:
        num = int(input("Enter a number-> "))
        if(start != None and end != None):
            if(num<start or num>end):
                raise Exception(f"Enter a number in range {start} to {end}")
        elif(start != None):
            if(num<start):
                raise Exception(f"Your number should be greater than or equal to {start}")
        elif(end != None):
                    if(num>end):
                        raise Exception(f"Your number should be smaller than or equal to {end}")
    except ValueError as e:
         print("Enter a valid integer ")
         return input_num(start,end)
    except Exception as e:
         print(e)
         return input_num(start,end)
    else:
         return num