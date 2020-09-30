import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        #return self.real+self.imaginary
        self.no=no
        # print(self.real) 2.00
        # print(no.real)   5.00
        # print(self.imaginary) 1.00
        # print(no.imaginary)    6.00
        return Complex(self.real+no.real,self.imaginary+no.imaginary)
 
    def __sub__(self, no):
        return Complex(self.real-no.real,self.imaginary-no.imaginary)
        
    def __mul__(self, no):
        #return Complex(self.real*no .real-self.imaginary*no.imaginary,(self.real*no.real+(self.real+no.real)))
        return Complex(self.real*no .real-self.imaginary*no.imaginary,(self.real*no.imaginary+(self.imaginary*no.real)))
    def __truediv__(self, no):
       # print(self.real*no .real-self.imaginary*(-no.imaginary),(self.real*no.real+(self.real+no.real)))
       #if no.real<0:
        a=no.real*no.real+((no.imaginary*no.imaginary))
        b=self.real*no.real+self.imaginary*(no.imaginary)
        c=self.real*(-no.imaginary)+(self.imaginary*no.real)
        #print(b,c)
        
        return Complex(b/a,c/a)

    def mod(self):
        #return Complex(f"{math.sqrt(self.real**2+self.imaginary**2):.2f}",'0.00')
        #return Complex((float(f"{math.sqrt(self.real**2+self.imaginary**2)}")),0.00)
         return Complex((float(math.sqrt(self.real**2+self.imaginary**2))),0.00)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
