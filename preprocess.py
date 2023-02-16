import pandas as pd

def read_csv(filepath):
    df = pd.read_csv(filepath, encoding='latin-1')

    return df

def only_funded(file):
    file = file[file['isFunded'] == 1]
    file.to_csv("data/cleaned_loaned_data.csv",index=False)
    return file


""""Charged Off" and "Settled Bankruptcy" are more severe loan statuses that suggest that the borrower has defaulted on their loan,
 indicating that they are not able to repay the loan. As a result, it may make more sense to focus on these two loan statuses as the primary indicators of default."""
def default(file):
    file['default'] = file['loanStatus'].apply(lambda x: 1 if x in ['Charged Off', 'Settled Bankruptcy'] else 0)
    file.to_csv("data/cleaned_loaned_data.csv",index=False)
    return file

def time_to_approve(file):
    file['applicationDate'] = pd.to_datetime(file['applicationDate'])
    file['originatedDate'] = pd.to_datetime(file['originatedDate'])
    file['timeToApprove']=(file['originatedDate']-file['applicationDate']).astype('timedelta64[h]')
    file.to_csv("data/cleaned_loaned_data.csv",index=False)
    return file
                           
    
def blank_checker(file):
     for column in file.columns:
        if file[column].isna().any():
            print(f"Column '{column}' has blank values.")

    

def blank_filler(file):
    file['nPaidOff']=file['nPaidOff'].fillna(0)
    return file


def clarity_id_checker(file):
    filter_file=file[file['hasCF']==1]
    filter_file.to_csv("data/with_CF_ID.csv",index=False)
    return file





    



