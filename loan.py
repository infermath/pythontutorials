class Loan:
    def __init__(self,notional,redemption,ir):
        self.notional = notional
        self.redemption = redemption
        self.ir = ir

    def FV(self):
        return self.redemption - self.notional*(1+self.ir)

    def PV(self):
        return self.redemption/(1+self.ir) - self.notional

    def DF(self):
        return1/(1+self.ir) 
