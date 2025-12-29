import matplotlib.pyplot as plt
import numpy as np

# Sample data - generating random data points using normal distribution
np.random.seed(0)
x = np.random.randn(1000)
y = np.random.randn(1000)
colors = np.random.randint(10, 101, size=1000)
sizes = np.random.randint(10, 101, size=1000)

# Scatter plot with multiple customizations
plt.scatter(x, y, c=colors, cmap="viridis", s=sizes, marker='o', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Matplotlib')
plt.show()
