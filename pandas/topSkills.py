import ast
import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset # type: ignore

df = load_dataset("lukebarousse/data_jobs")
df_data = df['train'].to_pandas()

#conver job_posted_date from string to date
df_data["job_posted_date"] = pd.to_datetime(df_data.job_posted_date)

#APPLY FUNCTION TO A SPECIFIC COLUMN to convert string to list

df_data['job_skills'] = df_data['job_skills'].apply(lambda skill_list: ast.literal_eval(skill_list) if pd.notna(skill_list) else skill_list)

skillsExploded = df_data.explode('job_skills')

skillsCount = skillsExploded.groupby(['job_skills', 'job_title_short']).size()

df_skillsCount = skillsCount.reset_index(name='skills_count')

df_skillsCount = df_skillsCount.sort_values(by='skills_count', ascending=False)

job_title = 'Data Analyst'
topskills = 10
df_topSkills = df_skillsCount[df_skillsCount['job_title_short'] == job_title].head(10)

print(df_topSkills)

df_topSkills.plot(kind='barh', x='job_skills', y='skills_count')
plt.gca().invert_yaxis()
plt.title(f'Top {topskills} Skills for {job_title}')
plt.xlabel('job posting count')
plt.ylabel(f'{job_title} top {topskills} skills')
plt.legend.set_visible(False)
plt.show()