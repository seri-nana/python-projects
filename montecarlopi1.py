import random
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def montecarlo(numpoints):
    pointsincircle = 0
    for element in range(numpoints):
        x = random.random()
        y = random.random()
        distance = x*x + y*y
        if distance <= 1:
            pointsincircle = pointsincircle + 1
    output = pointsincircle/numpoints * 4
    return output
a = 1000
print(montecarlo(a))

def plotpi(numpoints):
    pivalues = [montecarlo(item) for item in numpoints]
    mcerrs = [math.sqrt((pivalue/4 * (1 - pivalue/4))/numpoint) for pivalue, numpoint in zip(pivalues, numpoints)]
    pis = [3.1415926535897932384626 for item in pivalues]
    #data = {'numpoints': numpoints, 'pivalues':pivalues, 'mcerrs': mcerrs}
    df_pi = pd.DataFrame(list(zip(numpoints, pivalues, mcerrs,pis)), columns=["numpoints", "pivalues", "mcerrs","pis"])
    return df_pi
    
numpoints = [10,50,100,500,1000,5000,10000,50000,100000,500000,1000000]    
df1 = plotpi(numpoints)
print(df1)
#df1 = df1.set_index('numpoints')
#df1.plot(title='values of pi')

# Create a figure and a set of subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

# Plot the first column on the first axis (left plot)
df1[['pivalues','pis']].plot(ax=axes[0], kind='line', title='Pi')
#df1.plot(x='numpoints', y=['pivalues', 'pis'], kind='line',title='Pi') 
axes[0].set_xlabel('Index')
axes[0].set_ylabel('Values')

# Plot the second column on the second axis (right plot)
df1['mcerrs'].plot(ax=axes[1], kind='line', title='Monte Carlo Error', color='red')
axes[1].set_xlabel('Index')
axes[1].set_ylabel('Values')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
