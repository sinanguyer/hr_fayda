import pandas as pd
import numpy as np
import datetime
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import time
import plotly.express as px
import altair as alt
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




### streamlit part
#st.title('Turkish Team')
#st.write(df_turkey)
#columns = st.sidebar.selectbox("Select column to plot", df_turkey.columns)

# Create the plot based on the selected column
#fig = px.histogram(df_turkey, x=columns, nbins=20)

# Show the plot
#st.plotly_chart(fig)

df = pd.concat([df_turkey, df_germany], ignore_index=True)


#df_combined = pd.concat([df_germany, df_turkey])

# Display data editor and allow user to select country
with st.sidebar:
    country = st.selectbox('Select a country', ['Germany', 'Turkey'])

# Filter data based on country selection
if country == 'Germany':
    df_filtered = df_germany
else:
    df_filtered = df_turkey

# Display filtered data
with st.container():
    st.write(f"{country} data")

if country == 'Germany':
    df = pd.concat([st.experimental_data_editor(df_filtered),df_turkey])
else:
    df = pd.concat([st.experimental_data_editor(df_filtered),df_germany])
# Define the columns to display in the selectbox
columns = ['First Name', 'Last Name', 'Position', 'Education', 'Age', 'country',
'Sex', 'JobSatisfaction', 'NumProjects', 'JobTenure',
'numcompanieswork', 'Duration of Employment', 'Attrition',
'Monthly Gross Wage', 'Social Security Cost',
'Private health insurance', 'Food Payment', 'Shuttle fee',
'Other Office Cost(Rent,IT etc)', 'Total Montly Cost', 'Position.1',
'Recruiter Cost', 'Advertising Cost', 'Date of Employment',
'Total Cost', 'Annual PC', 'Annual Total Cost', 'TurnoverRate',
'HappinessOfWorkplace', 'DistanceFromHome', 'MonthlyHours',
'OvertimeHours']

# Define the plot types to display in the selectbox
#plot_types = ['Scatter Plot', 'Parallel Coordinates']

# Define the default values for the selectboxes
#default_column = 'Age'
#default_plot_type = 'Scatter Plot'

# Define the title for the app
#st.title('Employee Data Analysis')

# Display the selectboxes for the dataframe and columns
#selected_dataframe = st.selectbox('Select a dataframe:', options=['df_turkey', 'df_german'])
#selected_column = st.selectbox('Select a column:', options=columns, index=columns.index(default_column))

# Display the selectbox for the plot type
#selected_plot_type = st.selectbox('Select a plot type:', options=plot_types, index=plot_types.index(default_plot_type))

# Filter the dataframe based on the selected dataframe
#if selected_dataframe == 'df_turkey':
#    filtered_df = df_turkey
#else:
#    filtered_df = df_germany
#
# Create the plot based on the selected plot type
#if selected_plot_type == 'Scatter Plot':
#    fig = px.scatter(filtered_df, x=selected_column, y='Monthly Gross Wage', color='Attrition')
#else:
#    fig = px.parallel_coordinates(filtered_df, dimensions=[selected_column, 'Monthly Gross Wage', 'Attrition'], color='Attrition')

# Display the plot
#st.plotly_chart(fig)


#df = pd.concat([df_turkey, df_germany], ignore_index=True)
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
# Get the list of numeric columns
x_column = numeric_columns[0]
y_column = numeric_columns[1]

# Create dropdown menus to select columns and plot type
x_axis = st.sidebar.selectbox('Select x-axis:', options=numeric_columns,key=1)
y_axis = st.sidebar.selectbox('Select y-axis:', options=numeric_columns,key=2)
plot_type = st.sidebar.selectbox('Select plot type:', options=['Scatter', 'Histogram'])

# Filter data by country
country_filter = st.sidebar.selectbox('Select country:', options=['Turkey', 'Germany', 'All'])
if country_filter != 'All':
    df_filtered = df[df['country'] == country_filter]
else:
    df_filtered = df

# Display plot
if st.sidebar.button("Generate Plots"):
    st.header(f'{plot_type} plot: {x_axis} vs. {y_axis}')
    if plot_type == 'Scatter':
        sns.scatterplot(data=df_filtered, x=x_axis, y=y_axis, hue='country')
    else:
        sns.histplot(data=df_filtered, x=x_axis, hue='country', element='step', stat='density')
        sns.kdeplot(data=df_filtered, x=x_axis, hue='country')

# Show the Streamlit app
    st.pyplot()



# Select only the numeric columns
# Select only the numeric columns
num_cols_germany = df_germany.select_dtypes(include=np.number).columns.tolist()
num_cols_turkey = df_turkey.select_dtypes(include=np.number).columns.tolist()

# Create a correlation matrix

corr_matrix_germany = df_germany[num_cols_germany].corr()
corr_matrix_turkey = df_turkey[num_cols_turkey].corr()

# Create a correlation matrix
corr_matrix_germany = df_germany[num_cols_germany].corr().round(2)
corr_matrix_turkey = df_turkey[num_cols_turkey].corr().round(2)

# Define a function to generate the correlation matrix plot

def corr_matrix_plot(corr_matrix, title):
    fig, ax = plt.subplots(figsize=(15, 12))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(corr_matrix, cmap=cmap, annot=True, fmt=".2f", square=True, mask=mask, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)

# Display the correlation matrix plot for Germany data
if st.sidebar.button("Generate Correlation matrix for Germany"):
    st.title("Correlation Matrix for Germany Data")
    corr_matrix_plot(corr_matrix_germany, "Correlation Matrix for Germany Data")

# Display the correlation matrix plot for Turkey data
if st.sidebar.button("Generate Correlation matrix for Turkey"):
    st.title("Correlation Matrix for Turkey Data")
    corr_matrix_plot(corr_matrix_turkey, "Correlation Matrix for Turkey Data")

# Create a button to generate correlations for specific variables
st.markdown("---")
st.header("Generate Correlations for Specific Variables")
var_1_germany = st.selectbox("Choose the first variable (Germany)", num_cols_germany)
var_2_germany = st.selectbox("Choose the second variable (Germany)", num_cols_germany)
if var_1_germany != var_2_germany:
    if st.button("Generate Correlation (Germany)"):
        correlation_germany = df_germany[[var_1_germany, var_2_germany]].corr().iloc[0, 1].round(2)
        st.write(f"The correlation between {var_1_germany} and {var_2_germany} (Germany) is {correlation_germany}")
else:
    st.warning("Please select different variables.")

var_1_turkey = st.selectbox("Choose the first variable (Turkey)", num_cols_turkey)
var_2_turkey = st.selectbox("Choose the second variable (Turkey)", num_cols_turkey)
if var_1_turkey != var_2_turkey:
    if st.button("Generate Correlation (Turkey)"):
        correlation_turkey = df_turkey[[var_1_turkey, var_2_turkey]].corr().iloc[0, 1].round(2)
        st.write(f"The correlation between {var_1_turkey} and {var_2_turkey} (Turkey) is {correlation_turkey}")
else:
    st.warning("Please select different variables.")


st.set_option('deprecation.showPyplotGlobalUse', False)
