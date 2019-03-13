import math as m
import matplotlib.pyplot as plt

class Zero:
    def __init__(self, maturity):
        self.maturity  = maturity

    def YTM(self, price):
        return m.pow(100/price, 1/self.maturity) - 1

    def Price(self, ytm):
        return 100/m.pow(1+ytm,self.maturity)

        
