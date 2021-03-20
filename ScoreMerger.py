import pandas as pd

df = pd.read_csv("/content/Merged DB-Grid view (1).csv") #path to original csv
df2 = df.groupby(['Name','Email-ID']).sum() #sums common columns for rows with same keys (name and email here)
sorted_df = df2.sort_values(by=["Sum"], ascending=False) #sort by total score for ranks
print(sorted_df)
sorted_df.to_csv('/content/Stuff/r2db.csv', index=True) #save final csv
