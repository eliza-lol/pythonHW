from math import sqrt


class Triangle():

    def __init__(self,a,b,c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
    
    def area(self):
        s = (self.a + self.b + self.c)//2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    def scale(self, scale_factor):
        return Triangle(scale_factor * self.a, scale_factor * self.b, scale_factor * self.c)

    def is_valid(self):
        if self.a + self.b > self.c or self.a + self.c > self.b or self.b + self.c > self.a:
            return True 
        else:
            return False
    
    def is_right(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True
        else:
            return False




        