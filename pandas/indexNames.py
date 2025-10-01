import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset # type: ignore

df_swJobs_pivot = pd.read_csv("software_jobs.csv", index_col='job_posted_month')
df = load_dataset("lukebarousse/data_jobs")
df_data = df['train'].to_pandas()

df_data["job_posted_date"] = pd.to_datetime(df_data.job_posted_date)
df_data.index.name = 'job_index'

df_usa = df_data[df_data['job_country'] == 'United States'].copy()


df_usa['job_posted_month'] = df_usa['job_posted_date'].dt.strftime('%B') 

df_usa_pivot = df_usa.pivot_table (
                        #values='job_country',
                        index='job_posted_month',
                        columns='job_title_short',
                        aggfunc='size'
)

df_usa_pivot.reset_index(inplace=True)
df_usa_pivot['month_no'] = pd.to_datetime(df_usa_pivot['job_posted_month'], format='%B').dt.month

df_usa_pivot.sort_values('month_no', inplace=True)
df_usa_pivot.set_index('job_posted_month', inplace=True)

df_usa_pivot.drop(columns='month_no', inplace=True)

top3Jobs = df_usa['job_title_short'].value_counts().head(3)
top3Jobs = top3Jobs.index.tolist()

mergedJobs = df_usa_pivot.merge(df_swJobs_pivot, on='job_posted_month')

top5Jobs = (
    mergedJobs
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .index
    .tolist()
)

print(top5Jobs)

mergedJobs[top5Jobs].plot(kind='line')
plt.ylabel('Job Counts')
plt.xlabel("2023")
plt.title('Top 3 Monthly Job Posted in USA')
plt.ylim(0,20000)
plt.legend()
plt.show()
