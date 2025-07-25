from platform import python_version
import random
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
import seaborn as sea
warnings.filterwarnings('ignore')

dados = sea.load_dataset('tips')

#sea.jointplot(data= dados, x= "total_bill", y= "tip", kind= "reg")
#sea.lmplot(data=dados, x="total_bill", y="tip", col= "smoker")

df = pd.DataFrame()
df['idade']= random.sample(range(20,100), 30)
df['peso']= random.sample(range(55,150), 30)

#print(df.shape)
#print(df.head())

#sea.lmplot(data= df, x= 'idade', y= 'peso', fit_reg= True)

#sea.kdeplot(df.idade)

#sea.kdeplot(df.peso)

#sea.displot(df.peso)

#plt.hist(df.idade, alpha= .3)
#sea.rugplot(df.idade)
#
#sea.boxplot(df.idade, color= 'm')
#sea.boxplot(df.peso, color= 'r')
#
#sea.violinplot(df.idade, color= 'g')

#sea.clustermap(df)








plt.show()

