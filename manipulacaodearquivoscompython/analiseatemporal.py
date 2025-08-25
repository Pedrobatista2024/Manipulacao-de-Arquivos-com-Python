import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

df_dsa = pd.read_csv('dadostemporal.csv')

print(df_dsa.shape)

print(df_dsa.head())

print(df_dsa.tail())