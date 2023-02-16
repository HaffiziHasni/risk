import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def bar_for_leadtype(file):
    leadType_counts = file['leadType'].value_counts()
    plt.bar(leadType_counts.index, leadType_counts.values)
    plt.title('Count of Lead Type')
    plt.xlabel('Lead Type')
    plt.ylabel('Count')
    plt.show()
    return file

def relation_leadtype_default(file):
    leadType_counts = pd.crosstab(index=file['leadType'],columns=file['default'])
    leadType_counts.plot(kind='bar')
    plt.title("distribution of leadtype by default")
    plt.xlabel("Lead Type")
    plt.ylabel("Count")
    plt.show()
    return file


def plot_histograms(file, variable):
    # Create two subplots
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Plot histogram for default group
    ax[0].hist(file[file['default'] == 1][variable], bins=20, alpha=0.5, label='Default')
    ax[0].set_xlabel(variable)
    ax[0].set_ylabel('Frequency')
    ax[0].legend()

    # Plot histogram for non-default group
    ax[1].hist(file[file['default'] == 0][variable], bins=20, alpha=0.5, label='Non-default')
    ax[1].set_xlabel(variable)
    ax[1].set_ylabel('Frequency')
    ax[1].legend()

    # Set plot title
    fig.suptitle(f'Distribution of {variable} between Default and Non-default groups')

    plt.show()
    return file



def plot_payFrequency_loanAmount(file):
     # Filter for default and non-default loans
    default_file = file[file['default'] == 1]
    nondefault_file = file[file['default'] == 0]
    plt.figure()
    plt.scatter(default_file['loanAmount'], default_file['leadCost'], c='r', label='Default')
    plt.xlabel('Loan Amount')
    plt.ylabel('lead Cost')
    plt.legend()

    # Create scatter plot of payFrequency against loanAmount for non-default loans
    plt.figure()
    plt.scatter(nondefault_file['loanAmount'], nondefault_file['leadCost'], c='b', label='Non-Default')
    plt.xlabel('Loan Amount')
    plt.ylabel('lead Cost')
    plt.legend()

    plt.show()
    return file

def heat_map(file,x_var, y_var):
    g = sns.lmplot(x=x_var,y=y_var, hue='default',data=file, fit_reg=False)
    g.set_titles("{col_name}")
    g.add_legend()
    plt.show()
    return file
   
def scatter_plot(file,x_var,y_var):
    default_mask = file['default'] == True
    sns.scatterplot(x=x_var, y=y_var, hue=default_mask, data=file)
    plt.show()
    return file








