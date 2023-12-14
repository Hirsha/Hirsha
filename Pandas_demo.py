import pandas as pd
import random
import matplotlib.pyplot as plt
# Create a DataFrame with 100 entries
data = {'Name': [],
        'Age': [],
        'City': []}

for _ in range(100):
    name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    age = random.randint(20, 40)
    city = random.choice(['New York', 'London', 'Paris', 'Tokyo'])
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

print("DataFrame:")
print(df)
plt.show()

# Show basic statistics of the DataFrame
print("\nBasic Statistics:")
print(df.describe())

# Filter the DataFrame
print("\nFiltered DataFrame:")
filtered_df = df[df['Age'] > 26]
print(filtered_df)

# Group the DataFrame by a column
print("\nGrouped DataFrame:")
grouped_df = df.groupby('City').count()
print(grouped_df)

# Plot a bar chart of the grouped DataFrame
print("\nBar Chart:")
grouped_df.plot(kind='bar')
plt.show()

# Continue the demo or exit
while True:
    user_input = input("\nType 'next' to continue or 'exit' to end the demo: ")
    if user_input == 'next':
        # Add more functionalities here
        pass
    elif user_input == 'exit':
        break
