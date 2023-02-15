import preprocess
import visual
#read CSV
loan=preprocess.read_csv('data/loan.csv')
#considering funded loans, assuming human and auto underwriters do their job well
loan=preprocess.only_funded(loan)

#normalizing the value counts of loanstatus to see distribution and all the values
print(loan['loanStatus'].value_counts(normalize=True))

#considering loan status as the dependent
loan=preprocess.default(loan)

#payment=preprocess.read_csv('data/payment.csv')
preprocess.blank_checker(loan)
#we can see 3 columns has blank values however fpstatus have intentional blanks so we can say two.can't say much about clarity id since it's just ID so we look to npaidoff, assuming we can change the nan to 0
preprocess.blank_filler(loan)
loan=preprocess.read_csv('data/cleaned_loaned_data.csv')

#visual.bar_for_leadtype(loan)
#by mandatory has the most, and by distribution also similar for 1 and 0 for default, not much to go on
#checking how much they owe maybe? try checking the relations of all variables except for IDs

# Group the data by the default column


# Get the summary statistics for each group
sstats = preprocess.summary_statistics(loan)
sstats.to_csv("data/statistics_summary.csv", index=True)

visual.plot_histograms(loan, 'apr')
visual.plot_histograms(loan, 'loanAmount')
visual.plot_histograms(loan, 'originallyScheduledPaymentAmount')

#checking whether the default has clarityFraudID
preprocess.clarity_id_checker(loan)
loan_with_only_clarity_id=preprocess.read_csv('data/with_CF_ID.csv')


#defaults=preprocess.default(payment)
#underwriting=pd.read_csv('data/clarity_underwriting_variables.csv')




