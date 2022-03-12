# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df = pd.read_csv('50_Startups.csv')

State=pd.get_dummies(df["State"],drop_first=True)
df = pd.concat([df,State],axis=1)
df=df.drop("State",axis=1)
y=df["Profit"]
X=df.drop("Profit",axis=1)



from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))


