'''
Author: Lucas Yudi Sugi - 9293251
Discipline: SCC0270 - Introducao a Redes Neurais 
Title: PCA in iris
'''

#Import's
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pca import PCA

#Read file
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']  
iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None,names=columns)

#Extract features
features = iris.drop('class',1)

#Apply pca in data
p = PCA(k=3)
p = p.fit_transform(features)

#Create a dataframe with new data
names = ['pc1','pc2','pc3','pc4']
principalDf = pd.DataFrame(data=p,columns=names[0:p.shape[1]])

#Concat with class
finalDf = pd.concat([principalDf,iris['class']],axis=1)

#Show the new space
sns.pairplot(data=finalDf,hue='class',diag_kind='kde')
plt.show()
