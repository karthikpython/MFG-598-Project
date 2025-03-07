# -*- coding: utf-8 -*-
"""MFG 598 Graphs Code (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ptwoKzyZW3L1Bi8J22UygGP-0ika0f-f
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv('/content/drive/MyDrive/Karthik/df.csv')  # Replace with your actual file path

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Identify the top 5 makes by count
top_5_makes = df['make'].value_counts().nlargest(5).index

# Filter the DataFrame to only include rows with the top 5 makes
top_5_df = df[df['make'].isin(top_5_makes)]

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Plotting Number of Vehicles by Top 5 Makes
plt.figure(figsize=(10, 6))
sns.countplot(y='make', data=top_5_df, order=top_5_makes)
plt.title('Number of Vehicles by Top 5 Makes')
plt.xlabel('Count')
plt.ylabel('Make')
plt.show()

from google.colab import drive
drive.mount('/content/drive')

# Filter the DataFrame for more accurate MPG calculations
filtered_top_5_df = top_5_df[top_5_df['city_mpg_ft1'] > 0]

# Calculate the average city MPG for each of the top 5 makes
average_mpg = filtered_top_5_df.groupby('make')['city_mpg_ft1'].mean().sort_values(ascending=False)

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Plotting Average City MPG by Top 5 Makes
plt.figure(figsize=(10, 6))
sns.barplot(x=average_mpg.values, y=average_mpg.index)
plt.title('Average City MPG by Top 5 Makes')
plt.xlabel('Average City MPG')
plt.ylabel('Make')
plt.show()

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Plotting Vehicle Distribution by Year
plt.figure(figsize=(12, 8))
sns.countplot(x='year', data=df)
plt.title('Vehicle Distribution by Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate the x-axis labels for better readability
plt.show()