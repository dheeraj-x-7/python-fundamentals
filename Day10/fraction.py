class Fraction:
    def __init__(self,n,d):
        # it is constructor 
        # invoke when the instance of class created
        self.usable = False
        try :
            if isinstance(n,int) and isinstance(d,int):
                if d!=0 :

                    self.num = n
                    self.den = d
                    self.usable = True
                else :
                    raise Exception("Denominator can't be zero")
            else:
                raise Exception("Input should ne integer")
            
        except Exception as e:
            print(e)
           


    def __str__(self):
        if self.usable:
            return f"{self.num}/{self.den}"
        else:
            return None
        
    def __add__(self,other):
        if self.usable:
            n = self.num*other.den + other.num*self.den
            d = self.den*other.den
            return f"{n}/{d}"
    def __sub__(self,other):
       if self.usable:
                n = self.num*other.den - other.num*self.den
                d = self.den*other.den
                return f"{n}/{d}"
        
    def __mul__(self,other):
        if self.usable:

            n = self.num*other.num
            d = self.den*other.den
            return f"{n}/{d}"
        
    def simplify(self):
        pass
# magic/dunder methods -> by these methods developer can customize the behaviour and integrate seamlessly with Python’s built-in syntax and operators.
# __add__, __sub__, __mul__ -> these are invoke when these operator(+,-,*) used 
# __str__ -> invoke when print statement used to print fractions