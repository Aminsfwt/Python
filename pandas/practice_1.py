import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset # type: ignore

df = load_dataset("lukebarousse/data_jobs")
df_train = df['train'].to_pandas()


#print(df_train[["job_via", "job_title_short"]].iloc[20:90])

#print(df_train.iloc[20])

#print(df_train[["job_via", "job_title_short"]].info())



#dataAnalystjobs = df_train[(df_train.job_title_short == "Data Analyst") & (df_train.salary_year_avg > 10000)]
#print(dataAnalystjobs)

#conver job_posted_date fromobject to datetime and assign it to itself
df_train["job_posted_date"] = pd.to_datetime(df_train.job_posted_date)

#extract month from job_posted_date and assign it to new coloumn
df_train["job_posted_month"] = df_train.job_posted_date.dt.month

#sort dataset by job_posted_date
df_train.sort_values("job_posted_date", inplace=True)

#drop column salary_hour_avg from the dataset
#df_train.drop(labels='salary_hour_avg', axis=1, inplace=True)

#drop null values from salary_year_avg
#df_train.dropna(subset=['salary_year_avg'], inplace=True)

#descrianaltyics functions
#print(df_train['salary_year_avg'].median())

#info about min  salary_year_avg
#min_salary = df_train['salary_year_avg'].idxmin()

#the all unique jobs
#print(df_train["job_title_short"].unique())

#all job positions
#print(df_train["job_title_short"].value_counts())

#groub by method
#print(df_train.groupby("job_title_short")[["salary_year_avg", "salary_hour_avg"]].max())

#aggragation
#print(df_train.groupby("job_title_short")[["salary_year_avg", "salary_hour_avg"]].agg(["min", "max", "median"]))

#search
#print(df_train["job_country"].isin(["Egypt"]).any())

#simple project 
us_jobs = df_train[df_train["job_country"] == "United States"]
us_jobs = us_jobs[us_jobs["salary_year_avg"].notna()]
us_jobs.drop(labels='salary_hour_avg', axis=1, inplace=True)
groups = us_jobs.groupby("job_title_short")["salary_year_avg"].agg(["min", "max", "median"]).sort_values("median")
print(groups)
