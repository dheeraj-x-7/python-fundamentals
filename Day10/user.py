class User:
    # class variable -> that defined outside to constructor body
    __user_count = 0
    def __init__(self,name,age,code):
        
        if(type(age)!=int):
            raise TypeError("Age must be numeric...")
        elif(age<0):
            raise ValueError("Age can't be negative...")
        else:
            # instance variable ->  that defined in constructor body
            self.age = age
            self.name = name
            self.__code = code # this is private varibale via name mangling
            User.__user_count +=1
            self.sno = User.__user_count
    # getter method 
    def get_code(self):
        return self.__code
    # setter method
    def set_code(self,old,new):
        if self.__code == old :
            self.__code = new
            print("code successfully changed...")
        else:
            print("Old code not matched...")


    def display(self):
        return f""" 
                    user no.  -> {self.sno}
                    user name -> {self.name}
                    user age  -> {self.age}

"""

        


class Student(User):
     __student_count = 0
     def __init__(self,name,age,code,college,course,fees,email):
         if type(fees) != int:
             raise TypeError("Invalid type of fee...")
         elif fees < 0 :
             raise ValueError("Fee can't be negative")
         else:    
            super().__init__(name,age,code)
            self.college = college
            self.course = course
            self.fees = fees
            self.email = email
            Student.__student_count +=1      
            self.stu_id = Student.__student_count
            self.marks ={}

     def display(self):
         return f"""
                    Student no.   -> {self.stu_id}
                    Student name  -> {self.name}
                    Student age   -> {self.age}
                    College name  -> {self.college}
                    Course        -> {self.course}
                    Fee           -> {self.fees}
                    Student email -> {self.email}

"""
     def set_marks(self,**mark):
         for key, value in mark.items():
             if type(value) != int and type(value) != float:
                 raise TypeError("Marks must be numeric")
             self.marks[key] = value
     def display_marks(self):
         for key,value in self.marks.items():
             print(f"{key} => {value}")

