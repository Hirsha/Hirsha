import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
temperature = np.random.randint(0, 100, size=100)
energy = np.random.randint(100, 1000, size=100)

# Create DataFrame
data = pd.DataFrame({'temperature': temperature, 'energy': energy})

# Save DataFrame to CSV
data.to_csv('energydata.csv', index=False)

# Rest of the code
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

# Load dataset
dataset = pd.read_csv('energydata.csv')

X = dataset['temperature'].values.reshape(-1,1)
y = dataset['energy'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm

#To retrieve the intercept:
print(regressor.intercept_)
#For retrieving the slope:
print(regressor.coef_)

# Plot the data points and the regression line
plt.scatter(X, y, color='blue')
plt.plot(X, regressor.predict(X), color='red')
plt.xlabel('Temperature')
plt.ylabel('Energy')
plt.title('Simple Linear Regression')
plt.show()
