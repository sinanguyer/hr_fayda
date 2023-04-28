import pandas as pd
import numpy as np
import datetime
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import time


##################################################################################################################
np.random.seed(123)
job_satisfaction = np.random.randint(1, 11, size=8)
num_projects = np.random.randint(1, 6, size=8)
# Creating a sample DataFrame for Turkish Team
df_turkey = pd.DataFrame({
    'First Name': ['Batuhan', 'Miray', 'Ender', 'Chahira', 'Sena', 'Sinan', 'Betül', 'Irem'],
    'Last Name': ['Özdemir', 'Köklü', 'Mutlu', 'Grimes', 'Mise', 'Güyer', 'Yildiz', 'Celik'],
    'Position': ['Customer Care', 'E&E Technical Coordination', 'E&E Technical Coordination',
                 'Project Coordinator', 'Quotation Administrator', 'IT Project Analyst',
                 'Procurement Manager', 'Quotation Administrator'],
    'Education': ['Bachelor', 'Bachelor', 'Bachelor', 'Bachelor', 'Bachelor', 'PhD', 'Bachelor', 'Bachelor'],
    'Age': [33, 34, 27, 40, 34, 34, 34, 34],
    'country': ['Turkey', 'Turkey', 'Turkey', 'Turkey', 'Turkey', 'Turkey', 'Turkey', 'Turkey'],
    'Sex': ['M', 'F', 'M', 'F', 'F', 'M', 'F', 'F'],
    'JobSatisfaction': job_satisfaction,
    'NumProjects': num_projects,
    'JobTenure': np.random.randint(1, 15, size=8),

})

# Adding the Monthly Gross Wage, Social Security Cost, Private health insurance, Food Payment,
# Shuttle fee, Other Office Cost, Total Montly Cost, Position.1, Duration of Employment,
# Recruiter Cost, Advertising Cost, Total Cost, Annual PC, Annual Total Cost, and today columns

# Define the current date
today = datetime.date.today()
today = datetime.date.today()

# Convert the date strings to datetime objects
dates = ['19.09.2022', '19.09.2022', '19.09.2022', '2.01.2023', '2.01.2023', '2.01.2023', '2.01.2023', '01.02.2023']
dates = [datetime.datetime.strptime(date, '%d.%m.%Y').date() for date in dates]

num_companies_worked = np.random.randint(0, 6, size=(len(df_turkey),))
df_turkey['numcompanieswork'] = num_companies_worked

# Calculate the duration of employment
df_turkey['Duration of Employment'] = [(today - date).days for date in dates]
df_turkey['Attrition'] = np.random.choice([0, 1], size=len(df_turkey), p=[0.7, 0.3])
df_turkey['Monthly Gross Wage'] = np.random.randint(4000, 10000, size=8) * 0.20
df_turkey['Social Security Cost'] = df_turkey['Monthly Gross Wage'] * 0.225
df_turkey['Private health insurance'] = 200
df_turkey['Food Payment'] = 500
df_turkey['Shuttle fee'] = 1000
df_turkey['Other Office Cost(Rent,IT etc)'] = 2000
df_turkey['Total Montly Cost'] = df_turkey['Monthly Gross Wage'] + df_turkey['Social Security Cost'] + \
                                 df_turkey['Private health insurance'] + df_turkey['Food Payment'] + df_turkey[
                                     'Shuttle fee'] + \
                                 df_turkey['Other Office Cost(Rent,IT etc)']
df_turkey['Position.1'] = df_turkey['Position']
df_turkey['Recruiter Cost'] = df_turkey['Monthly Gross Wage'] * 0.1
df_turkey['Advertising Cost'] = np.random.randint(100, 1000, size=8)
df_turkey['Date of Employment'] = ['19.09.2022', '19.09.2022', '19.09.2022', '2.01.2023', '2.01.2023', '2.01.2023',
                                   '2.01.2023', '01.02.2023']
# df_turkey['Duration of Employment'] = df_turkey['today'] - df_turkey['Date of Employment']
df_turkey['Total Cost'] = df_turkey['Total Montly Cost'] * df_turkey['Duration of Employment'] + \
                          df_turkey['Recruiter Cost'] + df_turkey['Advertising Cost']
df_turkey['Annual PC'] = df_turkey['Total Montly Cost'] * 12
df_turkey['Annual Total Cost'] = df_turkey['Total Cost'] * 12

df_turkey['TurnoverRate'] = np.where(df_turkey['Attrition'] == 1, 1, 0)
df_turkey['HappinessOfWorkplace'] = df_turkey['JobSatisfaction'] * df_turkey['JobTenure']

