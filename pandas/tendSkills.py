import ast
import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset # type: ignore

df = load_dataset("lukebarousse/data_jobs")
df_data = df['train'].to_pandas()

#convert job_posted_date from string to date
df_data["job_posted_date"] = pd.to_datetime(df_data.job_posted_date)

df_data['job_skills'] = df_data['job_skills'].apply(lambda skill: ast.literal_eval(skill) if pd.notna(skill) else skill)

df_DA = df_data[df_data['job_title_short'] == "Data Engineer"].copy()

df_DA['job_posted_month_no'] = df_DA['job_posted_date'].dt.month

df_DA_explode = df_DA.explode('job_skills') 

pivoted_DA = df_DA_explode.pivot_table(
                index='job_posted_month_no',
                columns='job_skills',
                aggfunc='size',
                fill_value=0 
)

pivoted_DA.loc['total'] = pivoted_DA.sum()

pivoted_DA = pivoted_DA[pivoted_DA.loc['total'].sort_values(ascending=False).index]

pivoted_DA = pivoted_DA.drop('total')

pivoted_DA = pivoted_DA.reset_index()

pivoted_DA['job_posted_month'] = pivoted_DA['job_posted_month_no'].apply(lambda x: pd.to_datetime(x, format='%m').strftime('%b'))

pivoted_DA = pivoted_DA.set_index('job_posted_month')

pivoted_DA = pivoted_DA.drop(columns='job_posted_month_no')

topSkills = pivoted_DA.iloc[:,:5]

topSkills.plot(kind='line')
plt.title(f'Top')
plt.show()

print(pivoted_DA)