import preprocess
import visual
import statistics_summary
import statistical_tests
import pandas as pd

#read CSV
loan=preprocess.read_csv('data/loan.csv')
#considering funded loans, assuming human and auto underwriters do their job well
loan=preprocess.only_funded(loan)

#normalizing the value counts of loanstatus to see distribution and all the values
print(loan['loanStatus'].value_counts(normalize=True))

#considering loan status as the dependent
loan=preprocess.default(loan)
loan=preprocess.time_to_approve(loan)
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
sstats = statistics_summary.summary_statistics(loan)
sstats.to_csv("data/statistics_summary.csv", index=True)

#plotting
visual.plot_histograms(loan, 'apr')
visual.plot_histograms(loan, 'loanAmount')
visual.plot_histograms(loan, 'originallyScheduledPaymentAmount')
#not symmetrical skewed.defaulters tend to take lower loans and lower payment amount.
#checking whether the default has clarityFraudID
#testing for statistical significance using mann-whitney
statistical_tests.manwhit(loan,'loanAmount')
statistical_tests.manwhit(loan,'originallyScheduledPaymentAmount')
#not much significant difference between the two as p>0.05, no difference between the distribution of two groups.



preprocess.clarity_id_checker(loan)
loan_with_only_clarity_id=preprocess.read_csv('data/with_CF_ID.csv')
underwriting=preprocess.read_csv('data/clarity_underwriting_variables.csv')
#merging the two
merged_data_loan_underwriting = loan_with_only_clarity_id.merge(underwriting, left_on='clarityFraudId', right_on='underwritingid', how='inner')
merged_data_loan_underwriting.to_csv("data/merged_data_loan_underwriting.csv",index=False)
merged_data=preprocess.read_csv("data/merged_data_loan_underwriting.csv")

#summary of merge
stats_merged_data=statistics_summary.summary_statistics(merged_data)
stats_merged_data.to_csv("data/statistics_summary_CF.csv",index=True)

#defaulters have lower number of inquiries across
#defaulters have lower mean and stdev values of unique fraud indicator, meaning higher likelihood of default
#generally higher clear fraud score for defaulters than non defaulters
#mean 692 and stdev 142 for defaulters and 685 mean and 127 stdev
#defaults=preprocess.default(payment)


#Feature Engineering
#loan_df = preprocess.read_csv('data/cleaned_loaned_data.csv')
#visual.plot_payFrequency_loanAmount(loan_df)

#merging clean_loan_data and payment
payment=preprocess.read_csv("data/payment.csv")
cleaned_loaned_data=preprocess.read_csv("data/cleaned_loaned_data.csv")
merged_data_loan_payment=cleaned_loaned_data.merge(payment,on="loanId")
merged_data_loan_payment.to_csv("data/merged_data_loan_payment.csv",index=False)

visual.scatter_plot(merged_data_loan_underwriting,'loanAmount','clearfraudscore' )

visual.heat_map_pay_frequency_APR(loan,'loanAmount','apr')
#loan amount less than 1000 and higher apr tend to default more
visual.heat_map_pay_frequency_APR(loan,'loanAmount','timeToApprove')
#shorter approval time for low loan amount ~<500, defaulters tend to be in this range