import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset # type: ignore

df = load_dataset("lukebarousse/data_jobs")
df_data = df['train'].to_pandas()

df_data["job_posted_date"] = pd.to_datetime(df_data.job_posted_date)

median_year_salary = df_data["salary_year_avg"].median()
median_hour_salary = df_data["salary_hour_avg"].median()

df_filled = df_data.copy()

df_filled["salary_year_avg"] = df_filled["salary_year_avg"].fillna(median_year_salary)  
df_filled["salary_hour_avg"] = df_filled["salary_hour_avg"].fillna(median_hour_salary)

df_unique = df_filled.copy()

#df_unique = df_unique.drop_duplicates(subset=["job_title", "company_name"])

#print(df_filled.sample(5,random_state=42))
#print(len(df_filled) - len(df_unique))

#print(df_unique.loc[:, ["salary_year_avg", "salary_hour_avg"]])

#PIVOT Tables
#pivotJobs = df_unique.pivot_table(index='job_title_short', aggfunc='size')

#pivot table: median salary for jobs per counteries
#pivotJobs = df_data.pivot_table(values='salary_year_avg', index='job_country', columns='job_title_short', aggfunc='median')

#get top 5 countries
topCountries = df_data['job_country'].value_counts().head(5).index

topCountriesMedianSalaies = df_data.pivot_table(
                            values='salary_year_avg',
                            index='job_country',
                            columns='job_title_short',
                            aggfunc='median'
)

topCountriesMedianSalaies = topCountriesMedianSalaies.loc[topCountries]

jobTitles = ['Data Analyst', 'Data Engineer', 'Data Scientist']

topCountriesMedianSalaies = topCountriesMedianSalaies.loc[topCountries, jobTitles].sort_values('job_country', ascending=False)

print(topCountriesMedianSalaies)

"""
topCountriesMedianSalaies.plot(kind='bar')
plt.ylabel('Median Salary ($)')
plt.xlabel("Top 5 Countries")
plt.title('Top 5 Countries Median Salaies')
plt.xticks(rotation=45, ha='right')
plt.show()
"""
