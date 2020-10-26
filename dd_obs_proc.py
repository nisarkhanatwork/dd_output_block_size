import pandas
from matplotlib import pyplot as plt

col_names = ['block-size', 'transfer-rate']

obs_df = pandas.read_csv('obs_data.txt', sep = ':', names = col_names)

clean_obs_df = obs_df.replace(regex = {r'\s*block size\s*' : pandas.np.nan, 
                                        r'\s*transfer rate\s*' : pandas.np.nan})
# create data for indices
data_index = pandas.np.repeat(pandas.np.arange(start = 1, stop = 101), 19, axis = 0)

col_df_for_pivot = pandas.DataFrame(data = data_index)

final_df = col_df_for_pivot.join(clean_obs_df)
final_df = final_df.rename(columns = {0: "rows"})

df_after_pivot = final_df.pivot(index = 'rows', columns = 'block-size',
                                values = 'transfer-rate')
df_after_pivot = df_after_pivot.dropna(axis = 'columns').astype('float64')

stats_df = df_after_pivot.describe()
range1 = pandas.np.arange(start = 0, stop = 10)
range2 = pandas.np.arange(start = 10, stop = 18)
print(stats_df.take(range1, axis = 1))
print(stats_df.take(range2, axis = 1))


