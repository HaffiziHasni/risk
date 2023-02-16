import pandas as pd

def summary_statistics(file):
    # create separate dataframes for defaults and non-defaults
    defaults = file[file['default'] == 1]
    non_defaults = file[file['default'] == 0]

    # compute summary statistics for each dataframe
    default_stats = defaults.describe(include='all')
    non_default_stats = non_defaults.describe(include='all')

    # combine the summary statistics into a single dataframe
    stats = pd.concat([default_stats, non_default_stats], axis=0, keys=['Default', 'Non-Default'])

    return stats

