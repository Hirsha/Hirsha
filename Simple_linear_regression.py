import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
temperature = np.random.randint(-20, 40, size=100)
energy = np.random.randint(-500, 3000, size=100)

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

X = np.array(dataset['temperature']).reshape(-1,1)
y = np.array(dataset['energy']).reshape(-1,1)

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

# Highlight relevant points in red and annotate their coordinates
plt.scatter(X_test, y_test, color='red')
# Find the 10 nearest points to the fitted line
distances = np.abs(y_test - regressor.predict(X_test))
nearest_indices = np.argsort(distances.flatten())[:10]
nearest_points = list(zip(X_test.flatten()[nearest_indices], y_test.flatten()[nearest_indices]))
for point in nearest_points:
    plt.annotate(f'({point[0]}, {point[1]})', point, textcoords="offset points", xytext=(0,10), ha='center', color='red')

plt.show()
