import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
plt.style.use("seaborn")

df = pd.read_csv("/Users/kyungyunlee/Desktop/ IRP reference/Data/Lee/20_piece_middle.csv")
df.plot("time", "y_value")
plt.show()