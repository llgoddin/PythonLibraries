import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import math

sales_data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

df = pd.DataFrame(sales_data, index=['June', 'July', 'August', 'September'])

print(df)

df.sum().plot(kind='pie')
plt.show()


# Create a path with os.join
path = os.path.join("data", "data.csv")

os.makedirs("data")
os.remove("data/data.csv")

# Math functions
print(math.sqrt(16))
print(math.factorial(5))
print(math.log(10))
print(math.log10(10))