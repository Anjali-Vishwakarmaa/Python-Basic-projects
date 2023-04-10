class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

    @classmethod
    def demo(cls, n, d):

        for i in range(2, 10):
            if n % i == 0 and d % i == 0:
                n = int(n / i)
                d = int(d / i)
                return cls.demo(n, d)
        else:
            return n,d

    def __add__(self, other):
        temp_num = (self.num * other.den)+(self.den * other.num)
        temp_den = self.den * other.den
        temp_num, temp_den = Fraction.demo(temp_num, temp_den)
        return '{}/{}'.format(temp_num, temp_den)

    def __sub__(self, other):
        temp_num = (self.num * other.den) - (self.den * other.num)
        temp_den = self.den * other.den
        temp_num, temp_den = Fraction.demo(temp_num, temp_den)
        return '{}/{}'.format(temp_num, temp_den)

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        temp_num, temp_den = Fraction.demo(temp_num, temp_den)
        return '{}/{}'.format(temp_num, temp_den)

    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        temp_num, temp_den = Fraction.demo(temp_num, temp_den)
        return '{}/{}'.format(temp_num, temp_den)



a = Fraction(2,5)
b = Fraction(3,4)
print(a+b)
print(a-b)
print(a*b)
print(a/b)