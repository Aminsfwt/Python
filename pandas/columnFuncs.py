import ast
import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset # type: ignore

df = load_dataset("lukebarousse/data_jobs")
df_data = df['train'].to_pandas()

#conver job_posted_date from string to date
df_data["job_posted_date"] = pd.to_datetime(df_data.job_posted_date)

#APPLY FUNCTION TO A SPECIFIC COLUMN to convert string to list
def clean_list(skill_list):
    if pd.notna(skill_list):
        return ast.literal_eval(skill_list)
    else:
        return skill_list

df_data['job_skills'] = df_data['job_skills'].apply(clean_list)


#APPLY FUNCTION TO A SPECIFIC ROW
df_salary = df_data[pd.notna(df_data["salary_year_avg"])]

#function to raise the avg salary to all employees
def projected_salary(row):
    if "Senior" in row['job_title_short']:
        return 1.05 * row['salary_year_avg'] 
    else:
        return 1.03 * row['salary_year_avg'] 
    
df_salary['salary_year_inflated'] = df_salary.apply(projected_salary, axis=1) 

print(df_salary[['job_title_short', 'salary_year_avg', 'salary_year_inflated', 'job_country']])
    