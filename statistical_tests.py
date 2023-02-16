from scipy.stats import mannwhitneyu

def manwhit(file,variable):
   defaulters = file[file['default'] == 1][variable]
   non_defaulters = file[file['default'] == 0][variable]
   stat, p = mannwhitneyu(defaulters, non_defaulters)
   # Print the results
   print(f'Mann-Whitney U test for loan amount:\nStatistic={stat:.2f}, p-value={p:.4f}')
   return file