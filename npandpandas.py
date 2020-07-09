import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

from numpy.random import randn 

data = randn(5, 5)
#print(data)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E' ])#колоночки для массива Data
df.head(4)#показать 4 строки из Data
df.shape #походу размер
df.describe()#info for array

np.array([2,7,15,274,68,11,0], float) 