# create random data for DistanceFromHome column
df_turkey['DistanceFromHome'] = np.random.randint(1, 30, size=len(df_turkey))

# create random data for MonthlyHours and OvertimeHours columns
df_turkey['MonthlyHours'] = np.random.randint(140, 300, size=len(df_turkey))
df_turkey['OvertimeHours'] = np.random.randint(0, 50, size=len(df_turkey))

print(df_turkey)

######################################################################################################################

#Germany Team

df_germany = pd.DataFrame({
    'First Name': ['Max', 'Sophie', 'Jan', 'Lena', 'Felix', 'Emilia', 'Moritz', 'Hannah'],
    'Last Name': ['Schneider', 'Müller', 'Bauer', 'Fischer', 'Weber', 'Hoffmann', 'Schmitt', 'Keller'],
    'Position': ['Customer Care', 'E&E Technical Coordination', 'E&E Technical Coordination',
                 'Project Coordinator', 'Quotation Administrator', 'IT Project Analyst',
                 'Procurement Manager', 'Quotation Administrator'],
    'Education': ['Bachelor', 'Bachelor', 'Bachelor', 'Master', 'Bachelor', 'Master', 'Master', 'Bachelor'],
    'Age': [37, 38, 45, 40, 39, 38, 41, 38],
    'country':['Germany','Germany','Germany','Germany','Germany','Germany','Germany','Germany'],
    'Sex': ['M', 'M', 'M', 'F', 'M', 'M', 'M', 'F'],
    'JobSatisfaction': job_satisfaction,
    'NumProjects': num_projects,
    'JobTenure': np.random.randint(1, 15, size=8),
})





# Adding the Monthly Gross Wage, Social Security Cost, Private health insurance, Food Payment,
# Shuttle fee, Other Office Cost, Total Montly Cost, Position.1, Duration of Employment,
# Recruiter Cost, Advertising Cost, Total Cost, Annual PC, Annual Total Cost, and today columns
# Define the current date
today = datetime.date.today()
today = datetime.date.today()

# Convert the date strings to datetime objects
dates = ['19.09.2022', '19.09.2022', '19.09.2022', '2.01.2023', '2.01.2023', '2.01.2023', '2.01.2023', '01.02.2023']
dates = [datetime.datetime.strptime(date, '%d.%m.%Y').date() for date in dates]

# Calculate the duration of employment
# generate random data for number of previous companies worked for
num_companies_worked = np.random.randint(0, 6, size=(len(df_germany),))
df_germany['numcompanieswork'] = num_companies_worked

df_germany['Duration of Employment'] = [(today - date).days for date in dates]
df_germany['Attrition'] = np.random.choice([0, 1], size=len(df_germany), p=[0.2, 0.8])
df_germany['Monthly Gross Wage'] = np.random.randint(4000, 10000, size=8)
df_germany['Social Security Cost'] = df_germany['Monthly Gross Wage'] * 0.35
df_germany['Private health insurance'] = df_germany['Monthly Gross Wage'] * 0.1
df_germany['Food Payment'] = 700
df_germany['Shuttle fee'] = 1200
df_germany['Other Office Cost(Rent,IT etc)'] = 2500
df_germany['Total Montly Cost'] = df_germany['Monthly Gross Wage'] + df_germany['Social Security Cost'] + \
    df_germany['Private health insurance'] + df_germany['Food Payment'] + df_germany['Shuttle fee'] + \
    df_germany['Other Office Cost(Rent,IT etc)']
df_germany['Position.1'] = df_germany['Position']
df_germany['Recruiter Cost'] = df_germany['Monthly Gross Wage'] * 0.1
df_germany['Advertising Cost'] = np.random.randint(100, 1000, size=8)
df_germany['Total Cost'] = df_germany['Total Montly Cost'] * df_germany['Duration of Employment'] + \
    df_germany['Recruiter Cost'] + df_germany['Advertising Cost']
df_germany['Annual PC'] = df_germany['Total Montly Cost'] * 12
df_germany['Annual Total Cost'] = df_germany['Total Cost'] * 12
df_germany['today'] = pd.Timestamp('now').strftime("%Y-%m-%d")
# create new variables as a function of attrition for Germany team
df_germany['TurnoverRate'] = np.where(df_germany['Attrition'] == 1, 1, 0)
df_germany['HappinessOfWorkplace'] = df_germany['JobSatisfaction'] * df_germany['JobTenure']

df_germany['DistanceFromHome'] = np.random.randint(1, 30, size=len(df_germany))
df_germany['MonthlyHours'] = np.random.randint(140, 300, size=len(df_germany))
df_germany['OvertimeHours'] = np.random.randint(0, 50, size=len(df_germany))


