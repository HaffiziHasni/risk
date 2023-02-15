import matplotlib.pyplot as plt
import pandas as pd


def bar_for_leadtype(file):
    leadType_counts = file['leadType'].value_counts()
    plt.bar(leadType_counts.index, leadType_counts.values)
    plt.title('Count of Lead Type')
    plt.xlabel('Lead Type')
    plt.ylabel('Count')
    plt.show()

def relation_leadtype_default(file):
    leadType_counts = pd.crosstab(index=file['leadType'],columns=file['default'])
    leadType_counts.plot(kind='bar')
    plt.title("distribution of leadtype by default")
    plt.xlabel("Lead Type")
    plt.ylabel("Count")
    plt.show()


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


