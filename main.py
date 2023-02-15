import pandas as pd
import cleaner

loan=cleaner.read_csv('data/loan.csv')
loan=cleaner.cleanBlanks(loan)

#payment=pd.read_csv('data/payment.csv')
#underwriting=pd.read_csv('data/clarity_underwriting_variables.csv')



