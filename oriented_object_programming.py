class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)+" = "+str(self.num/self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        newnum, newden = self.simplificated_fraction(newnum, newden)
        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den
        newnum, newden = self.simplificated_fraction(newnum, newden)
        return Fraction(newnum, newden)

    def __mul__(self, otherfraction):
        newnum = self.num*otherfraction.num
        newden = self.den * otherfraction.den
        newnum, newden = self.simplificated_fraction(newnum, newden)
        return Fraction(newnum, newden)

    def __truediv__(self, otherfraction):
        newnum = self.num*otherfraction.den
        newden = self.den * otherfraction.num
        newnum, newden = self.simplificated_fraction(newnum, newden)
        return Fraction(newnum, newden)

    def __eq__(self, otherfraction):
        if self.num == otherfraction.num and self.den == otherfraction.den:
            return True
        return False

    def __lt__(self, other):
        return self.num/self.den < other.num/other.den

    def __le__(self, other):
        return self.num/self.den <= other.num/other.den

    def simplificated_fraction(self, newnum, newden):
        gcd = self.gcd(newnum, newden)
        newnum, newden = int(newnum/gcd), int(newden/gcd)
        return newnum, newden

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
print(f1, f2)
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)
print(f1 == f2)
print(f1+f2 == f2+f1)
print(f1 < f2)
print(f1 > f2)
