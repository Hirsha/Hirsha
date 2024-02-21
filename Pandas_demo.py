import pandas as pd
import random
from faker import Faker
import matplotlib.pyplot as plt

fake = Faker()

# Create a DataFrame with 100 entries
data = {'Name': [],
    'Age': [],
    'City': []}

for _ in range(100000):
    name = fake.first_name()
    age = random.randint(20, 40)
    city = random.choice(['New York', 'London', 'Paris', 'Tokyo', 'Prague'])
    data['Name'].append(name)
    data['Age'].append(age)
    data['City'].append(city)


df = pd.DataFrame(data)
# Display the DataFrame
print("\nDataFrame:")
print(df)

while True:
    user_input = input("\nType 'next' to continue or 'exit' to end the demo: ")
    if user_input == 'next':
        break
    elif user_input == 'exit':
        exit()

# Display the DataFrame with full object
print("\nDataFrame:")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)

while True:
    user_input = input("\nType 'next' to continue or 'exit' to end the demo: ")
    if user_input == 'next':
        break
    elif user_input == 'exit':
        exit()

# Show basic statistics of the DataFrame
print("\nBasic Statistics:")
print(df.describe())

while True:
    user_input = input("\nType 'next' to continue or 'exit' to end the demo: ")
    if user_input == 'next':
        break
    elif user_input == 'exit':
        exit()

# Filter the DataFrame
print("\nFiltered DataFrame:")
filtered_df = df[df['Age'] > 37]
print(filtered_df)

while True:
    user_input = input("\nType 'next' to continue or 'exit' to end the demo: ")
    if user_input == 'next':
        break
    elif user_input == 'exit':
        exit()

# Group the DataFrame by a column
print("\nGrouped DataFrame:")
grouped_df = df.groupby('Name').count()
print(grouped_df)

# Plot a bar chart of the grouped DataFrame
print("\nBar Chart:")
grouped_df.plot(kind='bar')
plt.show()

# Plot a line chart of the grouped DataFrame
print("\nLine Chart:")
grouped_df.plot(kind='line')
plt.show()

# Plot a scatter chart of the DataFrame
print("\nScatter Chart:")
df.plot(kind='scatter', x='Age', y='City')
plt.show()


# Plot a histogram of the DataFrame
print("\nHistogram:")
df['Age'].plot(kind='hist')
plt.show()

# Plot a pie chart of the DataFrame
print("\nPie Chart:")
df['City'].value_counts().plot(kind='pie')
plt.show()