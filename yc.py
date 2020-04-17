import zero as z
import matplotlib.pyplot as plt
import numpy as np

maturities = [2,5,10,30]
yields=[0.0249, 0.0246,0.0266,0.0306]

plt.plot(maturities,yields)
plt.show()

bonds=[z.Zero(i) for i in maturities]
prices=[bonds[i].Price(yields[i]) for i in range(0,4)]

maturities.pop(2)
marketYield = yields.pop(2)
marketPrice = prices.pop(2)

interpolatedPrice = np.interp(10,maturities,prices)
interpolatedYield = np.interp(10,maturities,yields)

priceFeromInterpolatedYield = bonds[2].Price(interpolatedYield)
