from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler


def encode_to_numerical(file):
    cat_cols=['payFrequency', 'leadType', 'fpStatus', 'state']

    le= LabelEncoder()
    for col in cat_cols:
        file[col]=le.fit_transform(file[col])
        print(f"{col} encoding: {dict(zip(le.classes_, le.transform(le.classes_)))}")
    
    


    file.to_csv('data/encoded_cleaned_loan_data.csv',index=False)

    return file

def drop_var(file):
    file = file.drop(['clarityFraudId','underwritingid','originated','approved','isFunded','loanStatus','applicationDate','originatedDate','anon_ssn'])
    file.to_csv('data/encoded_cleaned_loan_data.csv',index=False)
    return file


def normalizer(file,var):
    scaler=MinMaxScaler()
    file[var]=scaler.fit_transform(file[[var]])
    return file






    
