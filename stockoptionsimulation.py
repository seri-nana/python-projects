import math
import random
import numpy as np
import statistics
import pandas as pd
import matplotlib.pyplot as plt

def stockoptionsimulation(s0,rate,maturity,sigma):
    st = s0 * math.exp((rate - sigma * sigma / 2) * maturity + sigma * math.sqrt(maturity) * np.random.standard_normal())
    return st

def finalcallprice(pathnumber):
    stockprices = []
    for item in range(pathnumber):
        stockprice = stockoptionsimulation(s0,rate,maturity,sigma)
        stockprices.append(stockprice)
    #print(stockprices)
    k = 700
    callprices = [math.exp(-rate * maturity) * max(stockprice - k, 0)for stockprice in stockprices]
    #print(callprices)
    finalcallprice = statistics.mean(callprices)
    standarddev = statistics.stdev(callprices)
    return finalcallprice,standarddev
    
s0 = 700    
rate = 0.04
maturity = 1
sigma = 0.14
pathnumbers = [10,50,100,500,1000,5000,10000]
finalcallprices = [finalcallprice(pathnumber)[0] for pathnumber in pathnumbers]
mcerrors = [finalcallprice(pathnumber)[1]/ math.sqrt(pathnumber) for pathnumber in pathnumbers]
print(finalcallprices)
print(mcerrors)
df_callprice = pd.DataFrame(list(zip(pathnumbers,finalcallprices,mcerrors)), columns = ["pathnumbers","finalcallprices","mcerrors"])
df_callprice = df_callprice.set_index('pathnumbers')

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
df_callprice['finalcallprices'].plot(ax=axes[0], kind='line', title='Monte Carlo Call Option Pricer Estimate')
axes[0].set_xlabel('Number of Simulation Paths')
axes[0].set_ylabel('Estimated Call Option Price')

df_callprice['mcerrors'].plot(ax=axes[1], kind='bar', title='Monte Carlo Standard Error', color='red')
axes[1].set_xlabel('Number of Simulation Paths')
axes[1].set_ylabel('Monte Carlo Error (Standard Error)')

plt.tight_layout()
plt.show()

