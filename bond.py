import math as m
import matplotlib.pyplot as plt

class Bond:
    def __init__(self, maturity, coupon):
        self.maturity  = maturity
        self.coupon = coupon

    def Price(self, ytm):
        sum = 100/m.pow(1+ytm,self.maturity)
        for i in range(1,self.maturity+1):
            sum += 100*self.coupon/m.pow(1+ytm,i)
        return round(sum,2)

james=Bond(1,0.04)
print(james.Price(0.01))

jane=Bond(5,0.02)
print(jane.Price(0.02))

joe=Bond(10, 0.03)

ir=range(10)
prices=[joe.Price(i*0.01) for i in ir]
print(prices)
plt.plot(ir,prices)
plt.show()
