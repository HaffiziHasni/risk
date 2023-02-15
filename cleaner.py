import pandas as pd

def read_csv(filepath):
    df = pd.read_csv(filepath, encoding='latin-1',dtype=str)

    return df

def cleanBlanks(file):
    file =file[~file.loanId.isnull() & ~file.originated.isnull() & ~file.loanAmount.isnull()]
    file.to_csv("data/cleaned_loaned_data.csv",index=False)
    return file



