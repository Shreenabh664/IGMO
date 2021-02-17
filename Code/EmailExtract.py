import pandas as pd
data = pd.read_csv("path/to/csv", index_col=False)
data.reset_index()
data.query('Status == "TAG"', inplace = True) #tag of which emails are to be extracted
pd.set_option('display.max_rows', None)
print('\n \n')
print(', \n'.join(data['Email-ID']))
