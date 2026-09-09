class Student: 
    college = "sgu"
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender  = gender
    #
    @classmethod
    def channge_clg(cls,new):
        cls.college = new 
    @staticmethod
    def greet():
        print("Welcome to sgi")
    
    def display(self):
        print(f"""
    name -> {self.name}
    age -> {self.age}
    gender -> {self.gender}
    college -> {self.college}
""")

s1 = Student("dheeraj",20,"male")
s1.display()
s2 = Student("prince",19,"male")
s1.channge_clg("sgi")
s2.display()
s1.display()
s1.greet()