from fraction import Fraction
from user import User, Student
# referace variable - > a variable or identifier that store the instance of clas, 
f1 = Fraction(3,4)
f2 = Fraction(4,6)
f3 = Fraction(5,5)
print(f1)
f4 = f1+f2
print(f4)
f4 = f1 * f3
print(f4)

f6 = Fraction(6,0)



u1 = User("dheeraj",20,8564)
u2 = User("ajay",19,"aju89")
u1.set_code(856,"dheer123")
print(u1.get_code())

u1_details = u1.display()
print(u1_details)
print(u1)
print(u2.display())
User.user_count = "ghj"
# accessing the private varibles of a class
print(u1._User__user_count)
u3 = User("avesh",22,7856)


s1 = Student("lokesh",23,522,"SGU","BA",50000,"l@gmail.com")
print(s1.display())
s1.set_marks(maths=78,python=89)
s1.display_marks()
