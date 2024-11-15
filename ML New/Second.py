import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
dataset= pd.read_csv("C:/Users/SL3-20/Downloads/temperatures.csv")
print(dataset.shape)
print(dataset.describe())
dataset.plot(x='FEB', y='MAR' , style='o')
plt.title('FEB vs MAR')
plt.xlabel('mintemp')
plt.ylabel('maxtemp')
plt.show()
plt.figure(figsize=(15,10))
plt.tight_layout()
seaborn.distplot(dataset['MAR'])
plt.show()
X= dataset['FEB'].values.reshape(-1,1)
y= dataset['MAR'].values.reshape(-1,1)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, 
random_state=0)
model =LinearRegression()
model.fit(X_train,y_train)
print('Intercept is :',model.intercept_)
print('Coefficient is :' ,model.coef_)
y_pred= model.predict(X_test)
df= pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df)
df1= df.head(25)
df1.plot(kind='bar', figsize=(16,10))
plt.grid(which='major', linestyle='-',linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':',linewidth='0.5', color='black')
plt.show()
plt.scatter(X_test,y_test,color='gray')
plt.plot(X_test,y_pred,color='red',linewidth=2)
plt.show()
print('Mean abolute error is:', metrics.mean_absolute_error(y_test,y_pred))
print('Mean squared error is:', metrics.mean_squared_error(y_test,y_pred))
print('Root mean squared error is:', 
np.sqrt(metrics.mean_squared_error(y_test,y_pred)))