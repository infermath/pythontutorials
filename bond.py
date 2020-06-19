import math as m
import matplotlib.pyplot as plt

class Bond:
    def __init__(self, maturity, coupon):
        self.maturity  = maturity
        self.coupon = coupon #annual in %

    def pv(self, r):
        sum = 100*m.pow(1+r, -self.maturity)
        for i in range(1, self.maturity+1):
            sum += self.coupon*m.pow(1+r,-i)
        return round(sum,2)

    def pv_derivative(self, r):
        sum = -self.maturity *100*m.pow(1+r, -self.maturity-1)
        for i in range(1, self.maturity+1):
            sum -= i*self.coupon*m.pow(1+r,-i-1)
        return round(sum,2)

    def pv_num_derivative(self, r):
        return (self.pv(r+0.001)-self.pv(r))/0.001
    
    def ytm(self, price):
        x = 0 #0.2
        while(abs(round(self.pv(x)-price, 2)) >0): #1
            x = x - (self.pv(x)-price)/self.pv_num_derivative(x)
            print(x)
        return x

bond=Bond(10, 4)
print(bond.pv(0.04))

price = 91
ytm = bond.ytm(price)
print(ytm)
print(bond.pv(ytm))

ir=range(10)
pvs=[bond.pv(i*0.01) - price for i in ir]

tangent = [bond.pv(0) - price + i*0.01*bond.pv_derivative(0) for i in ir]
tangent4 = [bond.pv(0.04) - price + (i-4)*0.01*bond.pv_derivative(0.04) for i in ir]

plt.plot(ir,pvs)
plt.plot(ir,tangent)
plt.plot(ir,tangent4)
plt.axvline(x=ytm*100)
plt.grid(True)
plt.show()
