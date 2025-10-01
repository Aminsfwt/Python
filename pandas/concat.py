import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset # type: ignore

df = load_dataset("lukebarousse/data_jobs")
df_data = df['train'].to_pandas()

df_data["job_posted_date"] = pd.to_datetime(df_data.job_posted_date)

df_data['job_posted_month'] = df_data["job_posted_date"].dt.strftime('%b')

#split months
months = df_data["job_posted_month"].unique()

dictMonths = {month : df_data[df_data['job_posted_month'] == month] for month in months }

Quarter_1 = pd.concat([dictMonths['Jan'], dictMonths['Feb'], dictMonths['Mar']], ignore_index=True)

#print(Quarter_1['job_posted_month'].value_counts())

Quarter_1.to_csv('Q_1_Jobs.csv')

"""Quarter_1['job_posted_month'].value_counts().plot(kind='pie')
plt.show()"""