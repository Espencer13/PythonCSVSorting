from audioop import maxpp
from statistics import stdev
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# download data from google drive: https://drive.google.com/drive/u/0/folders/11V-GD-OVq6hXvRjhcbMIvxHTU6EV7-ss
# df = pd.read_csv('/Users/m2mar/Documents/DATA 211/Data211 Final Project/DATA 211 Final Project Data Set.csv')
#df = pd.read_csv('/Users/osereme/Desktop/School/Year 5/Fall 2021/Winter 2022/DATA 211/Final Project/DATA 211 Final Project.csv')
df = pd.read_csv('/Users/evanspencer/Downloads/DATA 211 Final Project - DATA 211 Final Project.csv')

# Display the data shape
print('\n', "Data Shape: ", df.shape)

# Display the head
print('\n', "Data Head: ", df.head())

# Display the tail
print('\n', "Data Tail: ", df.tail())

# Set display options to display max 50 rows ##OSEREME TO CONFIRM IF CORRECT
pd.set_option('display.max_rows', 50)

# Display summary of the data
print('\n', "Data Summary: ", df.info())

# Removing any row than contains a NULL or NA value
df.dropna(inplace=True)

# Changing the draft year column to date format
df["Draft Year"] = pd.to_datetime(df["Draft Year"])

# Changing draft year column to string and removing "1970-01-01 00:00:00.00000" to get actual draft year
df['Draft Year'] = df['Draft Year'].astype(str)
df = df.replace(['1970-01-01 00:00:00.00000'], [''], regex=True)

# Changing draft year into an integer so it can be and sorted in ascending order
df['Draft Year'] = df['Draft Year'].astype(int)
df = df.sort_values(by='Draft Year', ascending=True)

# Removing duplicate last name
df.drop_duplicates(subset="Last Name", keep=False, inplace=True)

# VISUALIZATION 1

# Sorts the players based on salary in ascending order
df = df.sort_values(by="Salary (USD)", ascending=True)

# Create height variable for players
height = df['Height (inches)']

# Create salary variable for players
salary = df['Salary (USD)']

# Creates a scatter plot based on player height (x-axis)
plt.scatter(height, salary)

# Calculates mean height of the players
mean = sum(df['Height (inches)'])/len(df['Height (inches)']) #calculate approx. mean and standard deviation; normal distribution line of best fit is not too necessary

# Calculate standard deviation of player height
stdev = df['Height (inches)'].std()

# Prints mean and standard deviation of player height
print("Mean is %.2f" %mean)
print("Standard deviation is %.2f" %stdev)

# Ensure that y-axis values are printed as 1,200,000 instead of 1.2x10^6
plt.ticklabel_format(style = 'plain')

# Adds title, x-axis label, and y-axis labels
plt.title("Relationship Between Player Height and Salary")
plt.xlabel("Player Height (in inches)")
plt.ylabel("Player Salary (in USD)")

# Shows scatter plot
plt.show()

# VISUALIZATION 2

# calculates mean of the Player's Salary
salaryMean = df['Salary (USD)'].mean()

# Counts how many times each draft year appears in the CSV
countYears = df['Draft Year'].count()

# Groups the mean salaries by draft year
groupBySalaryMean = df.groupby(['Draft Year']).sum()

# groups 'Draft Year' by the count of Draft Yeas
groupByYearCount = df.groupby(['Draft Year']).count()

# Calculating the average salary by draft year
averageSalaries = groupBySalaryMean['Salary (USD)']/groupByYearCount['Salary (USD)']

# creates a line chart for the average salarie per draft years
plt.plot(averageSalaries)

# Ensure that y-axis values are printed as regular notation instead of in scientific notation
plt.ticklabel_format(style = 'plain')

# Adds title, x-axis label, and y-axis labels
plt.title("Average Player Salary By Draft Year")
plt.xlabel("Player Draft Year")
plt.ylabel("Average Player Salary (in USD)")

# shows line chart
plt.show()

# VISUALIZATION 3

# calculates mean of the Player's Salary (Same as in Vis. 2, thought it helped to have here as well)
salaryMean = df['Salary (USD)'].mean()

# Counts how many times each a player scores x amount of goals appears in the CSV
countGoals = df['Goals'].count()

# Groups the mean salaries by x goals scored
groupBySalaryMean = df.groupby(['Goals']).sum()

# Groups by count of goals scored
groupByGoals = df.groupby(['Goals']).count()

# calculates average salaries per goal
averageSalariesPerGoal = groupBySalaryMean['Salary (USD)']/groupByGoals['Salary (USD)']

# creating bar chart for average salary per goal
plt.bar(range(len(averageSalariesPerGoal)), averageSalariesPerGoal)

# Ensure that y-axis values are printed as regular notation instead of in scientific notation
plt.ticklabel_format(style = 'plain')

# Adds title, x-axis label, and y-axis labels
plt.title("Average Player Salary By Goals Scored")
plt.xlabel("Goals Scored")
plt.ylabel("Average Player Salary (in USD)")

# Shows the bar chart
plt.show()