print(df_germany)
######################################################################################################################


#Here comes the charts

# Create a scatter plot with age on the x-axis and salary on the y-axis for the Turkish team
sns.scatterplot(data=df_germany, x='Age', y='Monthly Gross Wage', hue='Education', style='Position.1')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Salary vs Age for the Germany Team')
plt.show()

sns.scatterplot(data=df_turkey, x='Age', y='Monthly Gross Wage', hue='Education', style='Position.1')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Salary vs Age for the Turkish Team')
plt.show()

# Calculate the average salary for each position in the German team
avg_salary = df_germany.groupby(['Position.1'])['Monthly Gross Wage'].mean().reset_index()

# Create a bar chart with the average salary for each position in the German team
ax =sns.barplot(data=avg_salary, x='Position.1', y='Monthly Gross Wage')
# Tilt the x-axis labels by 45 degrees
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
# Add labels and title
plt.xlabel('Position')
plt.ylabel('Average Salary')
plt.title('Average Salary by Position for the German Team')
plt.show()

########################################################################################################

# Calculate the average salary for each position in the Turkish team
avg_salary = df_turkey.groupby(['Position.1'])['Monthly Gross Wage'].mean().reset_index()

# Create a bar chart with the average salary for each position in the German team
ax =sns.barplot(data=avg_salary, x='Position.1', y='Monthly Gross Wage')
# Tilt the x-axis labels by 45 degrees
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
# Add labels and title
plt.xlabel('Position')
plt.ylabel('Average Salary')
plt.title('Average Salary by Position for the Turkish Team')
plt.show()

# Plot a histogram of salaries for the Turkish and German teams
sns.histplot(data=df_turkey, x='Monthly Gross Wage', label='Turkey', alpha=0.5)
sns.histplot(data=df_germany, x='Monthly Gross Wage', label='Germany', alpha=0.5)

# Add labels and title
plt.xlabel('Salary')
plt.ylabel('Count')
plt.title('Distribution of Salaries for Turkish and German Teams')

# Add a legend
plt.legend()
plt.show()

######################################################################################################################

# Calculate the average salary by education level for the Turkish and German teams
turkey_avg = df_turkey.groupby('Education')['Monthly Gross Wage'].mean().reset_index()
germany_avg = df_germany.groupby('Education')['Monthly Gross Wage'].mean().reset_index()

# Merge the two DataFrames
avg_salary_by_edu = pd.merge(turkey_avg, germany_avg, on='Education', suffixes=('_Turkey', '_Germany'))

# Plot a bar chart of the average salary by education level
sns.barplot(data=avg_salary_by_edu, x='Education', y=df_turkey['Monthly Gross Wage'], label='Turkey', alpha=0.5,palette=['red', 'green', 'blue'])
sns.barplot(data=avg_salary_by_edu, x='Education', y=df_germany['Monthly Gross Wage'], label='Germany', alpha=0.5)

# Add labels and title
plt.xlabel('Education Level')
plt.ylabel('Average Salary')
plt.title('Average Salary by Education Level for Turkish and German Teams')

# Add a legend
plt.legend()
plt.show()

#######################################################################################################################

# Plot a histogram of ages for the Turkish and German teams
sns.histplot(data=df_turkey, x='Age', label='Turkey', alpha=0.5)
sns.histplot(data=df_germany, x='Age', label='Germany', alpha=0.5)

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Ages for Turkish and German Teams')

# Add a legend
plt.legend()
plt.show()

###############################

#Calculate the proportion of team members by position for the Turkish and German teams
turkey_prop = df_turkey['Position.1'].value_counts(normalize=True).reset_index()
germany_prop = df_germany['Position.1'].value_counts(normalize=True).reset_index()

# Merge the two DataFrames
prop_by_position = pd.merge(turkey_prop, germany_prop, on='index', suffixes=('_Turkey', '_Germany'))

# Plot a stacked bar chart of the proportion of team members by position
prop_by_position.plot(x='index', kind='bar', stacked=True)

# Add labels and title
plt.xlabel('Position')
plt.ylabel('Proportion of Team Members')
plt.title('Proportion of Team Members by Position for Turkish and German Teams')

# Add a legend
plt.legend(['Turkey', 'Germany'])
plt.show()

#######################################################
#streamlit code
st.header("HR Analysis")
st.subheader("Turkish Team")
df_turkey = st.experimental_data_editor(df_turkey,num_rows="dynamic")
st.subheader("German Team")
df_germany = st.experimental_data_editor(df_germany,num_rows="dynamic")

hist1 = sns.histplot(data=df_turkey, x='Age', label='Turkey', alpha=0.5)
st.pyplot(hist1.get_figure())
