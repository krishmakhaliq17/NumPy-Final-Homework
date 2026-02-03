import pandas as pd
import numpy as np
data = {
    "employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen",
                 "Ivan", "Julia", "Kevin", "Laura"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance",
                   "IT", "HR", "Finance", "IT", "HR", "Finance"],
    "age": [23, 25, 22, 30, 28, 35, 26, 24, 29, 31, 27, 34],
    "salary": [5000, 4500, 5200, 6000, 4800, 6500,
               5100, 4700, 6200, 5400, 4600, 6800],
    "experience_years": [1, 2, 1, 5, 3, 7, 2, 2, 4, 3, 2, 8]
}
df = pd.DataFrame(data)
# 1 Display the DataFrame and its shape
print(df)
print("Shape:", df.shape)

# 2 Print column names and data types
print(df.dtypes)

# 3 Show first 5 rows and last 5 rows
print(df.head(5))
print(df.tail(5))

# 4 Check for missing values
print(df.isnull().sum())

# 5 Sort employees by salary descending
df_sorted = df.sort_values(by='salary', ascending=False)
print(df_sorted)

# 1 Filter employees with salary above average salary
avg_salary = df['salary'].mean()
above_avg = df[df['salary'] > avg_salary]

# 2 Find average salary per department
avg_dept_salary = df.groupby('department')['salary'].mean()

# 3 Count employees per department
dept_count = df['department'].value_counts()

# 4 Find employee with highest experience
max_exp_emp = df[df['experience_years'] == df['experience_years'].max()]

# 5 Create a new column salary_per_year
df['salary_per_year'] = df['salary'] / df['experience_years']

styled_df = df.style\
    .background_gradient(subset=['salary'], cmap='Greens')\
    .highlight_max(subset=['salary'], color='lightgreen')\
    .highlight_min(subset=['salary'], color='red')\
    .format({'salary': '${:,.2f}'})\
    .hide(axis='index')

styled_df

# 1-2-3-4 Apply multiple styles to department summary
dept_summary = df.groupby('department')[['salary']].mean().reset_index()


def highlight_high_salary(s):
    return ['background-color: yellow' if v > 6000 else '' for v in s]


report = dept_summary.style\
    .apply(highlight_high_salary, subset=['salary'])\
    .set_caption("Rapporto Stipendio Medio per Dipartimento")\
    .format({'salary': '${:,.2f}'})\
    .set_properties(**{'border': '1px solid black', 'text-align': 'center'})

report
